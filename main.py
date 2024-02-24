from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import uic


class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("image_test.ui", self)  # image_test.ui is the file from QT Designer
        self.pushButton.clicked.connect(self.addimage)
        self.show()

    def addimage(self):
        qpixmap=QPixmap('pat1.bmp')
        self.label.setPixmap(qpixmap)

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ ==  '__main__':
    main()
