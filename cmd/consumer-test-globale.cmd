@echo off
echo ========================================================
echo  Ecoute Globale de TOUS les topics Kafka (SmartCity)
echo ========================================================
cd /d "C:\kafka"

:: L'option --include utilise une Regex. ".*" signifie "n'importe quel caractère, autant de fois que nécessaire"
:: Cela permet d'écouter transport_events, air_quality, incidents, et tout autre topic existant.
.\bin\windows\kafka-console-consumer.bat --bootstrap-server 127.0.0.1:9092 --include ".*" --from-beginning --property print.topic=true
pause