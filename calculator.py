from PyQt5 import QtWidgets
from ui_calculator import Ui_MainWindow


class CalculatorWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    num = 0
    stillTyping = False # Used to tell if the user is typing more than a single digit in a calculation

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        #  Connect digit buttons to slots
        self.pushButton_Zero.clicked.connect(self.digit_pressed)
        self.pushButton_1.clicked.connect(self.digit_pressed)
        self.pushButton_2.clicked.connect(self.digit_pressed)
        self.pushButton_3.clicked.connect(self.digit_pressed)
        self.pushButton_4.clicked.connect(self.digit_pressed)
        self.pushButton_5.clicked.connect(self.digit_pressed)
        self.pushButton_6.clicked.connect(self.digit_pressed)
        self.pushButton_7.clicked.connect(self.digit_pressed)
        self.pushButton_8.clicked.connect(self.digit_pressed)
        self.pushButton_9.clicked.connect(self.digit_pressed)

        self.pushButton_dec.clicked.connect(self.decimal_pressed)

        self.pushButton_negative.clicked.connect(self.unary_operation_pressed)
        self.pushButton_mod.clicked.connect(self.unary_operation_pressed)

        self.pushButton_plus.clicked.connect(self.binary_operation_pressed)
        self.pushButton_div.clicked.connect(self.binary_operation_pressed)
        self.pushButton_minus.clicked.connect(self.binary_operation_pressed)
        self.pushButton_mult.clicked.connect(self.binary_operation_pressed)

        self.pushButton_equal.clicked.connect(self.equals_pressed)

        self.pushButton_Clear.clicked.connect(self.clear_pressed)

        self.pushButton_plus.setCheckable(True)
        self.pushButton_div.setCheckable(True)
        self.pushButton_minus.setCheckable(True)
        self.pushButton_mult.setCheckable(True)

    def digit_pressed(self):
        button = self.sender()

        if ((self.pushButton_plus.isChecked() or self.pushButton_minus.isChecked() or
                self.pushButton_div.isChecked() or self.pushButton_mult.isChecked()) and (not self.stillTyping)):
            newLabel = format(float(button.text()), '.15g')
            self.stillTyping = True
        else:
            if ('.' in self.label.text()) and (button.text() == "0"):
                newLabel = format(float(self.label.text() + button.text()), '.15')
            else:
                newLabel = format(float(self.label.text() + button.text()), '.15g')
        self.label.setText(newLabel)

    def decimal_pressed(self):
        self.label.setText(self.label.text() + '.')

    def unary_operation_pressed(self):
        button = self.sender()

        labelNumber = float(self.label.text())

        if button.text() == "+/-":
            labelNumber = labelNumber * -1
        else: # button text == '%'
            labelNumber = labelNumber * 0.01

        newLabel = format(labelNumber, '.15g')
        self.label.setText(newLabel)

    def binary_operation_pressed(self):
        button = self.sender()

        button.setChecked(True)

        self.num = float(self.label.text())

    def equals_pressed(self):

        newNum = float(self.label.text())

        if self.pushButton_plus.isChecked():
            labelNumber = self.num + newNum
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_plus.setChecked(False)
        elif self.pushButton_div.isChecked():
            labelNumber = self.num / newNum
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_div.setChecked(False)
        elif self.pushButton_minus.isChecked():
            labelNumber = self.num - newNum
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_minus.setChecked(False)
        elif self.pushButton_mult.isChecked():
            labelNumber = self.num * newNum
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_mult.setChecked(False)

        self.stillTyping = False

    def clear_pressed(self):
        self.pushButton_mult.setChecked(False)
        self.pushButton_div.setChecked(False)
        self.pushButton_minus.setChecked(False)
        self.pushButton_plus.setChecked(False)

        self.stillTyping = False

        self.label.setText('0')