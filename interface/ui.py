# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_From(object):
    def setupUi(self, From):
        From.setObjectName("From")
        From.resize(1000, 900)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 16, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 16, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 16, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 16, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        From.setPalette(palette)
        From.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DicomImageView = QtWidgets.QLabel(From)
        self.DicomImageView.setGeometry(QtCore.QRect(95, 200, 781, 500))
        self.DicomImageView.setText("")
        self.DicomImageView.setScaledContents(True)
        self.DicomImageView.setObjectName("DicomImageView")
        self.nextButton = QtWidgets.QPushButton(From)
        self.nextButton.setGeometry(QtCore.QRect(900, 550, 71, 41))
        self.nextButton.setObjectName("nextButton")
        self.prevButton = QtWidgets.QPushButton(From)
        self.prevButton.setGeometry(QtCore.QRect(900, 600, 71, 41))
        self.prevButton.setObjectName("prevButton")
        self.openFButton = QtWidgets.QPushButton(From)
        self.openFButton.setGeometry(QtCore.QRect(900, 650, 71, 41))
        self.openFButton.setObjectName("openFButton")
        self.horizontalScrollBar = QtWidgets.QScrollBar(From)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(110, 700, 791, 20))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.nextButton_2 = QtWidgets.QPushButton(From)
        self.nextButton_2.setGeometry(QtCore.QRect(900, 500, 71, 41))
        self.nextButton_2.setText("")
        self.nextButton_2.setObjectName("nextButton_2")
        self.nextButton_3 = QtWidgets.QPushButton(From)
        self.nextButton_3.setGeometry(QtCore.QRect(900, 450, 71, 41))
        self.nextButton_3.setText("")
        self.nextButton_3.setObjectName("nextButton_3")
        self.nextButton_4 = QtWidgets.QPushButton(From)
        self.nextButton_4.setGeometry(QtCore.QRect(900, 400, 71, 41))
        self.nextButton_4.setText("")
        self.nextButton_4.setObjectName("nextButton_4")
        self.nextButton_5 = QtWidgets.QPushButton(From)
        self.nextButton_5.setGeometry(QtCore.QRect(900, 350, 71, 41))
        self.nextButton_5.setText("")
        self.nextButton_5.setObjectName("nextButton_5")
        self.constrastButton = QtWidgets.QPushButton(From)
        self.constrastButton.setGeometry(QtCore.QRect(900, 300, 71, 41))
        self.constrastButton.setObjectName("constrastButton")
        self.zoom_outButton = QtWidgets.QPushButton(From)
        self.zoom_outButton.setGeometry(QtCore.QRect(900, 250, 71, 41))
        self.zoom_outButton.setObjectName("zoom_outButton")
        self.zoom_inButton = QtWidgets.QPushButton(From)
        self.zoom_inButton.setGeometry(QtCore.QRect(900, 200, 71, 41))
        self.zoom_inButton.setObjectName("zoom_inButton")
        self.index_label = QtWidgets.QLabel(From)
        self.index_label.setGeometry(QtCore.QRect(910, 700, 47, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.index_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.index_label.setFont(font)
        self.index_label.setText("")
        self.index_label.setObjectName("index_label")
        self.GButton = QtWidgets.QPushButton(From)
        self.GButton.setGeometry(QtCore.QRect(30, 60, 100, 100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(1, 16, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 16, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 16, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.GButton.setPalette(palette)
        self.GButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/ibrah/OneDrive/masaüstü/Proje/Yeni klasör/A1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GButton.setIcon(icon)
        self.GButton.setIconSize(QtCore.QSize(120, 120))
        self.GButton.setCheckable(False)
        self.GButton.setObjectName("GButton")
        self.GButton2 = QtWidgets.QPushButton(From)
        self.GButton2.setGeometry(QtCore.QRect(170, 60, 100, 100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(1, 16, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 16, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 16, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.GButton2.setPalette(palette)
        self.GButton2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.GButton2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/ibrah/OneDrive/masaüstü/Proje/Yeni klasör/A2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GButton2.setIcon(icon1)
        self.GButton2.setIconSize(QtCore.QSize(120, 120))
        self.GButton2.setObjectName("GButton2")
        self.GButton3 = QtWidgets.QPushButton(From)
        self.GButton3.setGeometry(QtCore.QRect(310, 60, 100, 100))
        self.GButton3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/ibrah/OneDrive/masaüstü/Proje/Yeni klasör/A3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GButton3.setIcon(icon2)
        self.GButton3.setIconSize(QtCore.QSize(120, 120))
        self.GButton3.setObjectName("GButton3")
        self.GButton4 = QtWidgets.QPushButton(From)
        self.GButton4.setGeometry(QtCore.QRect(450, 60, 100, 100))
        self.GButton4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/ibrah/OneDrive/masaüstü/Proje/Yeni klasör/A4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GButton4.setIcon(icon3)
        self.GButton4.setIconSize(QtCore.QSize(120, 120))
        self.GButton4.setObjectName("GButton4")
        self.GButton5 = QtWidgets.QPushButton(From)
        self.GButton5.setGeometry(QtCore.QRect(590, 60, 100, 100))
        self.GButton5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/ibrah/OneDrive/masaüstü/Proje/Yeni klasör/A5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GButton5.setIcon(icon4)
        self.GButton5.setIconSize(QtCore.QSize(120, 120))
        self.GButton5.setObjectName("GButton5")
        self.GButton6 = QtWidgets.QPushButton(From)
        self.GButton6.setGeometry(QtCore.QRect(730, 60, 100, 100))
        self.GButton6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Users/ibrah/OneDrive/masaüstü/Proje/Yeni klasör/A6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GButton6.setIcon(icon5)
        self.GButton6.setIconSize(QtCore.QSize(120, 120))
        self.GButton6.setObjectName("GButton6")
        self.GButton7 = QtWidgets.QPushButton(From)
        self.GButton7.setGeometry(QtCore.QRect(870, 60, 100, 100))
        self.GButton7.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("photos/A7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GButton7.setIcon(icon6)
        self.GButton7.setIconSize(QtCore.QSize(120, 120))
        self.GButton7.setObjectName("GButton7")
        self.nextButton_6 = QtWidgets.QPushButton(From)
        self.nextButton_6.setGeometry(QtCore.QRect(230, 820, 71, 41))
        self.nextButton_6.setText("")
        self.nextButton_6.setObjectName("nextButton_6")
        self.nextButton_7 = QtWidgets.QPushButton(From)
        self.nextButton_7.setGeometry(QtCore.QRect(30, 820, 71, 41))
        self.nextButton_7.setText("")
        self.nextButton_7.setObjectName("nextButton_7")
        self.nextButton_8 = QtWidgets.QPushButton(From)
        self.nextButton_8.setGeometry(QtCore.QRect(130, 820, 71, 41))
        self.nextButton_8.setText("")
        self.nextButton_8.setObjectName("nextButton_8")

        self.retranslateUi(From)
        QtCore.QMetaObject.connectSlotsByName(From)

    def retranslateUi(self, From):
        _translate = QtCore.QCoreApplication.translate
        From.setWindowTitle(_translate("From", "AiCancerDetection"))
        self.nextButton.setText(_translate("From", "Next"))
        self.prevButton.setText(_translate("From", "Prev"))
        self.openFButton.setText(_translate("From", "Open Folder"))
        self.constrastButton.setText(_translate("From", "Contrast"))
        self.zoom_outButton.setText(_translate("From", "Zoom out"))
        self.zoom_inButton.setText(_translate("From", "Zoom in"))
import test_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    From = QtWidgets.QWidget()
    ui = Ui_From()
    ui.setupUi(From)
    From.show()
    sys.exit(app.exec_())
