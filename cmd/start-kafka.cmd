@echo off
echo Démarrage du serveur Kafka...
cd /d "C:\kafka"
.\bin\windows\kafka-server-start.bat config\broker.properties
pause