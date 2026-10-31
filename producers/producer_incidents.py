from confluent_kafka import Producer
import json, time, random
from datetime import datetime, timezone

conf = {'bootstrap.servers': "127.0.0.1:9092"}
producer = Producer(conf)

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def delivery_report(err, msg):
    if err is not None:
        print(f"❌ Erreur d'envoi: {err}")

def main():
    print("Démarrage du producteur Incidents...")
    cities = ["Marrakech", "Casa", "Rabat"]
    incident_types = ["ACCIDENT", "ROUTE_FERMEE", "TRAVAUX"]

    try:
        while True:
            city = random.choice(cities)
            event = {
                "incident_id": f"INC_{random.randint(100, 999)}",
                "city": city,
                "type": random.choice(incident_types),
                "severity": random.randint(1, 5),
                "ts": now_iso()
            }

            producer.produce(
                'incidents',
                value=json.dumps(event).encode('utf-8'),
                callback=delivery_report
            )
            producer.poll(0)
            print(f"Incident envoyé: {event['incident_id']} | Type: {event['type']} | Sévérité: {event['severity']}")
            time.sleep(5)

    except KeyboardInterrupt:
        print("\nArrêt du producteur Incidents.")
    finally:
        producer.flush()

if __name__ == "__main__":
    main()