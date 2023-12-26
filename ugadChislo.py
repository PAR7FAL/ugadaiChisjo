import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class NumberGuessingGame(QWidget):
    def __init__(self):
        super().__init__()

        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 5

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Привет! Я загадал число от 1 до 100. Попробуй угадать его за 5 попыток.")
        layout.addWidget(self.label)

        self.input_field = QLineEdit()
        layout.addWidget(self.input_field)

        self.submit_button = QPushButton("Попробовать угадать")
        self.submit_button.clicked.connect(self.check_guess)
        layout.addWidget(self.submit_button)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.setWindowTitle("Угадай число")

    def check_guess(self):
        self.attempts += 1
        guess = int(self.input_field.text())

        if guess < self.secret_number:
            self.result_label.setText("Загаданное число больше вашего предположения.")
        elif guess > self.secret_number:
            self.result_label.setText("Загаданное число меньше вашего предположения.")
        else:
            self.result_label.setText(f"Поздравляю! Вы угадали число {self.secret_number} за {self.attempts} попыток.")
            self.submit_button.setEnabled(False)

        if self.attempts == self.max_attempts and guess != self.secret_number:
            self.result_label.setText(f"Вы проиграли! Загаданное число было: {self.secret_number}.")
            self.submit_button.setEnabled(False)

def run_game():
    app = QApplication(sys.argv)
    game = NumberGuessingGame()
    game.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_game()