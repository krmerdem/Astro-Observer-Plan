# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graphsetwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QWidget)
import icon_rc
import icon_rc
import icon_rc
import icon_rc
import icon_rc

class Ui_GraphSetWindow(object):
    def setupUi(self, GraphSetWindow):
        if not GraphSetWindow.objectName():
            GraphSetWindow.setObjectName(u"GraphSetWindow")
        GraphSetWindow.resize(400, 290)
        GraphSetWindow.setMinimumSize(QSize(400, 290))
        GraphSetWindow.setMaximumSize(QSize(400, 290))
        icon = QIcon()
        icon.addFile(u":/icon/icon/settingswin.svg", QSize(), QIcon.Normal, QIcon.Off)
        GraphSetWindow.setWindowIcon(icon)
        GraphSetWindow.setStyleSheet(u"QMainWindow {\n"
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
        self.centralwidget = QWidget(GraphSetWindow)
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
        self.confirmBtn = QPushButton(self.centralwidget)
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

        self.gridLayout.addWidget(self.confirmBtn, 1, 0, 1, 1)

        self.graphset_groupBox = QGroupBox(self.centralwidget)
        self.graphset_groupBox.setObjectName(u"graphset_groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphset_groupBox.sizePolicy().hasHeightForWidth())
        self.graphset_groupBox.setSizePolicy(sizePolicy)
        self.graphset_groupBox.setMinimumSize(QSize(380, 130))
        self.graphset_groupBox.setMaximumSize(QSize(550, 16777215))
        self.graphset_groupBox.setStyleSheet(u"QCheckBox{\n"
"color: #eeeeee\n"
"}")
        self.gridLayout_2 = QGridLayout(self.graphset_groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.graphiconlabel = QLabel(self.graphset_groupBox)
        self.graphiconlabel.setObjectName(u"graphiconlabel")
        self.graphiconlabel.setMinimumSize(QSize(30, 30))
        self.graphiconlabel.setMaximumSize(QSize(30, 30))
        self.graphiconlabel.setPixmap(QPixmap(u":/icon/icon/bar-chart-2.svg"))
        self.graphiconlabel.setScaledContents(True)

        self.gridLayout_2.addWidget(self.graphiconlabel, 0, 0, 1, 1)

        self.graphwidget = QWidget(self.graphset_groupBox)
        self.graphwidget.setObjectName(u"graphwidget")
        self.graphwidget.setMinimumSize(QSize(0, 40))
        self.graphwidget.setStyleSheet(u"QRadioButton{\n"
"color: #eeeeee;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 18px;\n"
"height: 18px;\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked\n"
"{\n"
"   background-color: #eeeeee;\n"
"}\n"
"QRadioButton::indicator:unchecked:hover\n"
"{\n"
"    background-color: #6316AC;\n"
"}\n"
"QRadioButton::indicator::checked \n"
"{\n"
"   background-color: #6fcf97;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:pressed \n"
"{\n"
"   background-color: #7e31b5;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed \n"
"{\n"
"   background-color: #7e31b5;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.graphwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.light_radioButton = QRadioButton(self.graphwidget)
        self.light_radioButton.setObjectName(u"light_radioButton")
        self.light_radioButton.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        self.light_radioButton.setFont(font)
        self.light_radioButton.setChecked(False)

        self.horizontalLayout.addWidget(self.light_radioButton, 0, Qt.AlignVCenter)

        self.dark_radioButton = QRadioButton(self.graphwidget)
        self.dark_radioButton.setObjectName(u"dark_radioButton")
        self.dark_radioButton.setMinimumSize(QSize(0, 30))
        self.dark_radioButton.setFont(font)
        self.dark_radioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.dark_radioButton, 0, Qt.AlignTop)


        self.gridLayout_2.addWidget(self.graphwidget, 0, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 1, 1, 1, 1)

        self.moonalt_checkBox = QCheckBox(self.graphset_groupBox)
        self.moonalt_checkBox.setObjectName(u"moonalt_checkBox")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        self.moonalt_checkBox.setFont(font1)
        self.moonalt_checkBox.setStyleSheet(u"")
        self.moonalt_checkBox.setChecked(True)

        self.gridLayout_2.addWidget(self.moonalt_checkBox, 2, 0, 1, 2)

        self.moondist_checkBox = QCheckBox(self.graphset_groupBox)
        self.moondist_checkBox.setObjectName(u"moondist_checkBox")
        self.moondist_checkBox.setFont(font1)
        self.moondist_checkBox.setStyleSheet(u"")
        self.moondist_checkBox.setChecked(True)

        self.gridLayout_2.addWidget(self.moondist_checkBox, 3, 0, 1, 2)

        self.asttime_checkBox = QCheckBox(self.graphset_groupBox)
        self.asttime_checkBox.setObjectName(u"asttime_checkBox")
        self.asttime_checkBox.setFont(font1)
        self.asttime_checkBox.setStyleSheet(u"")
        self.asttime_checkBox.setChecked(True)

        self.gridLayout_2.addWidget(self.asttime_checkBox, 4, 0, 1, 2)


        self.gridLayout.addWidget(self.graphset_groupBox, 0, 0, 1, 1)

        GraphSetWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(GraphSetWindow)
        self.statusbar.setObjectName(u"statusbar")
        GraphSetWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GraphSetWindow)

        QMetaObject.connectSlotsByName(GraphSetWindow)
    # setupUi

    def retranslateUi(self, GraphSetWindow):
        GraphSetWindow.setWindowTitle(QCoreApplication.translate("GraphSetWindow", u"Astro Observer Plan- Graph Settings", None))
        self.confirmBtn.setText(QCoreApplication.translate("GraphSetWindow", u"Confirm and Save", None))
        self.graphset_groupBox.setTitle(QCoreApplication.translate("GraphSetWindow", u"Graph Settings", None))
        self.graphiconlabel.setText("")
        self.light_radioButton.setText(QCoreApplication.translate("GraphSetWindow", u"Light", None))
        self.dark_radioButton.setText(QCoreApplication.translate("GraphSetWindow", u"Dark", None))
        self.moonalt_checkBox.setText(QCoreApplication.translate("GraphSetWindow", u"Show moon altitude (Staralt)", None))
        self.moondist_checkBox.setText(QCoreApplication.translate("GraphSetWindow", u"Show moon distance (Staralt)", None))
        self.asttime_checkBox.setText(QCoreApplication.translate("GraphSetWindow", u"Show astronomical time intervals (Staralt)", None))
    # retranslateUi

