from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QCheckBox, QPushButton, QMessageBox
from utils.api_handler import get_sunshine_apps
import json

class GameManagementWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Управление играми")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        # Таблица для отображения игр
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Игра", "Разрешено"])
        self.layout.addWidget(self.table)

        # Кнопки
        self.update_button = QPushButton("Обновить список")
        self.update_button.clicked.connect(self.load_games)
        self.layout.addWidget(self.update_button)

        self.save_button = QPushButton("Сохранить настройки")
        self.save_button.clicked.connect(self.save_settings)
        self.layout.addWidget(self.save_button)

        self.setLayout(self.layout)
        self.load_games()

    def load_games(self):
        games = get_sunshine_apps()
        if "error" in games:
            QMessageBox.critical(self, "Ошибка", f"Ошибка загрузки: {games['error']}")
            return

        self.table.setRowCount(0)
        for game in games.get("apps", []):
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(game["name"]))
            checkbox = QCheckBox()
            checkbox.setChecked(True)
            self.table.setCellWidget(row, 1, checkbox)

    def save_settings(self):
        games = []
        for row in range(self.table.rowCount()):
            name = self.table.item(row, 0).text()
            allowed = self.table.cellWidget(row, 1).isChecked()
            games.append({"name": name, "allowed": allowed})

        with open("game_settings.json", "w", encoding="utf-8") as file:
            json.dump(games, file, ensure_ascii=False, indent=4)
        print("Настройки сохранены!")
