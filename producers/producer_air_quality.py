from confluent_kafka import Producer
import json, time, random
from datetime import datetime, timezone

# Configuration du producteur Kafka
conf = {'bootstrap.servers': "127.0.0.1:9092"}
producer = Producer(conf)

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def delivery_report(err, msg):
    if err is not None:
        print(f"❌Erreur d'envoi: {err}")


def main():
    print("Démarrage du producteur Qualité de l'Air")
    cities = ["Marrakech", "Casa", "Rabat"]

    try:
        while True:
            city = random.choice(cities)
            # Génération d'un événement air
            # On simule parfois une pollution (pm25 > 35 ou co2 > 900)
            event = {
                "sensor_id": f"AQ_{random.randint(1, 10)}",
                "city": city,
                "pm25": round(random.uniform(5.0, 50.0), 1),
                "co2": round(random.uniform(400, 1000), 0),
                "ts": now_iso()
            }
            # Envoi vers le topic air_quality
            producer.produce(
                'air_quality',
                value=json.dumps(event).encode('utf-8'),
                callback=delivery_report
            )

            producer.poll(0)
            print(f"Air envoyé: {event['sensor_id']} | PM2.5: {event['pm25']} | CO2: {event['co2']}")
            time.sleep(1.5)  # 1 événement toutes les 1.5 secondes

    except KeyboardInterrupt:
        print("\nArrêt du producteur Air.")
    finally:
        producer.flush()

if __name__ == "__main__":
    main()