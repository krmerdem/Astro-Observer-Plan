# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plotwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QSizePolicy,
    QStatusBar, QWidget)

from mplwidget import MplWidget

class Ui_plotwindow(object):
    def setupUi(self, plotwindow):
        if not plotwindow.objectName():
            plotwindow.setObjectName(u"plotwindow")
        plotwindow.resize(800, 630)
        self.centralwidget = QWidget(plotwindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setObjectName(u"MplWidget")
        self.MplWidget.setMinimumSize(QSize(600, 0))

        self.gridLayout.addWidget(self.MplWidget, 0, 0, 1, 1)

        plotwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(plotwindow)
        self.statusbar.setObjectName(u"statusbar")
        plotwindow.setStatusBar(self.statusbar)

        self.retranslateUi(plotwindow)

        QMetaObject.connectSlotsByName(plotwindow)
    # setupUi

    def retranslateUi(self, plotwindow):
        plotwindow.setWindowTitle(QCoreApplication.translate("plotwindow", u"Object Visibility Graph", None))
    # retranslateUi

