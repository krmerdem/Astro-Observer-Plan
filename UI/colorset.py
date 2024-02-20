# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'colorset.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)
import icon_rc

class Ui_ColorSet(object):
    def setupUi(self, ColorSet):
        if not ColorSet.objectName():
            ColorSet.setObjectName(u"ColorSet")
        ColorSet.resize(578, 408)
        icon = QIcon()
        icon.addFile(u":/icon/icon/color-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        ColorSet.setWindowIcon(icon)
        ColorSet.setStyleSheet(u"QWidget {\n"
"background: #1c1c27;\n"
"border-radius: 10px solid #eeeeee;\n"
"}")
        self.gridLayout_2 = QGridLayout(ColorSet)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(ColorSet)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"color: #eeeeee;\n"
"}")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 30))
        self.label_7.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.simcolor_Button = QPushButton(self.groupBox)
        self.simcolor_Button.setObjectName(u"simcolor_Button")
        self.simcolor_Button.setMinimumSize(QSize(50, 30))
        self.simcolor_Button.setMaximumSize(QSize(50, 30))
        self.simcolor_Button.setStyleSheet(u"QPushButton{\n"
"border: 2px solid #eeeeee;\n"
"border-radius: 10px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.simcolor_Button, 1, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setFont(font)

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.tmasscolor_Button = QPushButton(self.groupBox)
        self.tmasscolor_Button.setObjectName(u"tmasscolor_Button")
        self.tmasscolor_Button.setMinimumSize(QSize(50, 30))
        self.tmasscolor_Button.setMaximumSize(QSize(50, 30))
        self.tmasscolor_Button.setStyleSheet(u"QPushButton{\n"
"border: 2px solid #eeeeee;\n"
"border-radius: 10px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.tmasscolor_Button, 2, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)

        self.gaiacolor_Button = QPushButton(self.groupBox)
        self.gaiacolor_Button.setObjectName(u"gaiacolor_Button")
        self.gaiacolor_Button.setMinimumSize(QSize(50, 30))
        self.gaiacolor_Button.setMaximumSize(QSize(50, 30))
        self.gaiacolor_Button.setStyleSheet(u"QPushButton{\n"
"border: 2px solid #eeeeee;\n"
"border-radius: 10px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.gaiacolor_Button, 3, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)

        self.maincolor_Button = QPushButton(self.groupBox)
        self.maincolor_Button.setObjectName(u"maincolor_Button")
        self.maincolor_Button.setMinimumSize(QSize(50, 30))
        self.maincolor_Button.setMaximumSize(QSize(50, 30))
        self.maincolor_Button.setStyleSheet(u"QPushButton{\n"
"border: 2px solid #eeeeee;\n"
"border-radius: 10px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.maincolor_Button, 4, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.compcolor_Button = QPushButton(self.groupBox)
        self.compcolor_Button.setObjectName(u"compcolor_Button")
        self.compcolor_Button.setMinimumSize(QSize(50, 30))
        self.compcolor_Button.setMaximumSize(QSize(50, 30))
        self.compcolor_Button.setStyleSheet(u"QPushButton{\n"
"border: 2px solid #eeeeee;\n"
"border-radius: 10px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.compcolor_Button, 5, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 30))
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.checkcolor_Button = QPushButton(self.groupBox)
        self.checkcolor_Button.setObjectName(u"checkcolor_Button")
        self.checkcolor_Button.setMinimumSize(QSize(50, 30))
        self.checkcolor_Button.setMaximumSize(QSize(50, 30))
        self.checkcolor_Button.setStyleSheet(u"QPushButton{\n"
"border: 2px solid #eeeeee;\n"
"border-radius: 10px;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.checkcolor_Button, 6, 1, 1, 1)

        self.confirmBtn = QPushButton(self.groupBox)
        self.confirmBtn.setObjectName(u"confirmBtn")
        self.confirmBtn.setMinimumSize(QSize(0, 30))
        self.confirmBtn.setMaximumSize(QSize(16777215, 30))
        self.confirmBtn.setStyleSheet(u"QPushButton{\n"
"background-color:  #6316AC;\n"
"border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #765cde;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #7e31b5;\n"
"}")

        self.gridLayout.addWidget(self.confirmBtn, 7, 0, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(ColorSet)

        QMetaObject.connectSlotsByName(ColorSet)
    # setupUi

    def retranslateUi(self, ColorSet):
        ColorSet.setWindowTitle(QCoreApplication.translate("ColorSet", u"Color Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("ColorSet", u"Colors", None))
        self.label_7.setText(QCoreApplication.translate("ColorSet", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Color of SIMBAD Markings</span></p></body></html>", None))
        self.simcolor_Button.setText("")
        self.label_8.setText(QCoreApplication.translate("ColorSet", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Color of 2MASS Markings</span></p></body></html>", None))
        self.tmasscolor_Button.setText("")
        self.label_9.setText(QCoreApplication.translate("ColorSet", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Color of GAIA DR3 Markings</span></p></body></html>", None))
        self.gaiacolor_Button.setText("")
        self.label.setText(QCoreApplication.translate("ColorSet", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Main Object Color</span></p></body></html>", None))
        self.maincolor_Button.setText("")
        self.label_2.setText(QCoreApplication.translate("ColorSet", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Comparison Object Color</span></p></body></html>", None))
        self.compcolor_Button.setText("")
        self.label_3.setText(QCoreApplication.translate("ColorSet", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Check Object Color</span></p></body></html>", None))
        self.checkcolor_Button.setText("")
        self.confirmBtn.setText(QCoreApplication.translate("ColorSet", u"Confirm and Save", None))
    # retranslateUi

