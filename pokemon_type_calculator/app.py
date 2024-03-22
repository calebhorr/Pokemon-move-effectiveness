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
    QHBoxLayout,
    QWidget,
)
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        super(MainWindow, self).__init__()

        self.setWindowTitle("Pokemon type effectiveness calculator")

        layout1 = QVBoxLayout()
        layout1.setSpacing(5)
        layout2 = QVBoxLayout()
        layout2.setSpacing(5)
        layout3 = QVBoxLayout()
        layout3.setSpacing(5)
        layout4 = QHBoxLayout()
        layout4.setSpacing(100)
        layout1.addWidget(QLabel('what is the typing of the attack'))
        attack_type_combo_box = QComboBox()
        attack_type_combo_box.addItems(["Normal", "Fire", "Water", "Grass", "Flying", "Fighting", "Poison", "Electric", 
                                        "Ground", "Rock", "Psychic", "Ice", "Bug", "Ghost", "Steel", "Dragon", "Dark", "Fairy"])
        layout1.addWidget(attack_type_combo_box)
        layout2.addWidget(QLabel('what is the first or only type of the defending pokemon'))
        defense_type_one_combo_box = QComboBox()
        defense_type_one_combo_box.addItems(["Normal", "Fire", "Water", "Grass", "Flying", "Fighting", "Poison", "Electric", 
                                        "Ground", "Rock", "Psychic", "Ice", "Bug", "Ghost", "Steel", "Dragon", "Dark", "Fairy"])
        layout2.addWidget(defense_type_one_combo_box)
        layout3.addWidget(QLabel('what is the second type of the defending pokemon'))
        defense_type_two_combo_box = QComboBox()
        defense_type_two_combo_box.addItems(["Normal", "Fire", "Water", "Grass", "Flying", "Fighting", "Poison", "Electric", 
                                        "Ground", "Rock", "Psychic", "Ice", "Bug", "Ghost", "Steel", "Dragon", "Dark", "Fairy"])
        layout3.addWidget(defense_type_two_combo_box)

        layout4.addLayout(layout1)
        layout4.addLayout(layout2)
        layout4.addLayout(layout3)
        widget = QWidget()
        widget.setLayout(layout4)
        self.setCentralWidget(widget)



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()