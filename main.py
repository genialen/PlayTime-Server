from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from utils.sunshine_manager import start_sunshine, stop_sunshine, is_sunshine_running, is_sunshine_active
from utils.logger import log_info, log_error
from utils.api_handler import authenticate


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PlayTime - Вход")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        # Поля для ввода логина и пароля
        self.label_username = QLabel("Логин:")
        self.input_username = QLineEdit()
        layout.addWidget(self.label_username)
        layout.addWidget(self.input_username)

        self.label_password = QLabel("Пароль:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)

        # Кнопка входа
        self.login_button = QPushButton("Войти")
        self.login_button.clicked.connect(self.handle_login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def handle_login(self):
        """
        Обработчик кнопки входа.
        """
        username = self.input_username.text()
        password = self.input_password.text()

        if not username or not password:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите логин и пароль.")
            log_error("Попытка входа с пустыми данными.")
            return

        log_info(f"Попытка входа с логином: {username}")
        result = authenticate(username, password)

        if result.get("status") == "success":
            log_info("Успешный вход.")
            self.open_main_window()
        else:
            error_message = result.get("error", "Ошибка аутентификации.")
            QMessageBox.critical(self, "Ошибка", error_message)
            log_error(f"Ошибка входа: {error_message}")

    def open_main_window(self):
        """
        Открывает основное окно после успешного входа.
        """
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PlayTime - Сервер управления")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Статус Sunshine
        self.label_status = QLabel("Инициализация Sunshine...")
        layout.addWidget(self.label_status)

        # Кнопка для перезапуска Sunshine
        self.restart_button = QPushButton("Перезапустить Sunshine")
        self.restart_button.clicked.connect(self.restart_sunshine)
        layout.addWidget(self.restart_button)

        self.setLayout(layout)

        # Инициализация Sunshine
        self.init_sunshine()

    def init_sunshine(self):
        """
        Инициализация Sunshine при запуске приложения.
        """
        try:
            start_sunshine()
            self.update_sunshine_status()
        except Exception as e:
            self.label_status.setText("Ошибка запуска Sunshine")
            log_error(f"Ошибка запуска Sunshine: {e}")

    def update_sunshine_status(self):
        """
        Проверяет статус Sunshine.
        """
        if is_sunshine_running() and is_sunshine_active():
            self.label_status.setText("Sunshine: Запущен и активен")
            log_info("Sunshine успешно запущен.")
        elif is_sunshine_running():
            self.label_status.setText("Sunshine: Запущен, но порт недоступен")
            log_error("Sunshine запущен, но веб-интерфейс недоступен.")
        else:
            self.label_status.setText("Sunshine: Не запущен")
            log_error("Sunshine не запущен.")

    def restart_sunshine(self):
        """
        Перезапускает Sunshine.
        """
        try:
            stop_sunshine()
            start_sunshine()
            self.update_sunshine_status()
            log_info("Sunshine успешно перезапущен.")
        except Exception as e:
            log_error(f"Ошибка перезапуска Sunshine: {e}")
            self.label_status.setText("Ошибка перезапуска Sunshine")


if __name__ == "__main__":
    try:
        app = QApplication([])
        login_window = LoginWindow()
        login_window.show()
        log_info("Программа PlayTime запущена.")
        app.exec_()
    except Exception as e:
        log_error(f"Ошибка запуска приложения: {e}")
