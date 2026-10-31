@echo off
echo Création des topics de SmartCity...
cd /d "C:\kafka"

echo 1. Création du topic 'transport_events'
.\bin\windows\kafka-topics.bat --create --topic transport_events --bootstrap-server localhost:9092 --partitions 2 --replication-factor 1

echo 2. Création du topic 'air_quality'
.\bin\windows\kafka-topics.bat --create --topic air_quality --bootstrap-server localhost:9092 --partitions 2 --replication-factor 1

echo 3. Création du topic 'incidents'
.\bin\windows\kafka-topics.bat --create --topic incidents --bootstrap-server localhost:9092 --partitions 2 --replication-factor 1

echo.
echo Liste des topics existants :
.\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092
pause