# SmartCity Real-Time – Transport & Air Quality

**Mini-projet Big Data | Applications avancées & Big Data**

## Présentation

SmartCity Real-Time est une solution Big Data basée sur une architecture **Kappa**, permettant de simuler, collecter, traiter et visualiser des données urbaines en temps réel.

Le projet couvre trois domaines :
- **Transport intelligent** : suivi des bus et tramways (position, vitesse et retard).
- **Qualité de l'air** : surveillance des niveaux de PM2.5 et de CO2.
- **Incidents urbains** : détection et suivi des événements (accidents, routes fermées, etc.).

## Objectifs

- **Ingestion** : génération et collecte de flux JSON avec Python et Apache Kafka.
- **Traitement** : transformation et agrégation des données avec Spark Structured Streaming.
- **Stockage** : persistance des indicateurs et des états courants dans PostgreSQL.
- **Visualisation** : création d'un tableau de bord interactif avec Power BI (DirectQuery).

## Architecture du projet

Le pipeline repose sur les composants suivants :

```text
Python Producers
       |
       v
   Apache Kafka
       |
       v
Spark Structured Streaming
       |
       v
   PostgreSQL
       |
       v
    Power BI
```

### Technologies utilisées

| Technologie | Rôle |
|---|---|
| Python | Simulation et production des événements |
| Apache Kafka 4 (KRaft) | Ingestion et transmission des flux |
| Apache Spark 3.5.8 | Traitement en streaming et calcul des KPI |
| PostgreSQL | Stockage des données et indicateurs |
| Power BI Desktop | Visualisation et reporting |
| Java JDK 17 | Environnement d'exécution Spark |

## Topics Kafka

Trois topics sont utilisés pour organiser les événements :

- `transport_events` : événements des véhicules.
- `air_quality` : mesures des capteurs de qualité de l'air.
- `incidents` : événements et incidents urbains.

## Indicateurs clés (KPI)

Les données sont traitées à travers des fenêtres temporelles d'une minute.

| Domaine | Indicateur | Description |
|---|---|---|
| Transport | `avg_speed` | Vitesse moyenne des véhicules |
| Transport | `late_count` | Nombre d'événements avec plus de 5 minutes de retard |
| Air | `avg_pm25` | Moyenne des mesures PM2.5 |
| Air | `pollution_count` | Nombre de mesures dépassant les seuils configurés |
| Incidents | `incident_count` | Nombre d'incidents enregistrés |
| Incidents | `max_severity` | Niveau maximal de sévérité |

**Seuils de détection configurés :**
- Retard : `delay_min > 5`
- Pollution : `PM2.5 > 35 µg/m³` ou `CO2 > 900 ppm`
- Incident sévère : `severity >= 3`

Les tables `transport_latest` et `air_latest` conservent également le dernier état connu de chaque véhicule et capteur.

## Structure du projet

```text
pythonProject_smartcity_bigdata/
│
├── cmd/
│   ├── start-kafka.cmd
│   ├── create-topic.cmd
│   ├── consumer-air-quality-console.cmd
│   ├── consumer-incidents-console.cmd
│   ├── consumer-test-globale.cmd
│   └── consumer-trans-enevts-console.cmd
│
├── producers/
│   ├── producer_air_quality.py
│   ├── producer_Groupe_smartcity.py
│   ├── producer_incidents.py
│   └── producer_transport.py
│
├── spark_streaming/
│   └── stream_smartcity_to_postgres_kpi.py
│
├── sql/
│   └── Script_PostgreSQL.sql
│
├── checkpoints/
│   ├── transport_latest/
│   ├── transport_kpi/
│   ├── air_latest/
│   ├── air_kpi/
│   └── incidents_kpi/
│
├── venv/
├── requirements.txt
└── README.md
```

## Prérequis

- Windows 10/11
- Python 3.9+
- Java JDK 17
- Apache Kafka 4 (KRaft)
- Apache Spark 3.5.8
- PostgreSQL
- Power BI Desktop

## Installation

**1. Cloner le projet**

```bash
git clone <URL_DU_DEPOT>
cd pythonProject_smartcity_bigdata
```

**2. Activer l'environnement virtuel**

```powershell
.\venv\Scripts\activate
```

**3. Installer les dépendances**

```bash
pip install -r requirements.txt
```

## Démarrage du projet

Suivre cet ordre d'exécution :

**1. Démarrer Kafka**

```powershell
.\cmd\start-kafka.cmd
```

**2. Créer les topics Kafka**

```powershell
.\cmd\create-topic.cmd
```

**3. Initialiser PostgreSQL**

Exécuter le script `sql/Script_PostgreSQL.sql` dans PostgreSQL pour créer la base et les tables nécessaires.

**4. Démarrer les producteurs Python**

Lancer les scripts du dossier `producers/` pour générer les événements :

```bash
python producers/producer_transport.py
python producers/producer_air_quality.py
python producers/producer_incidents.py
```

**5. Démarrer Spark Structured Streaming**

```bash
python spark_streaming/stream_smartcity_to_postgres_kpi.py
```

**6. Visualiser les résultats**

Connecter Power BI Desktop à PostgreSQL en utilisant le mode **DirectQuery**, puis consulter le tableau de bord SmartCity.

## Stockage PostgreSQL

La base de données contient cinq tables principales :

| Table | Description |
|---|---|
| `transport_latest` | Dernier état des véhicules |
| `air_latest` | Dernières mesures des capteurs |
| `transport_kpi_1min` | KPI transport par minute |
| `air_kpi_1min` | KPI qualité de l'air par minute |
| `incidents_kpi_1min` | KPI incidents par minute |

## Résultat attendu

Le tableau de bord Power BI permet de suivre :
- Les positions et les retards des véhicules.
- L'évolution des indicateurs de qualité de l'air.
- Le nombre et la sévérité des incidents.
- Les KPI calculés sur des fenêtres d'une minute.
- Le dernier état connu des véhicules et des capteurs.

## Auteurs

**Projet académique – Applications avancées & Big Data**

Réalisé dans le cadre d'un mini-projet SmartCity.

---

*SmartCity Real-Time – Turning urban data into actionable insights.*