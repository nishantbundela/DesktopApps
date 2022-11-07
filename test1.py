from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
            super(MyWindow, self).__init__()
            self.setGeometry(200, 200, 600, 600)
            self.setWindowTitle("Experimental App")
            self.initUI()
    
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Testing labels")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click Me")
        self.b1.clicked.connect(self.clicked1)

    def clicked1(self):
        self.label.setText("Button1 Pressed hhhhhhhhhhhh")
        self.update()

    def update(self):
        self.label.adjustSize()



def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()