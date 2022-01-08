from PyQt5 import QtCore, QtGui, QtWidgets
import random
import pyperclip
import imgs.source


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 300)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0.716, stop:0 rgba(134, 255, 165, 255), stop:1 rgba(184, 164, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setFamily(".SF NS Mono")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(55, 40, 190, 20))
        self.label.setObjectName("label")
        self.label.setText("Generate me my password!")
        self.label.setFont(font)
        self.label.setStyleSheet("background: transparent;")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 230, 300, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("background-color: white;")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 110, 101, 20))
        self.label_3.setText('amount of numbers')
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("background: transparent; font-size:10px;")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 260, 45, 20))
        self.label_4.setText('')
        self.label_4.setStyleSheet("background: transparent;")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 140, 100, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Generate")
        self.pushButton.setStyleSheet("background-color: white; border-radius:15px;")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 255, 100, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("Copy")
        self.pushButton_2.setStyleSheet("background-color: white; border-radius:15px;")

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(100, 80, 48, 24))
        self.spinBox.setMinimum(10)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setStyleSheet("background-color: white;")
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(150, 80, 51, 51))
        self.frame.setStyleSheet("border-image: url(:/imgs/arrowpng.png); background:transparent;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("passgenerator")
        
        self.pushButton.clicked.connect(self.generate)
        self.pushButton_2.clicked.connect(self.copy)
        

    def generate(self):
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'
        symbols = '[]{}()*;/,_-'

        all = lower + upper + numbers + symbols
        length = self.spinBox.value()
        password = "".join(random.sample(all, length))
        self.label_2.setText(password)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.label_4.setText('')

    def copy(self):
        pyperclip.copy(self.label_2.text())
        self.label_4.setText('copied!')
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
