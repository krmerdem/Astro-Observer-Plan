# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progresswindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QProgressBar, QSizePolicy, QStatusBar, QWidget)
import icon_rc
import icon_rc
import icon_rc
import icon_rc
import icon_rc

class Ui_ProgressWindow(object):
    def setupUi(self, ProgressWindow):
        if not ProgressWindow.objectName():
            ProgressWindow.setObjectName(u"ProgressWindow")
        ProgressWindow.resize(250, 100)
        ProgressWindow.setMinimumSize(QSize(250, 100))
        ProgressWindow.setMaximumSize(QSize(250, 100))
        ProgressWindow.setStyleSheet(u"QMainWindow {\n"
"background: #1c1c27;\n"
"border-radius: 10px solid #eeeeee;\n"
"}\n"
"\n"
"QLineEdit {\n"
"background: #2d3259;\n"
"border-radius: 10px;\n"
"color: #eeeeee;\n"
"font-family:Arial ;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border: 2px solid #5190CB;\n"
"\n"
"}\n"
"QSpinBox {\n"
"background: #2d3259;\n"
"border-radius: 10px;\n"
"color: #eeeeee;\n"
"font-family:Arial ;\n"
"padding: 3px;\n"
"}\n"
"\n"
"QSpinBox::down-button\n"
"{\n"
"background:transparent;\n"
"}\n"
"\n"
"QSpinBox::up-button\n"
"{\n"
"background:transparent;\n"
"}\n"
"\n"
"QSpinBox::down-arrow\n"
"{\n"
"border-image : url(:/icon/icon/chevron-down-wh.svg);\n"
"width: 15px;\n"
"height:15px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow\n"
"{\n"
"border-image : url(:/icon/icon/chevron-up-wh.svg);\n"
"width: 15px;\n"
"height:15px;\n"
"}\n"
"\n"
"QSpinBox:hover{\n"
"background-color: #524eee;\n"
"}\n"
"\n"
"QDoubleSpinBox:hover{\n"
"background-color: #524eee;\n"
"}\n"
"\n"
"QDoubleSpinBox {\n"
"background: #2d3259;\n"
"border-radius"
                        ": 10px;\n"
"color: #eeeeee;\n"
"font-family:Arial ;\n"
"padding: 3px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"background:transparent;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"background:transparent;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow\n"
"{\n"
"border-image : url(:/icon/icon/chevron-down-wh.svg);\n"
"width: 15px;\n"
"height:15px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-arrow\n"
"{\n"
"border-image : url(:/icon/icon/chevron-up-wh.svg);\n"
"width: 15px;\n"
"height:15px;\n"
"}\n"
"\n"
"QComboBox {\n"
"background: #2d3259;\n"
"border-radius: 7px;\n"
"padding: 5px;\n"
"color: #eeeeee;\n"
"}\n"
"\n"
"QComboBox::drop-down:button{\n"
"border-radius:5px; \n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"image: url(:/icon/icon/chevron-down-wh.svg);\n"
"width: 15px;\n"
"height:15px;\n"
"margin-right:10px;\n"
"\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"background-color: #524eee;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(ProgressWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"background: #121212;\n"
"}\n"
"QGroupBox {\n"
"background-color: #1c1c27;\n"
"border-radius: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QGroupBox::title {\n"
"                subcontrol-origin: margin;\n"
"                subcontrol-position: top center;    /* position at the top center */\n"
"                padding: 10px;\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, Qt.AlignHCenter)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    min-height: 12px;\n"
"    max-height: 12px;\n"
"    border-radius: 6px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    border-radius: 6px;\n"
"    background-color: #009688;\n"
"}")
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)

        ProgressWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ProgressWindow)
        self.statusbar.setObjectName(u"statusbar")
        ProgressWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ProgressWindow)

        QMetaObject.connectSlotsByName(ProgressWindow)
    # setupUi

    def retranslateUi(self, ProgressWindow):
        ProgressWindow.setWindowTitle(QCoreApplication.translate("ProgressWindow", u"Process", None))
        self.label.setText(QCoreApplication.translate("ProgressWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Searching...</span></p></body></html>", None))
    # retranslateUi

