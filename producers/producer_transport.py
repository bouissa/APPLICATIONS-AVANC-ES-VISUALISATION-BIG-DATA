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
    print("Démarrage du producteur Transport...")
    cities = ["Marrakech", "Casa", "Rabat"]
    lines = ["L1", "L3", "L5", "T2"]

    try:
        while True:
            city = random.choice(cities)

            event = {
                "vehicle_id": f"BUS_{random.randint(1, 20)}",
                "line": random.choice(lines),
                "city": city,
                "lat": round(random.uniform(31.0, 32.0), 4),
                "lon": round(random.uniform(-8.5, -7.5), 4),
                "speed": round(random.uniform(10, 60), 1),
                "delay_min": random.choice([0, 0, 2, 5, 8, 12]),
                "ts": now_iso()
            }

            producer.produce(
                'transport_events',
                value=json.dumps(event).encode('utf-8'),
                callback=delivery_report
            )
            producer.poll(0)
            print(f"Transport envoyé: {event['vehicle_id']} | Retard: {event['delay_min']} min")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nArrêt du producteur Transport.")
    finally:
        producer.flush()

if __name__ == "__main__":
    main()