@echo off
echo Écoute du flux 'transport_events'
cd /d "C:\kafka"
.\bin\windows\kafka-console-consumer.bat --bootstrap-server 127.0.0.1:9092 --topic air_quality --from-beginning
pause