import logging
import logging.config
import json

with open("cfg.json", "r") as f:
    log_config = json.load(f)

logging.config.dictConfig(log_config)
logger = logging.getLogger(__name__)

logger.info("Rozpoczęto wczytywanie danych treningowych")
logger.warning("Nie znaleziono pliku konfiguracji, używam domyślnych parametrów.")
logger.error("Błąd połączenia z bazą danych modeli!")
