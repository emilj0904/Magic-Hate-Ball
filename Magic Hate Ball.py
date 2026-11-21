import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, Qt

import random
import pygame


class EightBallApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1000, 350, 680, 790)

        self.response_generator = ResponseGenerator()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.display_responses)
        self.timer.setSingleShot(True)

        self.question_input = QLineEdit(self)
        self.ask_button = QPushButton("Ask...", self)
        self.response_label = QLabel(self)

        pygame.mixer.init()
        pygame.mixer.music.load("shaking_ball.mp3")

        self.initUI()


    def initUI(self):
        self.setWindowTitle("Magic Hate Ball")
        self.setWindowIcon(QIcon("icon.jpg"))

        vbox = QVBoxLayout()

        vbox.addWidget(self.question_input)
        vbox.addWidget(self.ask_button)
        vbox.addSpacing(40)
        vbox.addWidget(self.response_label)

        vbox.setContentsMargins(40, 40, 40, 40)

        self.setLayout(vbox)

        self.question_input.setAlignment(Qt.AlignCenter)
        self.response_label.setAlignment(Qt.AlignCenter)
        self.response_label.setWordWrap(True)

        self.setObjectName("main_window")
        self.question_input.setObjectName("question_input")
        self.ask_button.setObjectName("ask_button")
        self.response_label.setObjectName("response_label")

        self.setStyleSheet("""
            QWidget#main_window{
                background-color: #202021;
            }
            QLineEdit{
                font-family: Arial Narrow;
                font-size: 30px;
                color: white;
                border: 5px solid;
                border-color: #754ae0;
                background-color: #2a2a2b;
                padding: 15px 0px;
                border-radius: 5px;
            }
            QPushButton#ask_button{
                font-family: Arial;
                font-weight: bold;
                font-size: 30px;
                color: white;
                background-color: #653ad0;
                padding: 5px 0px;
                border-radius: 5px;
            }
            QLabel#response_label{
                font-family: Consolas;
                font-size: 40px;
                color: white;
                background-color: #0C0EB6;
                border: 100px solid;
                border-color: #111111;
                padding: 4px;
            }""")

        self.question_input.setPlaceholderText("Enter your yes-or-no question...")
        self.ask_button.setFocus()
        
        self.ask_button.clicked.connect(self.on_button_click)


    def on_button_click(self):
        if self.question_input.text():
            self.ask_button.setEnabled(False)
            self.response_label.setText("Shaking...")
            pygame.mixer.music.play()
            self.timer.start(2500)
        
        else:
            self.response_label.setText("You need to ask me a question first!")


    def display_responses(self):
            self.response_label.setText(self.response_generator.choose_question())
            self.question_input.setText("")
            self.ask_button.setEnabled(True)



class ResponseGenerator:
    def __init__(self):
        self.responses = (
            "SUCK MY DICK",
            "FUCK YOU",
            "CHOKE ON THE THICKEST PART OF MY DICK",
            "WRITE YOUR QUESTION ON A PIECE OF PAPER AND STICK IT UP YOUR ASS",
            "KILL YOURSELF",
            "EAT MY ASS INSTEAD",
            "STOP WASTING MY FUCKING TIME",
            "GO FUCK YOURSELF",
            "FUCK OFF",
            "SHUT THE FUCK UP",
            "NO ONE LIKES YOU",
            "I HOPE YOU DIE ALONE",
            "YOU ARE A WASTE OF LIFE",
            "YOU ARE A DEGENERATE",
            "I WILL PISS ON YOUR GRAVE")

    def choose_question(self):
        return random.choice(self.responses)


def main():
    app = QApplication(sys.argv)
    window = EightBallApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()