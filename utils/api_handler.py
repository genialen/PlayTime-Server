import requests

# Конфигурация API
API_URL = "http://127.0.0.1:5000/api/login"  # URL mock-сервера

def authenticate(username, password):
    """
    Функция для отправки логина и пароля на сервер.
    :param username: Логин пользователя
    :param password: Пароль пользователя
    :return: Результат запроса (словарь)
    """
    try:
        # Отправка POST-запроса на сервер
        response = requests.post(
            API_URL,
            json={"username": username, "password": password},
            timeout=10  # Тайм-аут на случай задержек
        )
        response.raise_for_status()  # Проверка на HTTP ошибки
        return response.json()  # Возврат ответа в формате JSON
    except requests.exceptions.RequestException as e:
        # Обработка ошибок подключения
        return {"error": str(e)}

import requests
from requests.auth import HTTPBasicAuth

def get_sunshine_apps():
    """
    Получить список приложений (игр) через API Sunshine.
    """
    try:
        response = requests.get(
            "https://localhost:47990/api/apps",
            auth=HTTPBasicAuth('sunshine', '123321123'),  # Укажите реальные данные администратора
            verify=False,  # Отключаем проверку сертификата (если используется самоподписанный сертификат)
            timeout=10
        )
        response.raise_for_status()
        return response.json()  # Возвращаем JSON-ответ
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


