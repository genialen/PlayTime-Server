import logging
import os

LOG_FILE_PATH = os.path.join(os.getcwd(), "logs", "playtime.log")

# Настройка логирования
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(message):
    """
    Записывает информационные сообщения в лог.
    """
    logging.info(message)
    print(f"INFO: {message}")

def log_error(message):
    """
    Записывает сообщения об ошибках в лог.
    """
    logging.error(message)
    print(f"ERROR: {message}")
