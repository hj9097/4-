from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from keypad2 import numPadList, operatorList, constantList, functionList
import calcFunctions

class Button(QToolButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Digit Buttons
        self.digitButton = [x for x in range(0, 10)]

        for i in range(0, 10):
            self.digitButton[i] = Button(str(i), self.buttonClicked)

        # . and = ButtonsAttributeError: 'NoneType' object has no attribute 'text'
        self.decButton = Button('.', self.buttonClicked)
        self.eqButton = Button('=', self.buttonClicked)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()

        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)

        numLayout = QGridLayout()

        for i in range(0, 10):
            if i == 0:
                numLayout.addWidget(self.digitButton[i], 3, 0)
            numLayout.addWidget(self.digitButton[i], int((9 - i) / 3), int((i - 1) % 3))

        buttonGroups = {
            'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 1},
            'functions': {'buttons': functionList, 'layout': funcLayout, 'columns': 1},
        }

        for label in buttonGroups.keys():
            r = 0;
            c = 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0;
                    r += 1

        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        mainLayout.addLayout(numLayout, 1, 0)

        mainLayout.addLayout(opLayout, 1, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

    def buttonClicked(self):

        if self.display.text() == 'Error!':
            self.display.setText('')

        button = self.sender()
        key = button.text()

        if key == '=':
            
            try:
                result = str(eval(self.display.text()))
                
            except:
                result = 'Error!'
                
            self.display.setText(result)

        elif key == 'C':
            self.display.clear()


        elif key in constantList:

            try:
                consList = ['3.141592', '3E+8', '340', '1.5E+8']

                for idx in range(0, 4):

                    if key in constantList[idx]:

                        self.display.setText(self.display.text() + consList[idx])
                        
            except:
                "Error"

                
        elif key in functionList:

            try:

                n = str(eval(self.display.text()))

                calcList = [calcFunctions.factorial(n),

                            calcFunctions.decToBin(n),

                            calcFunctions.binToDec(n),

                            calcFunctions.decToRoman(n)]

                for idx in range(4):

                    if key in functionList[idx]:

                        self.display.setText(calcList[idx])
            except:
                "Error"

        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
