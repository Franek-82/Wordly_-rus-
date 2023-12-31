from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QTextEdit, QPushButton, QLabel,
                             QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt5.QtGui import QFont, QTextCharFormat
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from Wordly.word2 import func
import sys, random


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        with open("C:/Python/russian_nouns.txt", "r", encoding="utf-8") as file:
            self.lines = tuple(map(lambda x: x.rstrip(), file.readlines()))
            self.lines = tuple(filter(lambda x: len(x) < 7, self.lines))
            self.word_x = random.choice(self.lines)
            print(self.word_x)  # "газета"
        font = QFont('Courier', 23)
        self.setFont(font)
        self.le = len(self.word_x)
        self.line = QLineEdit()
        self.q_text = QTextEdit()
        self.q_text.setReadOnly(True)
        self.q_text.setStyleSheet("letter-spacing: 50px; font-size: 32px; padding-left: 15px")
        self.q_text.setLineWrapMode(QTextEdit.NoWrap)  # без переноса на след. строку
        self.q_text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.butt = QPushButton("Вы угадали слово")
        self.butt.setVisible(False)
        self.width = self.le * 65  # Изменяем ширину в зависимости от количества букв
        self.q_text.setFixedWidth(self.width)
        self.line.setFixedWidth(self.width)
        self.line.setMaxLength(self.le)
        self.line.returnPressed.connect(self.match)
        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.grid = QGridLayout()
        self.list_lbl = []
        for i in range(self.le):
            self.label = QLabel()
            self.label.setFixedSize(60, 60)
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setStyleSheet(
                "border: 1px solid black; font-size: 32px;")
            self.hbox.addWidget(self.label, alignment=QtCore.Qt.AlignTop)
            self.list_lbl.append(self.label)
        self.vbox.addWidget(self.q_text, alignment=QtCore.Qt.AlignHCenter)
        self.vbox.addWidget(self.line, alignment=QtCore.Qt.AlignHCenter)
        self.vbox.addWidget(self.butt, alignment=QtCore.Qt.AlignBottom)
        self.grid.addLayout(self.hbox, 0,
                            0)  # Устанавливаем конт. QHBoxLayout() в 1й столбец и 1ю строку QGridLayout()
        self.grid.addLayout(self.vbox, 1,
                            0)  # Устанавливаем конт. QVBoxLayout() во 2й столбец и 1ю строку QGridLayout()
        self.setLayout(self.grid)
        self.line.setFocus()

    def match(self):
        self.word = self.line.text()
        if len(self.word) < self.le:
            print(f"Слово должно состоять из {self.le} букв.")
            self.line.clear()
            return
        elif self.word == self.word_x:
            self.butt.setVisible(True)
            self.line.setVisible(False)
            for i in range(self.le):
                self.list_lbl[i].setText(self.word_x[i])
            self.butt.clicked.connect(app.exit)
        elif self.word not in self.lines:
            self.line.clear()
            print("Нет такого слова ")
        else:
            # два словаря с совпадающими символами
            self.red, self.blue = func(self.word_x, self.word)
            self.line.clear()
            self.q_text.setVisible(True)
            self.update_word_x()

    def update_word_x(self):
        format = QTextCharFormat()
        cursor = self.q_text.textCursor()
        self.q_text.append("")
        cursor.beginEditBlock()
        for i, char in enumerate(self.word):
            if i in self.red.keys():
                color = Qt.red
                format.setForeground(color)
                cursor.mergeCharFormat(format)
                cursor.insertText(char)
                # print(self.list_lbl[i])
                self.list_lbl[i].setText(char)
            elif i in self.blue.keys():
                color = Qt.blue
                format.setForeground(color)
                cursor.mergeCharFormat(format)
                cursor.insertText(char)
            else:
                format.setForeground(Qt.black)
                cursor.mergeCharFormat(format)
                cursor.insertText(char)
        cursor.endEditBlock()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.setWindowTitle("Игра")
    window.resize(350, 180)
    window.setMinimumHeight(400)
    window.show()
    sys.exit(app.exec())
