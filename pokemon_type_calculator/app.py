import sys

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDial,
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
        global attack_type_combo_box
        global defense_type_one_combo_box
        global defense_type_two_combo_box
        global calculation_label
        super().__init__()
        super(MainWindow, self).__init__()

        self.setWindowTitle("Pokemon type effectiveness calculator")

        layout1 = QVBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        layout4 = QHBoxLayout()
        layout5 = QHBoxLayout()

        layout_app = QVBoxLayout()
        layout1.addWidget(QLabel('what is the typing of the attack'))
        attack_type_combo_box = QComboBox()
        attack_type_combo_box.addItems(["Normal", "Fire", "Water", "Grass", "Flying", "Fighting", "Poison", "Electric", 
                                        "Ground", "Rock", "Psychic", "Ice", "Bug", "Ghost", "Steel", "Dragon", "Dark", "Fairy"])
        layout1.addWidget(attack_type_combo_box)
        layout1.addStretch()

        layout2.addWidget(QLabel('what is the first or only type of the defending pokemon'))
        defense_type_one_combo_box = QComboBox()
        defense_type_one_combo_box.addItems(["Normal", "Fire", "Water", "Grass", "Flying", "Fighting", "Poison", "Electric", 
                                        "Ground", "Rock", "Psychic", "Ice", "Bug", "Ghost", "Steel", "Dragon", "Dark", "Fairy"])
        layout2.addWidget(defense_type_one_combo_box)
        layout2.addStretch()

        layout3.addWidget(QLabel('what is the second type of the defending pokemon'))
        defense_type_two_combo_box = QComboBox()
        defense_type_two_combo_box.addItems(["Normal", "Fire", "Water", "Grass", "Flying", "Fighting", "Poison", "Electric", 
                                        "Ground", "Rock", "Psychic", "Ice", "Bug", "Ghost", "Steel", "Dragon", "Dark", "Fairy", "None"])
        layout3.addWidget(defense_type_two_combo_box)
        layout3.addStretch()

        
        layout4.addLayout(layout1)
        layout4.addSpacing(50)
        layout4.addLayout(layout2)
        layout4.addSpacing(50)
        layout4.addLayout(layout3)
        
        calculate_button = QPushButton(text = "Calculate")
        calculate_button.setFixedSize(75,30)
        calculate_button.setCheckable(True)
        calculate_button.clicked.connect(self.button_was_pressed)
        layout5.addWidget(calculate_button)

        layout_app.addLayout(layout4)
        layout_app.addLayout(layout5)
        widget = QWidget()
        widget.setLayout(layout_app)
        self.setCentralWidget(widget)

    def button_was_pressed(self):
        self.attack_type = attack_type_combo_box.currentText()
        self.defense_type_one = defense_type_one_combo_box.currentText()
        self.defense_type_two = defense_type_two_combo_box.currentText()
        
        attack_type = self.attack_type
        defense_type_one = self.defense_type_one
        defense_type_two = self.defense_type_two
        pokemon_types = [
            








            
        ]


        if defense_type_two == "None": 
            defense_type_two = ""
        elif defense_type_one != defense_type_two:
            defense_type_two = "and " + defense_type_two + " "
        elif defense_type_one == defense_type_two:
            defense_type_two = ""
        self.calculation_phrase = f"The {attack_type} move will deal 1x damage to the {defense_type_one} {defense_type_two}type pokemon"
        print(self.calculation_phrase)





app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()