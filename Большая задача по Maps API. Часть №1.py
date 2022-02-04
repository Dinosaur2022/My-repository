from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtGui import QPixmap
import requests
from PIL import Image
from io import BytesIO


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CreateMap = QtWidgets.QPushButton(self.centralwidget)
        self.CreateMap.setGeometry(QtCore.QRect(50, 140, 591, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CreateMap.setFont(font)
        self.CreateMap.setObjectName("CreateMap")
        self.MapLab = QtWidgets.QLabel(self.centralwidget)
        self.MapLab.setGeometry(QtCore.QRect(50, 220, 591, 371))
        self.MapLab.setText("")
        self.MapLab.setObjectName("MapLab")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(520, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.TextX = QtWidgets.QLineEdit(self.centralwidget)
        self.TextX.setGeometry(QtCore.QRect(50, 30, 121, 31))
        self.TextX.setObjectName("TextX")
        self.TextY = QtWidgets.QLineEdit(self.centralwidget)
        self.TextY.setGeometry(QtCore.QRect(270, 30, 121, 31))
        self.TextY.setObjectName("TextY")
        self.TextScale = QtWidgets.QLineEdit(self.centralwidget)
        self.TextScale.setGeometry(QtCore.QRect(520, 30, 121, 31))
        self.TextScale.setObjectName("TextScale")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Map Search"))
        self.CreateMap.setText(_translate("MainWindow", "Create a map"))
        self.label.setText(_translate("MainWindow", "Position de x"))
        self.label_3.setText(_translate("MainWindow", "Position de y"))
        self.label_2.setText(_translate("MainWindow", "Scale"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 700)
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.CreateMap.clicked.connect(self.push)
        self.TextX.setText('0')
        self.TextY.setText('0')
        self.TextScale.setText('1')

        x = 0
        y = 0
        scale = 1

        url = lambda x, y, scale: f'http://static-maps.yandex.ru/1.x/?ll={x},{y}&spn={scale},{scale}&l=map'
        response = requests.get(url(x, y, scale))

        Image.open(BytesIO(response.content)).resize((591, 371)).save('map.png')
        pixmap = QPixmap('map.png')
        self.MapLab.setPixmap(pixmap)


    def push(self):
        try:
            x = float(self.TextX.text()) % 360
            y = float(self.TextY.text()) % 90
            scale = float(self.TextScale.text())
            if scale > 90:
                scale = 90
        except Exception as e:
            print(e)
            x = 0
            y = 0
            scale = 1
            self.TextX.setText(str(x))
            self.TextY.setText(str(y))
            self.TextScale.setText(str(scale))

        url = lambda x, y, scale: f'http://static-maps.yandex.ru/1.x/?ll={x},{y}&spn={scale},{scale}&l=map'
        response = requests.get(url(x, y, scale))

        Image.open(BytesIO(response.content)).resize((591, 371)).save('map.png')
        pixmap = QPixmap('map.png')
        self.MapLab.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
