

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 587)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listbox = QtWidgets.QListWidget(self.centralwidget)
        self.listbox.setGeometry(QtCore.QRect(10, 110, 251, 401))
        self.listbox.setObjectName("listbox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 150, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.test = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.insert())
        self.test.setGeometry(QtCore.QRect(290, 420, 311, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 133, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 133, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 133, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        self.test.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.test.setFont(font)
        self.test.setObjectName("test")
        self.alert_rmc = QtWidgets.QLineEdit(self.centralwidget)
        self.alert_rmc.setGeometry(QtCore.QRect(20, 30, 481, 22))
        self.alert_rmc.setObjectName("alert_rmc")
        self.equal = QtWidgets.QLineEdit(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(380, 170, 131, 22))
        self.equal.setObjectName("equal")
        self.checksum = QtWidgets.QLabel(self.centralwidget)
        self.checksum.setGeometry(QtCore.QRect(320, 340, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.checksum.setFont(font)
        self.checksum.setText("")
        self.checksum.setObjectName("checksum")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 230, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.longitude = QtWidgets.QLineEdit(self.centralwidget)
        self.longitude.setGeometry(QtCore.QRect(370, 220, 141, 22))
        self.longitude.setObjectName("longitude")
        self.latitude = QtWidgets.QLineEdit(self.centralwidget)
        self.latitude.setGeometry(QtCore.QRect(370, 260, 141, 22))
        self.latitude.setObjectName("latitude")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SOG ="))
        self.label_2.setText(_translate("MainWindow", "Knots"))
        self.test.setText(_translate("MainWindow", "test"))
        self.label_3.setText(_translate("MainWindow", "POS = "))

    def check(self):
        string = self.alert_rmc.text()
        if "*" not in string:
            self.longitude.setText("dont enough information")
            self.latitude.setText("dont enough information")
            self.equal.setText("dont enough information")
            self.checksum.setText("error checksum")
        else:
            text, checksum = string.split("*")
            d = 0
            for c in text[1:].encode():
                d ^= c
            d = int(hex(d), 16)
            checksum = int(checksum, 16)
            if d == checksum:
                return True
            return False

        # print(int(hex(d),16), checksum)

    def insert(self):
        text = self.alert_rmc.text().split(",")
        for i in text:
            self.listbox.addItem(i)
        if self.check():
            for i in range(len(text)):
                if text[i] == "N" or text[i] == "S":
                    self.longitude.setText(text[i - 1] + text[i])
                if text[i] == "W" or text[i] == "E":
                    self.latitude.setText(text[i - 1] + text[i])
                    if "." in text[i + 1]:
                        self.equal.setText(text[i + 1])
                    else:
                        self.equal.setText("dont enough information")
                        break
            self.checksum.setText("checksum is good")
        else:
            self.checksum.setText("error checksum")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
