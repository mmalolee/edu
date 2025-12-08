import logging
import logging.config


cfg = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standardowy": {
            "format": "%(asctiime)s :[%(levelname)s], %(message)s",
            "datefmt": "%d-%m-%d -> %H:%M:%S",
        },
        "prościutki": {"format": "%(levelname)s: %(message)s"},
    },
    "handlers": {
        "w_konsoli": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "prościutki",
            "stream": "ext://sys.stdout",
        },
        "plik": {
            "class": "logging.FileHandler",
            "level": "ERROR",
            "formatter": "standardowy",
            "filename": "bledy_modelu.log",
            "mode": "a",
        },
    },
    "loggers": {
        "": {"handlers": ["w_konsoli", "plik"], "level": "INFO", "propagate": True}
    },
}
