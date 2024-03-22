import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        super(MainWindow, self).__init__()

        self.setWindowTitle("Pokemon type effectiveness calculator")

        layout1 = QVBoxLayout()

        layout1.addWidget(QLabel('what is the typing of the attack'))
        attack_type_combo_box = QComboBox()
        attack_type_combo_box.addItems(["Normal", "Fire", "Water", "Grass", "Flying", "Fighting", "Poison", "Electric", 
                                        "Ground", "Rock", "Psychic", "Ice", "Bug", "Ghost", "Steel", "Dragon", "Dark", "Fairy"])
        layout1.addWidget(attack_type_combo_box)
        layout1.addWidget(QLabel('what is the first or only type of the defending pokemon'))
        defense_type_one_combo_box = QComboBox()
        defense_type_one_combo_box.addItems(["Normal", "Fire", "Water", "Grass", "Flying", "Fighting", "Poison", "Electric", 
                                        "Ground", "Rock", "Psychic", "Ice", "Bug", "Ghost", "Steel", "Dragon", "Dark", "Fairy"])
        layout1.addWidget(QComboBox())
        layout1.addWidget(QLabel('what is the second type of the defending pokemon'))
        defense_type_two_combo_box = QComboBox()
        defense_type_two_combo_box.addItems(["Normal", "Fire", "Water", "Grass", "Flying", "Fighting", "Poison", "Electric", 
                                        "Ground", "Rock", "Psychic", "Ice", "Bug", "Ghost", "Steel", "Dragon", "Dark", "Fairy"])
        layout1.addWidget(QComboBox())

        layout = QVBoxLayout()
        widgets = [
            QComboBox,
            QComboBox,
            QComboBox,
            QLabel,
        ]
        for w in widgets:
            layout.addWidget(w())   
        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()