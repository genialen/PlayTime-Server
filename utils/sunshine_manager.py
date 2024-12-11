import subprocess
import os
import psutil
import time
import requests

SUNSHINE_PATH = r"C:\Users\Kudahter\PycharmProjects\PlayTime Server\utils\sunshine\sunshine.exe"


def start_sunshine():
    """
    Запускает Sunshine через оболочку cmd.
    """
    print(f"Попытка запуска Sunshine по пути: {SUNSHINE_PATH}")
    if not os.path.exists(SUNSHINE_PATH):
        raise FileNotFoundError(f"Sunshine не найден по пути {SUNSHINE_PATH}")

    try:
        # Запуск Sunshine через cmd.exe
        process = subprocess.Popen(
            ["cmd.exe", "/c", SUNSHINE_PATH],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        time.sleep(5)  # Даем время на запуск
        print("Sunshine запущен.")

        if is_sunshine_active():
            print("Sunshine успешно запущен и доступен.")
        else:
            print("Sunshine запущен, но веб-интерфейс недоступен.")
    except Exception as e:
        print(f"Ошибка запуска Sunshine: {e}")
        raise RuntimeError(f"Ошибка запуска Sunshine: {e}")

def is_sunshine_running():
    """
    Проверяет, запущен ли процесс Sunshine.
    """
    for process in psutil.process_iter(['name']):
        if process.info['name'] == 'sunshine.exe':
            return True
    return False

def is_sunshine_active():
    """
    Проверяет, доступен ли веб-интерфейс Sunshine.
    """
    import requests
    try:
        response = requests.get("https://localhost:47990", verify=False, timeout=5)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Ошибка проверки Sunshine через порт: {e}")
        return False

def stop_sunshine():
    """
    Останавливает процесс Sunshine.
    """
    for process in psutil.process_iter():
        if process.name() == 'sunshine.exe':
            process.terminate()
            print("Sunshine остановлен.")
            return
    print("Sunshine не найден.")
