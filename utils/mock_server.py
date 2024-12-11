from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/login', methods=['POST'])
def login():
    """
    Обработчик запросов на логин.
    Проверяет данные и возвращает имитацию ответа сервера.
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Пример проверки логина и пароля
    if username == "1" and password == "1":
        return jsonify({"status": "success", "message": "Login successful!"})
    else:
        return jsonify({"status": "fail", "message": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(debug=True)
