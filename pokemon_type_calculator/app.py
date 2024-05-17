import sys
import controller
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
        super().__init__()
        super(MainWindow, self).__init__()

        self.setWindowTitle('Pokemon type effectiveness calculator')

        layout1 = QVBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        layout4 = QHBoxLayout()
        layout5 = QHBoxLayout()
        layout6 = QHBoxLayout()
        layout7 = QHBoxLayout()
        layout8 = QVBoxLayout()
        layout_app = QVBoxLayout()
        layout1.addWidget(QLabel('what is the typing of the attack'))
        self.attack_type_combo_box = QComboBox()
        self.attack_type_combo_box.addItems(['Normal', 'Fire', 'Water', 'Grass', 'Flying', 'Fighting', 'Poison', 'Electric', 
                                        'Ground', 'Rock', 'Psychic', 'Ice', 'Bug', 'Ghost', 'Steel', 'Dragon', 'Dark', 'Fairy'])
        layout1.addWidget(self.attack_type_combo_box)
        layout1.addStretch()

        layout2.addWidget(QLabel('what is the first or only type of the defending pokemon'))
        self.defense_type_one_combo_box = QComboBox()
        self.defense_type_one_combo_box.addItems(['Normal', 'Fire', 'Water', 'Grass', 'Flying', 'Fighting', 'Poison', 'Electric', 
                                        'Ground', 'Rock', 'Psychic', 'Ice', 'Bug', 'Ghost', 'Steel', 'Dragon', 'Dark', 'Fairy'])
        layout2.addWidget(self.defense_type_one_combo_box)
        layout2.addStretch()

        layout3.addWidget(QLabel('what is the second type of the defending pokemon'))
        self.defense_type_two_combo_box = QComboBox()
        self.defense_type_two_combo_box.addItems(['Normal', 'Fire', 'Water', 'Grass', 'Flying', 'Fighting', 'Poison', 'Electric', 
                                        'Ground', 'Rock', 'Psychic', 'Ice', 'Bug', 'Ghost', 'Steel', 'Dragon', 'Dark', 'Fairy', 'None'])
        layout3.addWidget(self.defense_type_two_combo_box)
        layout3.addStretch()

        
        layout4.addLayout(layout1)
        layout4.addSpacing(50)
        layout4.addLayout(layout2)
        layout4.addSpacing(50)
        layout4.addLayout(layout3)
        
        #calculate button
        calculate_button = QPushButton(text = 'Calculate')
        calculate_button.setFixedSize(75,30)
        calculate_button.setCheckable(True)
        calculate_button.clicked.connect(self.button_was_pressed)
        layout5.addWidget(calculate_button)

        #damage text ex: that move: is super efective
        self.damage_text_label = QLabel('That move: ')
        layout6.addSpacing(275)
        layout6.addWidget(self.damage_text_label)

        self.damage_multiplier_label = QLabel('And will deal:')
        layout7.addSpacing(275)
        layout7.addWidget(self.damage_multiplier_label)

        layout8.addLayout(layout6)
        layout8.addLayout(layout7)



        app_title = QLabel(text='Pokemon move effectiveness Calculator')
        layout_app.addWidget(app_title)
        layout_app.addSpacing(50)
        layout_app.addLayout(layout4)
        layout_app.addSpacing(50)
        layout_app.addLayout(layout5)
        layout_app.addSpacing(50)
        layout_app.addLayout(layout8)


        widget = QWidget()
        widget.setLayout(layout_app)
        self.setCentralWidget(widget)

        self.pokemon_types = [
            'Normal',#0
            'Fire',#1
            'Water',#2
            'Elecrtic',#3
            'Grass',#4
            'Ice',#5
            'Fighting',#6
            'Poison',#7
            'Ground',#8
            'Flying',#9
            'Psychic',#10
            'Bug',#11
            'Rock',#12
            'Ghost',#13
            'Dragon',#14
            'Dark',#15
            'Steel',#16
            'Fairy',#17
            ]
    
    def button_was_pressed(self):
        attack_type = self.attack_type_combo_box.currentText()
        defense_type_one = self.defense_type_one_combo_box.currentText()
        defense_type_two = self.defense_type_two_combo_box.currentText()
        pokemon_types = self.pokemon_types

        if defense_type_two == 'None' or defense_type_one == defense_type_two:
            defense_type_two = ''
        damage_multiplier = controller.calculate(attack_type,defense_type_one,defense_type_two,pokemon_types)


        damage_text = ''
        if damage_multiplier == 0:
            damage_text = 'Has no effect'
        if damage_multiplier == 1:
            damage_text = 'is average'
        if damage_multiplier == 2:
            damage_text = 'is super effective!'
        if damage_multiplier == 4:
            damage_text = 'is super effective!!'
        if damage_multiplier == 0.5:
            damage_text = 'is not very effective!'
        if damage_multiplier == 0.25:
            damage_text = ' is not very effective!!'
        
        self.damage_text_label.setText('That move: ' + damage_text)
        self.damage_multiplier_label.setText('And will deal: ' + str(damage_multiplier) + 'x')



        if defense_type_one != defense_type_two and defense_type_two:
            defense_type_two = 'and ' + defense_type_two + ' '






app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()