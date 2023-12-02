# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDoubleSpinBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QStatusBar,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)
import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1215, 919)
        MainWindow.setMinimumSize(QSize(1215, 875))
        icon = QIcon()
        icon.addFile(u":/icon/icon/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"background: #1c1c27;\n"
"/***border-radius: 10px solid #eeeeee; ***/\n"
"}\n"
"\n"
"\n"
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
"border-radius: 10px;\n"
"color: #eeeeee;\n"
"font-family:Arial ;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"background:transparent;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button\n"
""
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
"\n"
"QDateEdit:hover{\n"
"background-color: #524eee;\n"
"}\n"
"\n"
"QDateEdit {\n"
"background: #2d3259;\n"
"border-radius: 10px;\n"
"color: #eeeeee;\n"
"font-family:Arial ;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QDateEdit::down-button\n"
"{\n"
"background:transparent;\n"
"}\n"
"\n"
"QDateEdit::up-button\n"
"{\n"
"background:transparent;\n"
"}\n"
"\n"
"QDateEdit::down-arrow\n"
"{\n"
"border-image : url(:/icon/icon/chevron-down-wh.svg);\n"
"width: 15px;\n"
"height:15px;\n"
"\n"
"}\n"
"\n"
"QDateEdit::up-arrow\n"
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
"color"
                        ": #eeeeee;\n"
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
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(80, 80, 122);\n"
"    min-height: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px"
                        ";\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"    border-image: url(:/icon/icon/chevron-up-wh.svg);\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"    border-image: url(:/icon/icon/chevron-down-wh.svg);\n"
"    background: n"
                        "one;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
" QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    height: 14px;\n"
"    margin: 0 15px 0 15px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {	\n"
"    background-color: rgb(80, 80, 122);\n"
"    min-width: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {	\n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed {	\n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    width: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {	\n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"\n"
""
                        "QScrollBar::sub-line:horizontal:pressed {	\n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    width: 15px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {	\n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {	\n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"    border-image: url(:/icon/icon/chevron-left-wh.svg);\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"    border-image: url(:/icon/icon/chevron-right-wh.svg);\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"   background: #1f1b"
                        "24;\n"
"   color: #eeeeee;\n"
"   selection-background-color:#6316AC;\n"
"\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
"background: #121212;\n"
"/***border: 1px solid #808080; **/\n"
"}")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(6, -1, -1, -1)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(50, 0))
        self.widget.setMaximumSize(QSize(50, 16777215))
        self.widget.setStyleSheet(u"QWidget {\n"
"	background-color: #1c1c27;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"border-radius: 15px;\n"
"background-color:#1c1c27;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:#6316AC;\n"
"}\n"
"    \n"
"QPushButton:flat {\n"
"    background-color: #6316AC;     \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #7e31b5;\n"
"}\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(50, 0))
        self.frame_4.setMaximumSize(QSize(50, 400))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(25)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.objvisBtn = QPushButton(self.frame_4)
        self.objvisBtn.setObjectName(u"objvisBtn")
        self.objvisBtn.setMinimumSize(QSize(45, 45))
        self.objvisBtn.setMaximumSize(QSize(45, 45))
        self.objvisBtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.objvisBtn.setIcon(icon1)
        self.objvisBtn.setIconSize(QSize(24, 24))
        self.objvisBtn.setCheckable(False)
        self.objvisBtn.setChecked(False)
        self.objvisBtn.setAutoDefault(True)
        self.objvisBtn.setFlat(True)

        self.verticalLayout_5.addWidget(self.objvisBtn, 0, Qt.AlignHCenter)

        self.simdataBtn = QPushButton(self.frame_4)
        self.simdataBtn.setObjectName(u"simdataBtn")
        self.simdataBtn.setMinimumSize(QSize(45, 45))
        self.simdataBtn.setMaximumSize(QSize(45, 45))
        self.simdataBtn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/search_wh.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.simdataBtn.setIcon(icon2)
        self.simdataBtn.setIconSize(QSize(24, 24))
        self.simdataBtn.setCheckable(False)
        self.simdataBtn.setAutoDefault(True)

        self.verticalLayout_5.addWidget(self.simdataBtn, 0, Qt.AlignHCenter)

        self.convBtn = QPushButton(self.frame_4)
        self.convBtn.setObjectName(u"convBtn")
        self.convBtn.setMinimumSize(QSize(45, 45))
        self.convBtn.setMaximumSize(QSize(45, 45))
        self.convBtn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/repeat_wh.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.convBtn.setIcon(icon3)
        self.convBtn.setIconSize(QSize(24, 24))
        self.convBtn.setCheckable(False)
        self.convBtn.setAutoDefault(True)

        self.verticalLayout_5.addWidget(self.convBtn, 0, Qt.AlignHCenter)

        self.infoBtn = QPushButton(self.frame_4)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setMinimumSize(QSize(45, 45))
        self.infoBtn.setMaximumSize(QSize(45, 45))
        self.infoBtn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon4)
        self.infoBtn.setIconSize(QSize(24, 24))
        self.infoBtn.setCheckable(False)
        self.infoBtn.setAutoDefault(True)

        self.verticalLayout_5.addWidget(self.infoBtn, 0, Qt.AlignHCenter)

        self.sofwBtn = QPushButton(self.frame_4)
        self.sofwBtn.setObjectName(u"sofwBtn")
        self.sofwBtn.setMinimumSize(QSize(45, 45))
        self.sofwBtn.setMaximumSize(QSize(45, 45))
        self.sofwBtn.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/dev_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sofwBtn.setIcon(icon5)
        self.sofwBtn.setIconSize(QSize(24, 24))
        self.sofwBtn.setCheckable(False)
        self.sofwBtn.setAutoDefault(True)

        self.verticalLayout_5.addWidget(self.sofwBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_4, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.gridLayout_2.addWidget(self.widget, 1, 0, 1, 1)

        self.frame_aukr = QFrame(self.centralwidget)
        self.frame_aukr.setObjectName(u"frame_aukr")
        self.frame_aukr.setMaximumSize(QSize(16777215, 50))
        self.frame_aukr.setStyleSheet(u"#frame_aukr{\n"
"background-color: #000000;\n"
"border-radius: 15px;\n"
"}")
        self.frame_aukr.setFrameShape(QFrame.StyledPanel)
        self.frame_aukr.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_aukr)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(12, -1, -1, -1)
        self.headerlabel = QLabel(self.frame_aukr)
        self.headerlabel.setObjectName(u"headerlabel")
        self.headerlabel.setMaximumSize(QSize(250, 16777215))
        self.headerlabel.setFrameShadow(QFrame.Plain)
        self.headerlabel.setPixmap(QPixmap(u":/icon/icon/header.png"))
        self.headerlabel.setScaledContents(True)

        self.gridLayout_7.addWidget(self.headerlabel, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.top_buttons = QFrame(self.frame_aukr)
        self.top_buttons.setObjectName(u"top_buttons")
        self.top_buttons.setMaximumSize(QSize(120, 16777215))
        self.top_buttons.setStyleSheet(u"QPushButton {\n"
"border-radius: 5px;\n"
"background-color:#000000;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #6316AC;\n"
"}\n"
"")
        self.top_buttons.setFrameShape(QFrame.StyledPanel)
        self.top_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_buttons)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QPushButton(self.top_buttons)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setMinimumSize(QSize(30, 30))
        self.minimizeButton.setMaximumSize(QSize(30, 30))
        self.minimizeButton.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon6)
        self.minimizeButton.setIconSize(QSize(24, 24))
        self.minimizeButton.setCheckable(False)
        self.minimizeButton.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.minimizeButton)

        self.restoreButton = QPushButton(self.top_buttons)
        self.restoreButton.setObjectName(u"restoreButton")
        self.restoreButton.setMinimumSize(QSize(30, 30))
        self.restoreButton.setMaximumSize(QSize(30, 30))
        self.restoreButton.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreButton.setIcon(icon7)
        self.restoreButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.restoreButton)

        self.closeButton = QPushButton(self.top_buttons)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(30, 30))
        self.closeButton.setMaximumSize(QSize(30, 30))
        self.closeButton.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icon/icon/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon8)
        self.closeButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeButton)


        self.gridLayout_7.addWidget(self.top_buttons, 0, 7, 1, 1, Qt.AlignRight|Qt.AlignVCenter)

        self.label_4 = QLabel(self.frame_aukr)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(40, 0))
        self.label_4.setMaximumSize(QSize(35, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        self.label_4.setFont(font)

        self.gridLayout_7.addWidget(self.label_4, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_aukr, 0, 0, 1, 2)

        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"QStackedWidget {\n"
"	background: #28293d;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#objvisPage {\n"
"	background: #28293d;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#simdataPage {\n"
"	background: #28293d;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#convPage {\n"
"	background: #28293d;\n"
"}\n"
"\n"
"#infoPage {\n"
"	background: #28293d;\n"
"}\n"
"\n"
"#softwPage {\n"
"	background: #28293d;\n"
"}")
        self.objvisPage = QWidget()
        self.objvisPage.setObjectName(u"objvisPage")
        self.objvisPage.setStyleSheet(u"QGroupBox {\n"
"background-color: #1c1c27;\n"
"border-radius: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QGroupBox::title {\n"
"                subcontrol-origin: margin;\n"
"                subcontrol-position: top center;    /* position at the top center */\n"
"                padding: 10px;\n"
"}\n"
"\n"
"")
        self.gridLayout = QGridLayout(self.objvisPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.astinf_groupBox = QGroupBox(self.objvisPage)
        self.astinf_groupBox.setObjectName(u"astinf_groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.astinf_groupBox.sizePolicy().hasHeightForWidth())
        self.astinf_groupBox.setSizePolicy(sizePolicy)
        self.astinf_groupBox.setMinimumSize(QSize(330, 0))
        self.astinf_groupBox.setMaximumSize(QSize(350, 16777215))
        self.astinf_groupBox.setStyleSheet(u"QLineEdit {\n"
"background: transparent;\n"
"border-radius: 0px;\n"
"border-left: 2px solid #DAF7A6;\n"
"color: #eeeeee;\n"
"font-family:Arial ;\n"
"padding-left: 10px;\n"
"}\n"
"")
        self.gridLayout_11 = QGridLayout(self.astinf_groupBox)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(15, 15, 15, -1)
        self.daylighttextlabel = QLabel(self.astinf_groupBox)
        self.daylighttextlabel.setObjectName(u"daylighttextlabel")
        self.daylighttextlabel.setMinimumSize(QSize(85, 30))
        self.daylighttextlabel.setMaximumSize(QSize(16777215, 30))
        self.daylighttextlabel.setFont(font)

        self.gridLayout_11.addWidget(self.daylighttextlabel, 1, 1, 1, 1)

        self.elevcorrectframe = QFrame(self.astinf_groupBox)
        self.elevcorrectframe.setObjectName(u"elevcorrectframe")
        self.elevcorrectframe.setMaximumSize(QSize(16777215, 80))
        self.elevcorrectframe.setFrameShape(QFrame.StyledPanel)
        self.elevcorrectframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.elevcorrectframe)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.elevcor_rb_widget = QWidget(self.elevcorrectframe)
        self.elevcor_rb_widget.setObjectName(u"elevcor_rb_widget")
        self.elevcor_rb_widget.setMinimumSize(QSize(0, 40))
        self.elevcor_rb_widget.setStyleSheet(u"QRadioButton{\n"
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
        self.horizontalLayout_9 = QHBoxLayout(self.elevcor_rb_widget)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.elevcoryes_radioBtn = QRadioButton(self.elevcor_rb_widget)
        self.elevcoryes_radioBtn.setObjectName(u"elevcoryes_radioBtn")
        self.elevcoryes_radioBtn.setMinimumSize(QSize(0, 30))
        self.elevcoryes_radioBtn.setFont(font)
        self.elevcoryes_radioBtn.setChecked(False)

        self.horizontalLayout_9.addWidget(self.elevcoryes_radioBtn, 0, Qt.AlignVCenter)

        self.elevcorno_radioBtn = QRadioButton(self.elevcor_rb_widget)
        self.elevcorno_radioBtn.setObjectName(u"elevcorno_radioBtn")
        self.elevcorno_radioBtn.setMinimumSize(QSize(0, 30))
        self.elevcorno_radioBtn.setFont(font)
        self.elevcorno_radioBtn.setChecked(True)

        self.horizontalLayout_9.addWidget(self.elevcorno_radioBtn, 0, Qt.AlignVCenter)


        self.gridLayout_24.addWidget(self.elevcor_rb_widget, 1, 1, 1, 1)

        self.elevcortextlabel = QLabel(self.elevcorrectframe)
        self.elevcortextlabel.setObjectName(u"elevcortextlabel")
        self.elevcortextlabel.setTextFormat(Qt.RichText)

        self.gridLayout_24.addWidget(self.elevcortextlabel, 0, 1, 1, 1)

        self.elevinfoBtn = QPushButton(self.elevcorrectframe)
        self.elevinfoBtn.setObjectName(u"elevinfoBtn")
        self.elevinfoBtn.setMinimumSize(QSize(20, 20))
        self.elevinfoBtn.setMaximumSize(QSize(20, 20))
        self.elevinfoBtn.setStyleSheet(u"QPushButton {\n"
"background-color:transparent;\n"
"}\n"
"")
        self.elevinfoBtn.setIcon(icon4)

        self.gridLayout_24.addWidget(self.elevinfoBtn, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.elevcorrectframe, 0, 0, 1, 3)

        self.daylight_lineEdit = QLineEdit(self.astinf_groupBox)
        self.daylight_lineEdit.setObjectName(u"daylight_lineEdit")
        self.daylight_lineEdit.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.daylight_lineEdit.setFont(font1)
        self.daylight_lineEdit.setStyleSheet(u"")
        self.daylight_lineEdit.setReadOnly(True)

        self.gridLayout_11.addWidget(self.daylight_lineEdit, 1, 2, 1, 1)

        self.asttwi2textlabel = QLabel(self.astinf_groupBox)
        self.asttwi2textlabel.setObjectName(u"asttwi2textlabel")
        self.asttwi2textlabel.setMinimumSize(QSize(0, 30))
        self.asttwi2textlabel.setMaximumSize(QSize(16777215, 30))
        self.asttwi2textlabel.setFont(font)

        self.gridLayout_11.addWidget(self.asttwi2textlabel, 6, 1, 1, 1)

        self.at2_lineEdit = QLineEdit(self.astinf_groupBox)
        self.at2_lineEdit.setObjectName(u"at2_lineEdit")
        self.at2_lineEdit.setMinimumSize(QSize(0, 30))
        self.at2_lineEdit.setFont(font1)
        self.at2_lineEdit.setStyleSheet(u"")
        self.at2_lineEdit.setReadOnly(True)

        self.gridLayout_11.addWidget(self.at2_lineEdit, 6, 2, 1, 1)

        self.nighttextlabel = QLabel(self.astinf_groupBox)
        self.nighttextlabel.setObjectName(u"nighttextlabel")
        self.nighttextlabel.setMinimumSize(QSize(0, 30))
        self.nighttextlabel.setMaximumSize(QSize(16777215, 30))
        self.nighttextlabel.setFont(font)

        self.gridLayout_11.addWidget(self.nighttextlabel, 5, 1, 1, 1)

        self.nautwitextlabel = QLabel(self.astinf_groupBox)
        self.nautwitextlabel.setObjectName(u"nautwitextlabel")
        self.nautwitextlabel.setMinimumSize(QSize(85, 30))
        self.nautwitextlabel.setMaximumSize(QSize(16777215, 30))
        self.nautwitextlabel.setFont(font)

        self.gridLayout_11.addWidget(self.nautwitextlabel, 3, 1, 1, 1)

        self.at1_lineEdit = QLineEdit(self.astinf_groupBox)
        self.at1_lineEdit.setObjectName(u"at1_lineEdit")
        self.at1_lineEdit.setMinimumSize(QSize(0, 30))
        self.at1_lineEdit.setFont(font1)
        self.at1_lineEdit.setStyleSheet(u"")
        self.at1_lineEdit.setReadOnly(True)

        self.gridLayout_11.addWidget(self.at1_lineEdit, 4, 2, 1, 1)

        self.night_lineEdit = QLineEdit(self.astinf_groupBox)
        self.night_lineEdit.setObjectName(u"night_lineEdit")
        self.night_lineEdit.setMinimumSize(QSize(0, 30))
        self.night_lineEdit.setFont(font1)
        self.night_lineEdit.setStyleSheet(u"")
        self.night_lineEdit.setReadOnly(True)

        self.gridLayout_11.addWidget(self.night_lineEdit, 5, 2, 1, 1)

        self.civiltwi2textlabel = QLabel(self.astinf_groupBox)
        self.civiltwi2textlabel.setObjectName(u"civiltwi2textlabel")
        self.civiltwi2textlabel.setMinimumSize(QSize(0, 30))
        self.civiltwi2textlabel.setMaximumSize(QSize(16777215, 30))
        self.civiltwi2textlabel.setFont(font)

        self.gridLayout_11.addWidget(self.civiltwi2textlabel, 8, 1, 1, 1)

        self.nt2_lineEdit = QLineEdit(self.astinf_groupBox)
        self.nt2_lineEdit.setObjectName(u"nt2_lineEdit")
        self.nt2_lineEdit.setMinimumSize(QSize(0, 30))
        self.nt2_lineEdit.setFont(font1)
        self.nt2_lineEdit.setStyleSheet(u"")
        self.nt2_lineEdit.setReadOnly(True)

        self.gridLayout_11.addWidget(self.nt2_lineEdit, 7, 2, 1, 1)

        self.nautwi2textlabel = QLabel(self.astinf_groupBox)
        self.nautwi2textlabel.setObjectName(u"nautwi2textlabel")
        self.nautwi2textlabel.setMinimumSize(QSize(85, 30))
        self.nautwi2textlabel.setMaximumSize(QSize(16777215, 30))
        self.nautwi2textlabel.setFont(font)

        self.gridLayout_11.addWidget(self.nautwi2textlabel, 7, 1, 1, 1)

        self.civiltwilabel = QLabel(self.astinf_groupBox)
        self.civiltwilabel.setObjectName(u"civiltwilabel")
        self.civiltwilabel.setMinimumSize(QSize(30, 30))
        self.civiltwilabel.setMaximumSize(QSize(30, 30))
        self.civiltwilabel.setPixmap(QPixmap(u":/icon/icon/civil_twi.png"))
        self.civiltwilabel.setScaledContents(True)

        self.gridLayout_11.addWidget(self.civiltwilabel, 2, 0, 1, 1)

        self.daylighticonlabel = QLabel(self.astinf_groupBox)
        self.daylighticonlabel.setObjectName(u"daylighticonlabel")
        self.daylighticonlabel.setMinimumSize(QSize(30, 30))
        self.daylighticonlabel.setMaximumSize(QSize(30, 30))
        self.daylighticonlabel.setPixmap(QPixmap(u":/icon/icon/daylight_wh.png"))
        self.daylighticonlabel.setScaledContents(True)

        self.gridLayout_11.addWidget(self.daylighticonlabel, 1, 0, 1, 1)

        self.asttwilabel = QLabel(self.astinf_groupBox)
        self.asttwilabel.setObjectName(u"asttwilabel")
        self.asttwilabel.setMinimumSize(QSize(30, 30))
        self.asttwilabel.setMaximumSize(QSize(30, 30))
        self.asttwilabel.setPixmap(QPixmap(u":/icon/icon/astro_twi.png"))
        self.asttwilabel.setScaledContents(True)

        self.gridLayout_11.addWidget(self.asttwilabel, 4, 0, 1, 1)

        self.nightlabel = QLabel(self.astinf_groupBox)
        self.nightlabel.setObjectName(u"nightlabel")
        self.nightlabel.setMinimumSize(QSize(30, 30))
        self.nightlabel.setMaximumSize(QSize(30, 30))
        self.nightlabel.setPixmap(QPixmap(u":/icon/icon/night.png"))
        self.nightlabel.setScaledContents(True)

        self.gridLayout_11.addWidget(self.nightlabel, 5, 0, 1, 1)

        self.ct1_lineEdit = QLineEdit(self.astinf_groupBox)
        self.ct1_lineEdit.setObjectName(u"ct1_lineEdit")
        self.ct1_lineEdit.setMinimumSize(QSize(0, 30))
        self.ct1_lineEdit.setFont(font1)
        self.ct1_lineEdit.setStyleSheet(u"")
        self.ct1_lineEdit.setReadOnly(True)

        self.gridLayout_11.addWidget(self.ct1_lineEdit, 2, 2, 1, 1)

        self.nautwilabel = QLabel(self.astinf_groupBox)
        self.nautwilabel.setObjectName(u"nautwilabel")
        self.nautwilabel.setMinimumSize(QSize(30, 30))
        self.nautwilabel.setMaximumSize(QSize(30, 30))
        self.nautwilabel.setPixmap(QPixmap(u":/icon/icon/nau_twi.png"))
        self.nautwilabel.setScaledContents(True)

        self.gridLayout_11.addWidget(self.nautwilabel, 3, 0, 1, 1)

        self.civiltiwitextlabel = QLabel(self.astinf_groupBox)
        self.civiltiwitextlabel.setObjectName(u"civiltiwitextlabel")
        self.civiltiwitextlabel.setMinimumSize(QSize(85, 30))
        self.civiltiwitextlabel.setMaximumSize(QSize(16777215, 30))
        self.civiltiwitextlabel.setFont(font)

        self.gridLayout_11.addWidget(self.civiltiwitextlabel, 2, 1, 1, 1)

        self.nautwi2label = QLabel(self.astinf_groupBox)
        self.nautwi2label.setObjectName(u"nautwi2label")
        self.nautwi2label.setMinimumSize(QSize(30, 30))
        self.nautwi2label.setMaximumSize(QSize(30, 30))
        self.nautwi2label.setPixmap(QPixmap(u":/icon/icon/nau_twi.png"))
        self.nautwi2label.setScaledContents(True)

        self.gridLayout_11.addWidget(self.nautwi2label, 7, 0, 1, 1)

        self.asttwitextlabel = QLabel(self.astinf_groupBox)
        self.asttwitextlabel.setObjectName(u"asttwitextlabel")
        self.asttwitextlabel.setMinimumSize(QSize(0, 30))
        self.asttwitextlabel.setMaximumSize(QSize(16777215, 30))
        self.asttwitextlabel.setFont(font)

        self.gridLayout_11.addWidget(self.asttwitextlabel, 4, 1, 1, 1)

        self.asttwi2label = QLabel(self.astinf_groupBox)
        self.asttwi2label.setObjectName(u"asttwi2label")
        self.asttwi2label.setMinimumSize(QSize(30, 30))
        self.asttwi2label.setMaximumSize(QSize(30, 30))
        self.asttwi2label.setPixmap(QPixmap(u":/icon/icon/astro_twi.png"))
        self.asttwi2label.setScaledContents(True)

        self.gridLayout_11.addWidget(self.asttwi2label, 6, 0, 1, 1)

        self.nt1_lineEdit = QLineEdit(self.astinf_groupBox)
        self.nt1_lineEdit.setObjectName(u"nt1_lineEdit")
        self.nt1_lineEdit.setMinimumSize(QSize(0, 30))
        self.nt1_lineEdit.setFont(font1)
        self.nt1_lineEdit.setStyleSheet(u"")
        self.nt1_lineEdit.setReadOnly(True)

        self.gridLayout_11.addWidget(self.nt1_lineEdit, 3, 2, 1, 1)

        self.ct2_lineEdit = QLineEdit(self.astinf_groupBox)
        self.ct2_lineEdit.setObjectName(u"ct2_lineEdit")
        self.ct2_lineEdit.setMinimumSize(QSize(0, 30))
        self.ct2_lineEdit.setFont(font1)
        self.ct2_lineEdit.setStyleSheet(u"")
        self.ct2_lineEdit.setReadOnly(True)

        self.gridLayout_11.addWidget(self.ct2_lineEdit, 8, 2, 1, 1)

        self.civiltwi2label = QLabel(self.astinf_groupBox)
        self.civiltwi2label.setObjectName(u"civiltwi2label")
        self.civiltwi2label.setMinimumSize(QSize(30, 30))
        self.civiltwi2label.setMaximumSize(QSize(30, 30))
        self.civiltwi2label.setPixmap(QPixmap(u":/icon/icon/civil_twi.png"))
        self.civiltwi2label.setScaledContents(True)

        self.gridLayout_11.addWidget(self.civiltwi2label, 8, 0, 1, 1)

        self.frame = QFrame(self.astinf_groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 200))
        self.frame.setMaximumSize(QSize(16777215, 200))
        self.frame.setStyleSheet(u"QLineEdit {\n"
"border-left: 2px solid rgb(255, 0, 127);\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, -1, 0, -1)
        self.illutextlabel = QLabel(self.frame)
        self.illutextlabel.setObjectName(u"illutextlabel")
        self.illutextlabel.setMinimumSize(QSize(85, 30))
        self.illutextlabel.setMaximumSize(QSize(85, 30))
        self.illutextlabel.setFont(font)

        self.gridLayout_27.addWidget(self.illutextlabel, 1, 1, 1, 1)

        self.phasetextlabel = QLabel(self.frame)
        self.phasetextlabel.setObjectName(u"phasetextlabel")
        self.phasetextlabel.setMinimumSize(QSize(85, 30))
        self.phasetextlabel.setMaximumSize(QSize(85, 30))
        self.phasetextlabel.setFont(font)

        self.gridLayout_27.addWidget(self.phasetextlabel, 2, 1, 1, 1)

        self.moonphaseline = QLineEdit(self.frame)
        self.moonphaseline.setObjectName(u"moonphaseline")
        self.moonphaseline.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(11)
        self.moonphaseline.setFont(font2)
        self.moonphaseline.setStyleSheet(u"")
        self.moonphaseline.setReadOnly(True)

        self.gridLayout_27.addWidget(self.moonphaseline, 2, 2, 1, 2)

        self.illuminationline = QLineEdit(self.frame)
        self.illuminationline.setObjectName(u"illuminationline")
        self.illuminationline.setMinimumSize(QSize(0, 30))
        self.illuminationline.setFont(font2)
        self.illuminationline.setStyleSheet(u"")
        self.illuminationline.setReadOnly(True)

        self.gridLayout_27.addWidget(self.illuminationline, 1, 2, 1, 2)

        self.moonsetline = QLineEdit(self.frame)
        self.moonsetline.setObjectName(u"moonsetline")
        self.moonsetline.setMinimumSize(QSize(0, 30))
        self.moonsetline.setFont(font2)
        self.moonsetline.setStyleSheet(u"")
        self.moonsetline.setReadOnly(True)

        self.gridLayout_27.addWidget(self.moonsetline, 4, 2, 1, 2)

        self.settextlabel = QLabel(self.frame)
        self.settextlabel.setObjectName(u"settextlabel")
        self.settextlabel.setMinimumSize(QSize(85, 30))
        self.settextlabel.setMaximumSize(QSize(85, 30))
        self.settextlabel.setFont(font)

        self.gridLayout_27.addWidget(self.settextlabel, 4, 1, 1, 1)

        self.illuiconlabel = QLabel(self.frame)
        self.illuiconlabel.setObjectName(u"illuiconlabel")
        self.illuiconlabel.setMinimumSize(QSize(30, 30))
        self.illuiconlabel.setMaximumSize(QSize(30, 30))
        self.illuiconlabel.setPixmap(QPixmap(u":/icon/icon/illumination.svg"))
        self.illuiconlabel.setScaledContents(True)

        self.gridLayout_27.addWidget(self.illuiconlabel, 1, 0, 1, 1)

        self.seticonlabel = QLabel(self.frame)
        self.seticonlabel.setObjectName(u"seticonlabel")
        self.seticonlabel.setMinimumSize(QSize(30, 30))
        self.seticonlabel.setMaximumSize(QSize(30, 30))
        self.seticonlabel.setPixmap(QPixmap(u":/icon/icon/set.svg"))
        self.seticonlabel.setScaledContents(True)

        self.gridLayout_27.addWidget(self.seticonlabel, 4, 0, 1, 1)

        self.phaseiconlabel = QLabel(self.frame)
        self.phaseiconlabel.setObjectName(u"phaseiconlabel")
        self.phaseiconlabel.setMinimumSize(QSize(30, 30))
        self.phaseiconlabel.setMaximumSize(QSize(30, 30))
        self.phaseiconlabel.setPixmap(QPixmap(u":/icon/icon/full_moon.svg"))
        self.phaseiconlabel.setScaledContents(True)

        self.gridLayout_27.addWidget(self.phaseiconlabel, 2, 0, 1, 1)

        self.elevcortextlabel_2 = QLabel(self.frame)
        self.elevcortextlabel_2.setObjectName(u"elevcortextlabel_2")
        self.elevcortextlabel_2.setMinimumSize(QSize(0, 25))
        self.elevcortextlabel_2.setMaximumSize(QSize(16777215, 25))
        self.elevcortextlabel_2.setTextFormat(Qt.RichText)

        self.gridLayout_27.addWidget(self.elevcortextlabel_2, 0, 0, 1, 4)

        self.risetextlabel = QLabel(self.frame)
        self.risetextlabel.setObjectName(u"risetextlabel")
        self.risetextlabel.setMinimumSize(QSize(85, 30))
        self.risetextlabel.setMaximumSize(QSize(85, 30))
        self.risetextlabel.setFont(font)

        self.gridLayout_27.addWidget(self.risetextlabel, 3, 1, 1, 1)

        self.riseiconlabel = QLabel(self.frame)
        self.riseiconlabel.setObjectName(u"riseiconlabel")
        self.riseiconlabel.setMinimumSize(QSize(30, 30))
        self.riseiconlabel.setMaximumSize(QSize(30, 30))
        self.riseiconlabel.setPixmap(QPixmap(u":/icon/icon/rise.svg"))
        self.riseiconlabel.setScaledContents(True)

        self.gridLayout_27.addWidget(self.riseiconlabel, 3, 0, 1, 1)

        self.moonriseline = QLineEdit(self.frame)
        self.moonriseline.setObjectName(u"moonriseline")
        self.moonriseline.setMinimumSize(QSize(0, 30))
        self.moonriseline.setFont(font2)
        self.moonriseline.setStyleSheet(u"")
        self.moonriseline.setReadOnly(True)

        self.gridLayout_27.addWidget(self.moonriseline, 3, 2, 1, 1)


        self.gridLayout_11.addWidget(self.frame, 9, 0, 1, 3)


        self.gridLayout.addWidget(self.astinf_groupBox, 0, 3, 4, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.loc_groupBox = QGroupBox(self.objvisPage)
        self.loc_groupBox.setObjectName(u"loc_groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.loc_groupBox.sizePolicy().hasHeightForWidth())
        self.loc_groupBox.setSizePolicy(sizePolicy1)
        self.loc_groupBox.setMinimumSize(QSize(380, 250))
        self.loc_groupBox.setMaximumSize(QSize(550, 16777215))
        self.loc_groupBox.setStyleSheet(u"QLineEdit{\n"
"background: transparent;\n"
"border: 0px;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.loc_groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(15, -1, 15, 20)
        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.locframe = QFrame(self.loc_groupBox)
        self.locframe.setObjectName(u"locframe")
        self.locframe.setStyleSheet(u"QLineEdit{\n"
"background-color:transparent;\n"
"color: #eeeeee;\n"
"/***border: 0px solid;***/\n"
"}")
        self.locframe.setFrameShape(QFrame.StyledPanel)
        self.locframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.locframe)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(-1, 30, -1, 30)
        self.teliconlabel = QLabel(self.locframe)
        self.teliconlabel.setObjectName(u"teliconlabel")
        self.teliconlabel.setMinimumSize(QSize(20, 20))
        self.teliconlabel.setMaximumSize(QSize(20, 20))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        self.teliconlabel.setFont(font3)
        self.teliconlabel.setPixmap(QPixmap(u":/icon/icon/telescope.png"))
        self.teliconlabel.setScaledContents(True)

        self.gridLayout_8.addWidget(self.teliconlabel, 7, 0, 1, 1)

        self.comboBox = QComboBox(self.locframe)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(350, 16777215))
        self.comboBox.setFont(font3)

        self.gridLayout_8.addWidget(self.comboBox, 0, 1, 1, 1)

        self.eleviconlabel = QLabel(self.locframe)
        self.eleviconlabel.setObjectName(u"eleviconlabel")
        self.eleviconlabel.setMinimumSize(QSize(20, 20))
        self.eleviconlabel.setMaximumSize(QSize(20, 20))
        self.eleviconlabel.setFont(font3)
        self.eleviconlabel.setPixmap(QPixmap(u":/icon/icon/elev.png"))
        self.eleviconlabel.setScaledContents(True)

        self.gridLayout_8.addWidget(self.eleviconlabel, 3, 0, 1, 1)

        self.utclineEdit = QLineEdit(self.locframe)
        self.utclineEdit.setObjectName(u"utclineEdit")
        self.utclineEdit.setMinimumSize(QSize(0, 30))
        self.utclineEdit.setMaximumSize(QSize(16777215, 30))
        self.utclineEdit.setFont(font)
        self.utclineEdit.setReadOnly(True)

        self.gridLayout_8.addWidget(self.utclineEdit, 8, 1, 1, 1)

        self.utciconlabel = QLabel(self.locframe)
        self.utciconlabel.setObjectName(u"utciconlabel")
        self.utciconlabel.setMinimumSize(QSize(20, 20))
        self.utciconlabel.setMaximumSize(QSize(20, 20))
        self.utciconlabel.setPixmap(QPixmap(u":/icon/icon/utc.png"))
        self.utciconlabel.setScaledContents(True)

        self.gridLayout_8.addWidget(self.utciconlabel, 8, 0, 1, 1)

        self.laticonlabel = QLabel(self.locframe)
        self.laticonlabel.setObjectName(u"laticonlabel")
        self.laticonlabel.setMinimumSize(QSize(20, 20))
        self.laticonlabel.setMaximumSize(QSize(20, 20))
        self.laticonlabel.setFont(font3)
        self.laticonlabel.setPixmap(QPixmap(u":/icon/icon/earth.png"))
        self.laticonlabel.setScaledContents(True)

        self.gridLayout_8.addWidget(self.laticonlabel, 1, 0, 1, 1)

        self.obsiconlabel = QLabel(self.locframe)
        self.obsiconlabel.setObjectName(u"obsiconlabel")
        self.obsiconlabel.setMinimumSize(QSize(20, 20))
        self.obsiconlabel.setMaximumSize(QSize(20, 20))
        self.obsiconlabel.setFont(font3)
        self.obsiconlabel.setPixmap(QPixmap(u":/icon/icon/observatory.png"))
        self.obsiconlabel.setScaledContents(True)

        self.gridLayout_8.addWidget(self.obsiconlabel, 0, 0, 1, 1)

        self.latlineEdit = QLineEdit(self.locframe)
        self.latlineEdit.setObjectName(u"latlineEdit")
        self.latlineEdit.setMinimumSize(QSize(0, 30))
        self.latlineEdit.setMaximumSize(QSize(16777215, 30))
        self.latlineEdit.setFont(font)
        self.latlineEdit.setReadOnly(True)

        self.gridLayout_8.addWidget(self.latlineEdit, 1, 1, 1, 1)

        self.longiconlabel = QLabel(self.locframe)
        self.longiconlabel.setObjectName(u"longiconlabel")
        self.longiconlabel.setMinimumSize(QSize(20, 20))
        self.longiconlabel.setMaximumSize(QSize(20, 20))
        self.longiconlabel.setFont(font3)
        self.longiconlabel.setPixmap(QPixmap(u":/icon/icon/earth.png"))
        self.longiconlabel.setScaledContents(True)

        self.gridLayout_8.addWidget(self.longiconlabel, 2, 0, 1, 1)

        self.tlimitslineEdit = QLineEdit(self.locframe)
        self.tlimitslineEdit.setObjectName(u"tlimitslineEdit")
        self.tlimitslineEdit.setMinimumSize(QSize(0, 30))
        self.tlimitslineEdit.setMaximumSize(QSize(16777215, 30))
        self.tlimitslineEdit.setFont(font)
        self.tlimitslineEdit.setReadOnly(True)

        self.gridLayout_8.addWidget(self.tlimitslineEdit, 7, 1, 1, 1)

        self.elevlineEdit = QLineEdit(self.locframe)
        self.elevlineEdit.setObjectName(u"elevlineEdit")
        self.elevlineEdit.setMinimumSize(QSize(0, 30))
        self.elevlineEdit.setMaximumSize(QSize(16777215, 30))
        self.elevlineEdit.setFont(font)
        self.elevlineEdit.setReadOnly(True)

        self.gridLayout_8.addWidget(self.elevlineEdit, 3, 1, 1, 1)

        self.longlineEdit = QLineEdit(self.locframe)
        self.longlineEdit.setObjectName(u"longlineEdit")
        self.longlineEdit.setMinimumSize(QSize(0, 30))
        self.longlineEdit.setMaximumSize(QSize(16777215, 30))
        self.longlineEdit.setFont(font)
        self.longlineEdit.setReadOnly(True)

        self.gridLayout_8.addWidget(self.longlineEdit, 2, 1, 1, 1)


        self.gridLayout_3.addWidget(self.locframe, 1, 1, 1, 2)

        self.savesetBtn = QPushButton(self.loc_groupBox)
        self.savesetBtn.setObjectName(u"savesetBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.savesetBtn.sizePolicy().hasHeightForWidth())
        self.savesetBtn.setSizePolicy(sizePolicy2)
        self.savesetBtn.setMinimumSize(QSize(110, 30))
        self.savesetBtn.setMaximumSize(QSize(16777215, 30))
        self.savesetBtn.setStyleSheet(u"QPushButton {\n"
"border-radius: 10px;\n"
"background-color:#6316AC;\n"
"color: #eeeeee;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #765cde;\n"
"}\n"
"    \n"
"QPushButton:pressed {\n"
"    background-color: #7e31b5;\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icon/icon/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.savesetBtn.setIcon(icon9)
        self.savesetBtn.setIconSize(QSize(20, 20))

        self.gridLayout_3.addWidget(self.savesetBtn, 2, 2, 1, 1)

        self.setBtn = QPushButton(self.loc_groupBox)
        self.setBtn.setObjectName(u"setBtn")
        sizePolicy2.setHeightForWidth(self.setBtn.sizePolicy().hasHeightForWidth())
        self.setBtn.setSizePolicy(sizePolicy2)
        self.setBtn.setMinimumSize(QSize(110, 30))
        self.setBtn.setMaximumSize(QSize(16777215, 30))
        self.setBtn.setStyleSheet(u"QPushButton {\n"
"border-radius:10px;\n"
"background-color:#6316AC;\n"
"color: #eeeeee;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #765cde;\n"
"}\n"
"    \n"
"QPushButton:pressed {\n"
"    background-color: #7e31b5;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #2d3259;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icon/icon/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.setBtn.setIcon(icon10)
        self.setBtn.setIconSize(QSize(20, 20))

        self.gridLayout_3.addWidget(self.setBtn, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.loc_groupBox)

        self.datetime_groupBox = QGroupBox(self.objvisPage)
        self.datetime_groupBox.setObjectName(u"datetime_groupBox")
        self.datetime_groupBox.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.datetime_groupBox.sizePolicy().hasHeightForWidth())
        self.datetime_groupBox.setSizePolicy(sizePolicy1)
        self.datetime_groupBox.setMinimumSize(QSize(380, 100))
        self.datetime_groupBox.setMaximumSize(QSize(550, 100))
        self.datetime_groupBox.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.datetime_groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(24, -1, 24, -1)
        self.dateiconlabel = QLabel(self.datetime_groupBox)
        self.dateiconlabel.setObjectName(u"dateiconlabel")
        self.dateiconlabel.setMinimumSize(QSize(30, 30))
        self.dateiconlabel.setMaximumSize(QSize(30, 30))
        self.dateiconlabel.setPixmap(QPixmap(u":/icon/icon/date.svg"))
        self.dateiconlabel.setScaledContents(True)

        self.gridLayout_4.addWidget(self.dateiconlabel, 0, 2, 1, 1)

        self.datetextlabel = QLabel(self.datetime_groupBox)
        self.datetextlabel.setObjectName(u"datetextlabel")
        self.datetextlabel.setMinimumSize(QSize(45, 0))
        self.datetextlabel.setMaximumSize(QSize(45, 16777215))
        self.datetextlabel.setFont(font)

        self.gridLayout_4.addWidget(self.datetextlabel, 0, 3, 1, 1)

        self.dateEdit = QDateEdit(self.datetime_groupBox)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(0, 30))
        self.dateEdit.setFont(font2)
        self.dateEdit.setStyleSheet(u"")
        self.dateEdit.setMaximumDateTime(QDateTime(QDate(2050, 12, 31), QTime(23, 59, 59)))
        self.dateEdit.setDate(QDate(2023, 7, 14))

        self.gridLayout_4.addWidget(self.dateEdit, 0, 4, 1, 1)


        self.verticalLayout.addWidget(self.datetime_groupBox)

        self.datetime_groupBox_2 = QGroupBox(self.objvisPage)
        self.datetime_groupBox_2.setObjectName(u"datetime_groupBox_2")
        sizePolicy1.setHeightForWidth(self.datetime_groupBox_2.sizePolicy().hasHeightForWidth())
        self.datetime_groupBox_2.setSizePolicy(sizePolicy1)
        self.datetime_groupBox_2.setMinimumSize(QSize(400, 200))
        self.datetime_groupBox_2.setMaximumSize(QSize(550, 16777215))
        self.datetime_groupBox_2.setStyleSheet(u"QLineEdit {\n"
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
"}")
        self.gridLayout_18 = QGridLayout(self.datetime_groupBox_2)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(24, -1, 24, -1)
        self.reftimelineEdit = QLineEdit(self.datetime_groupBox_2)
        self.reftimelineEdit.setObjectName(u"reftimelineEdit")
        self.reftimelineEdit.setMinimumSize(QSize(0, 30))
        self.reftimelineEdit.setMaximumSize(QSize(16777215, 30))
        self.reftimelineEdit.setFont(font2)
        self.reftimelineEdit.setStyleSheet(u"")
        self.reftimelineEdit.setClearButtonEnabled(True)

        self.gridLayout_18.addWidget(self.reftimelineEdit, 2, 2, 1, 2)

        self.periodlineEdit = QLineEdit(self.datetime_groupBox_2)
        self.periodlineEdit.setObjectName(u"periodlineEdit")
        self.periodlineEdit.setMinimumSize(QSize(0, 30))
        self.periodlineEdit.setMaximumSize(QSize(16777215, 30))
        self.periodlineEdit.setFont(font2)
        self.periodlineEdit.setStyleSheet(u"")
        self.periodlineEdit.setClearButtonEnabled(True)

        self.gridLayout_18.addWidget(self.periodlineEdit, 1, 2, 1, 2)

        self.phrangeiconlabel = QLabel(self.datetime_groupBox_2)
        self.phrangeiconlabel.setObjectName(u"phrangeiconlabel")
        self.phrangeiconlabel.setMinimumSize(QSize(28, 30))
        self.phrangeiconlabel.setMaximumSize(QSize(28, 30))
        self.phrangeiconlabel.setPixmap(QPixmap(u":/icon/icon/range.svg"))
        self.phrangeiconlabel.setScaledContents(True)

        self.gridLayout_18.addWidget(self.phrangeiconlabel, 5, 0, 1, 1)

        self.reftimeiconlabel = QLabel(self.datetime_groupBox_2)
        self.reftimeiconlabel.setObjectName(u"reftimeiconlabel")
        self.reftimeiconlabel.setMinimumSize(QSize(30, 30))
        self.reftimeiconlabel.setMaximumSize(QSize(30, 30))
        self.reftimeiconlabel.setPixmap(QPixmap(u":/icon/icon/reftime.svg"))
        self.reftimeiconlabel.setScaledContents(True)

        self.gridLayout_18.addWidget(self.reftimeiconlabel, 2, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_18.addItem(self.verticalSpacer_4, 0, 3, 1, 1)

        self.reftimetextLabel = QLabel(self.datetime_groupBox_2)
        self.reftimetextLabel.setObjectName(u"reftimetextLabel")
        self.reftimetextLabel.setMinimumSize(QSize(75, 30))
        self.reftimetextLabel.setMaximumSize(QSize(80, 30))
        self.reftimetextLabel.setFont(font)

        self.gridLayout_18.addWidget(self.reftimetextLabel, 2, 1, 1, 1)

        self.periodtextLabel = QLabel(self.datetime_groupBox_2)
        self.periodtextLabel.setObjectName(u"periodtextLabel")
        self.periodtextLabel.setMinimumSize(QSize(75, 30))
        self.periodtextLabel.setMaximumSize(QSize(75, 30))
        self.periodtextLabel.setFont(font)

        self.gridLayout_18.addWidget(self.periodtextLabel, 1, 1, 1, 1)

        self.periodiconlabel = QLabel(self.datetime_groupBox_2)
        self.periodiconlabel.setObjectName(u"periodiconlabel")
        self.periodiconlabel.setMinimumSize(QSize(30, 30))
        self.periodiconlabel.setMaximumSize(QSize(30, 30))
        self.periodiconlabel.setPixmap(QPixmap(u":/icon/icon/period.png"))
        self.periodiconlabel.setScaledContents(True)

        self.gridLayout_18.addWidget(self.periodiconlabel, 1, 0, 1, 1)

        self.phrangeTextLabel = QLabel(self.datetime_groupBox_2)
        self.phrangeTextLabel.setObjectName(u"phrangeTextLabel")
        self.phrangeTextLabel.setMinimumSize(QSize(100, 30))
        self.phrangeTextLabel.setMaximumSize(QSize(75, 30))
        self.phrangeTextLabel.setFont(font)

        self.gridLayout_18.addWidget(self.phrangeTextLabel, 5, 1, 1, 1)

        self.opr_resultlineEdit = QLineEdit(self.datetime_groupBox_2)
        self.opr_resultlineEdit.setObjectName(u"opr_resultlineEdit")
        self.opr_resultlineEdit.setMinimumSize(QSize(0, 30))
        self.opr_resultlineEdit.setMaximumSize(QSize(16777215, 30))
        self.opr_resultlineEdit.setFont(font2)
        self.opr_resultlineEdit.setStyleSheet(u"QLineEdit {\n"
"background: transparent;\n"
"border-radius: 0px;\n"
"border-left: 2px solid #DAF7A6;\n"
"color: #eeeeee;\n"
"font-family:Arial ;\n"
"padding-left: 10px;\n"
"}\n"
"")
        self.opr_resultlineEdit.setReadOnly(True)

        self.gridLayout_18.addWidget(self.opr_resultlineEdit, 5, 2, 1, 2)

        self.phrangeBtnsframe = QFrame(self.datetime_groupBox_2)
        self.phrangeBtnsframe.setObjectName(u"phrangeBtnsframe")
        self.phrangeBtnsframe.setMaximumSize(QSize(16777215, 40))
        self.phrangeBtnsframe.setFrameShape(QFrame.StyledPanel)
        self.phrangeBtnsframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.phrangeBtnsframe)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.oprcalcBtn = QPushButton(self.phrangeBtnsframe)
        self.oprcalcBtn.setObjectName(u"oprcalcBtn")
        self.oprcalcBtn.setMinimumSize(QSize(0, 30))
        self.oprcalcBtn.setStyleSheet(u"QPushButton{\n"
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
        self.oprcalcBtn.setIcon(icon1)
        self.oprcalcBtn.setAutoDefault(True)
        self.oprcalcBtn.setFlat(False)

        self.horizontalLayout_4.addWidget(self.oprcalcBtn)

        self.oprclearBtn = QPushButton(self.phrangeBtnsframe)
        self.oprclearBtn.setObjectName(u"oprclearBtn")
        self.oprclearBtn.setMinimumSize(QSize(0, 30))
        self.oprclearBtn.setStyleSheet(u"QPushButton{\n"
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
        icon11 = QIcon()
        icon11.addFile(u":/icon/icon/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.oprclearBtn.setIcon(icon11)
        self.oprclearBtn.setAutoDefault(True)

        self.horizontalLayout_4.addWidget(self.oprclearBtn)


        self.gridLayout_18.addWidget(self.phrangeBtnsframe, 3, 0, 1, 4)


        self.verticalLayout.addWidget(self.datetime_groupBox_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 4, 1)

        self.sim_ms_groupBox = QGroupBox(self.objvisPage)
        self.sim_ms_groupBox.setObjectName(u"sim_ms_groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sim_ms_groupBox.sizePolicy().hasHeightForWidth())
        self.sim_ms_groupBox.setSizePolicy(sizePolicy3)
        self.sim_ms_groupBox.setMinimumSize(QSize(372, 0))
        self.sim_ms_groupBox.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.sim_ms_groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 6, 15, 6)
        self.ms_simframe = QFrame(self.sim_ms_groupBox)
        self.ms_simframe.setObjectName(u"ms_simframe")
        self.ms_simframe.setFrameShape(QFrame.StyledPanel)
        self.ms_simframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.ms_simframe)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.simbadframe = QFrame(self.ms_simframe)
        self.simbadframe.setObjectName(u"simbadframe")
        self.simbadframe.setFrameShape(QFrame.StyledPanel)
        self.simbadframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.simbadframe)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.simbadlabel = QLabel(self.simbadframe)
        self.simbadlabel.setObjectName(u"simbadlabel")
        self.simbadlabel.setMinimumSize(QSize(120, 60))
        self.simbadlabel.setMaximumSize(QSize(120, 60))
        self.simbadlabel.setPixmap(QPixmap(u":/icon/icon/simbad.png"))
        self.simbadlabel.setScaledContents(True)

        self.gridLayout_15.addWidget(self.simbadlabel, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.simbadframe)

        self.ms_qregframe = QFrame(self.ms_simframe)
        self.ms_qregframe.setObjectName(u"ms_qregframe")
        self.ms_qregframe.setMinimumSize(QSize(0, 35))
        self.ms_qregframe.setMaximumSize(QSize(16777215, 16777215))
        self.ms_qregframe.setFrameShape(QFrame.StyledPanel)
        self.ms_qregframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.ms_qregframe)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.ms_querylabel = QLabel(self.ms_qregframe)
        self.ms_querylabel.setObjectName(u"ms_querylabel")
        self.ms_querylabel.setMinimumSize(QSize(80, 30))
        self.ms_querylabel.setMaximumSize(QSize(80, 30))

        self.gridLayout_28.addWidget(self.ms_querylabel, 0, 1, 1, 1)

        self.ms_queryiconlabel = QLabel(self.ms_qregframe)
        self.ms_queryiconlabel.setObjectName(u"ms_queryiconlabel")
        self.ms_queryiconlabel.setMinimumSize(QSize(25, 25))
        self.ms_queryiconlabel.setMaximumSize(QSize(25, 25))
        self.ms_queryiconlabel.setPixmap(QPixmap(u":/icon/icon/region.svg"))
        self.ms_queryiconlabel.setScaledContents(True)

        self.gridLayout_28.addWidget(self.ms_queryiconlabel, 0, 0, 1, 1)

        self.ms_qregion_comboBox = QComboBox(self.ms_qregframe)
        self.ms_qregion_comboBox.addItem("")
        self.ms_qregion_comboBox.addItem("")
        self.ms_qregion_comboBox.setObjectName(u"ms_qregion_comboBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ms_qregion_comboBox.sizePolicy().hasHeightForWidth())
        self.ms_qregion_comboBox.setSizePolicy(sizePolicy4)
        self.ms_qregion_comboBox.setMinimumSize(QSize(80, 30))
        self.ms_qregion_comboBox.setMaximumSize(QSize(16777215, 30))
        self.ms_qregion_comboBox.setFont(font)

        self.gridLayout_28.addWidget(self.ms_qregion_comboBox, 0, 3, 1, 1)

        self.ms_spinBox = QSpinBox(self.ms_qregframe)
        self.ms_spinBox.setObjectName(u"ms_spinBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.ms_spinBox.sizePolicy().hasHeightForWidth())
        self.ms_spinBox.setSizePolicy(sizePolicy5)
        self.ms_spinBox.setMinimumSize(QSize(0, 30))
        self.ms_spinBox.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(10)
        self.ms_spinBox.setFont(font4)
        self.ms_spinBox.setMinimum(5)
        self.ms_spinBox.setMaximum(59)

        self.gridLayout_28.addWidget(self.ms_spinBox, 0, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.ms_qregframe)

        self.sim_ms_lineEdit = QLineEdit(self.ms_simframe)
        self.sim_ms_lineEdit.setObjectName(u"sim_ms_lineEdit")
        self.sim_ms_lineEdit.setMinimumSize(QSize(0, 30))
        self.sim_ms_lineEdit.setStyleSheet(u"QLineEdit {\n"
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
"}")
        self.sim_ms_lineEdit.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.sim_ms_lineEdit)

        self.sim_buttons_frame = QFrame(self.ms_simframe)
        self.sim_buttons_frame.setObjectName(u"sim_buttons_frame")
        self.sim_buttons_frame.setMinimumSize(QSize(0, 30))
        self.sim_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.sim_buttons_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.sim_buttons_frame)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.sim_ms_searchBtn = QPushButton(self.sim_buttons_frame)
        self.sim_ms_searchBtn.setObjectName(u"sim_ms_searchBtn")
        self.sim_ms_searchBtn.setMinimumSize(QSize(0, 30))
        self.sim_ms_searchBtn.setMaximumSize(QSize(16777215, 16777215))
        self.sim_ms_searchBtn.setStyleSheet(u"QPushButton{\n"
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
        self.sim_ms_searchBtn.setIcon(icon2)
        self.sim_ms_searchBtn.setAutoDefault(True)

        self.gridLayout_26.addWidget(self.sim_ms_searchBtn, 0, 0, 1, 1)

        self.sim_ms_clearBtn = QPushButton(self.sim_buttons_frame)
        self.sim_ms_clearBtn.setObjectName(u"sim_ms_clearBtn")
        self.sim_ms_clearBtn.setMinimumSize(QSize(0, 30))
        self.sim_ms_clearBtn.setStyleSheet(u"QPushButton{\n"
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
        self.sim_ms_clearBtn.setIcon(icon11)
        self.sim_ms_clearBtn.setAutoDefault(True)

        self.gridLayout_26.addWidget(self.sim_ms_clearBtn, 0, 2, 1, 1)

        self.addBtn = QPushButton(self.sim_buttons_frame)
        self.addBtn.setObjectName(u"addBtn")
        self.addBtn.setMinimumSize(QSize(0, 30))
        self.addBtn.setMaximumSize(QSize(16777215, 16777215))
        self.addBtn.setStyleSheet(u"QPushButton{\n"
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
        icon12 = QIcon()
        icon12.addFile(u":/icon/icon/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addBtn.setIcon(icon12)
        self.addBtn.setAutoDefault(True)

        self.gridLayout_26.addWidget(self.addBtn, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.sim_buttons_frame)

        self.sim_ms_textEdit = QTextEdit(self.ms_simframe)
        self.sim_ms_textEdit.setObjectName(u"sim_ms_textEdit")
        self.sim_ms_textEdit.setStyleSheet(u"#sim_ms_textEdit {\n"
"background: #2d3259;\n"
"border-radius: 15px;\n"
"padding: 10px;\n"
"font-size: 9pt;\n"
"color: #eeeeee;\n"
"}")
        self.sim_ms_textEdit.setInputMethodHints(Qt.ImhMultiLine)
        self.sim_ms_textEdit.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_2.addWidget(self.sim_ms_textEdit)


        self.verticalLayout_3.addWidget(self.ms_simframe)


        self.gridLayout.addWidget(self.sim_ms_groupBox, 3, 1, 1, 1)

        self.coord_groupBox = QGroupBox(self.objvisPage)
        self.coord_groupBox.setObjectName(u"coord_groupBox")
        sizePolicy1.setHeightForWidth(self.coord_groupBox.sizePolicy().hasHeightForWidth())
        self.coord_groupBox.setSizePolicy(sizePolicy1)
        self.coord_groupBox.setMinimumSize(QSize(372, 300))
        self.coord_groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.coord_groupBox.setStyleSheet(u"")
        self.gridLayout_5 = QGridLayout(self.coord_groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(15, -1, 15, -1)
        self.frame_2 = QFrame(self.coord_groupBox)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(330, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton.setIcon(icon1)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.clearBtn = QPushButton(self.frame_2)
        self.clearBtn.setObjectName(u"clearBtn")
        self.clearBtn.setMinimumSize(QSize(0, 30))
        self.clearBtn.setStyleSheet(u"QPushButton{\n"
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
        self.clearBtn.setIcon(icon11)
        self.clearBtn.setAutoDefault(True)

        self.horizontalLayout_2.addWidget(self.clearBtn)

        self.graphsetBtn = QPushButton(self.frame_2)
        self.graphsetBtn.setObjectName(u"graphsetBtn")
        self.graphsetBtn.setMinimumSize(QSize(30, 30))
        self.graphsetBtn.setMaximumSize(QSize(30, 30))
        self.graphsetBtn.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 0, 127) ;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #fe4c4f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FF6638;\n"
"}\n"
"")
        self.graphsetBtn.setIcon(icon10)
        self.graphsetBtn.setAutoDefault(True)

        self.horizontalLayout_2.addWidget(self.graphsetBtn)


        self.gridLayout_5.addWidget(self.frame_2, 4, 0, 1, 1)

        self.starwidget = QWidget(self.coord_groupBox)
        self.starwidget.setObjectName(u"starwidget")
        self.starwidget.setMinimumSize(QSize(0, 40))
        self.starwidget.setStyleSheet(u"QRadioButton{\n"
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
        self.horizontalLayout = QHBoxLayout(self.starwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.staralt_radioButton = QRadioButton(self.starwidget)
        self.staralt_radioButton.setObjectName(u"staralt_radioButton")
        self.staralt_radioButton.setMinimumSize(QSize(0, 30))
        self.staralt_radioButton.setFont(font)
        self.staralt_radioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.staralt_radioButton, 0, Qt.AlignVCenter)

        self.starobs_radioButton = QRadioButton(self.starwidget)
        self.starobs_radioButton.setObjectName(u"starobs_radioButton")
        self.starobs_radioButton.setMinimumSize(QSize(0, 30))
        self.starobs_radioButton.setFont(font)

        self.horizontalLayout.addWidget(self.starobs_radioButton, 0, Qt.AlignTop)


        self.gridLayout_5.addWidget(self.starwidget, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.coord_groupBox)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit.setFont(font2)
        self.plainTextEdit.setStyleSheet(u"#plainTextEdit {\n"
"background: #2d3259;\n"
"border-radius: 15px;\n"
"padding: 5px;\n"
"color:#eeeeee\n"
"}")
        self.plainTextEdit.setInputMethodHints(Qt.ImhMultiLine)

        self.gridLayout_5.addWidget(self.plainTextEdit, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.coord_groupBox, 0, 1, 3, 1)

        self.pages.addWidget(self.objvisPage)
        self.simdataPage = QWidget()
        self.simdataPage.setObjectName(u"simdataPage")
        self.simdataPage.setStyleSheet(u"QTableView {\n"
"background: #2d3259;\n"
"gridline-color:black;\n"
"border-radius: 15px;\n"
"border-color: #000000;\n"
"padding: 10px;\n"
"font-size: 9pt;\n"
"color: #eeeeee;\n"
"}\n"
"\n"
"QTableView::item \n"
"        {   \n"
"            color: white;\n"
"            background:black;            \n"
"        }\n"
" QTableView::item:hover\n"
"        {   \n"
"            color: black;\n"
"            background:#ffaa00;            \n"
"        }\n"
" QTableView::item:focus\n"
"        {   \n"
"            color: #eeeeee;\n"
"            background:#6316AC;            \n"
"        }\n"
"\n"
"\n"
"QHeaderView::section {\n"
"\n"
"color:white; \n"
"background-color:#232326 ;\n"
"border: none;\n"
"border-style:none;\n"
"\n"
" }\n"
" QHeaderView {\n"
"    background: #2d3259;\n"
"\n"
"}\n"
"\n"
"QTableCornerButton::section { \n"
"background-color:#232326; \n"
"border-top-left-radius: 10px;\n"
"}\n"
"\n"
"")
        self.gridLayout_12 = QGridLayout(self.simdataPage)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(6, 6, 6, 6)
        self.simframe = QFrame(self.simdataPage)
        self.simframe.setObjectName(u"simframe")
        font5 = QFont()
        font5.setFamilies([u"Candara"])
        font5.setBold(True)
        self.simframe.setFont(font5)
        self.simframe.setStyleSheet(u"#simframe{\n"
"background-color: #1c1c27;\n"
"border-radius: 15px;\n"
"}")
        self.simframe.setFrameShape(QFrame.StyledPanel)
        self.simframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.simframe)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.qregframe = QFrame(self.simframe)
        self.qregframe.setObjectName(u"qregframe")
        self.qregframe.setMinimumSize(QSize(0, 30))
        self.qregframe.setMaximumSize(QSize(16777215, 200))
        self.qregframe.setFrameShape(QFrame.StyledPanel)
        self.qregframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.qregframe)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 6, 0, 6)
        self.querylabel = QLabel(self.qregframe)
        self.querylabel.setObjectName(u"querylabel")
        self.querylabel.setMinimumSize(QSize(100, 30))
        self.querylabel.setMaximumSize(QSize(100, 30))

        self.gridLayout_29.addWidget(self.querylabel, 0, 1, 1, 1)

        self.label_2 = QLabel(self.qregframe)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(25, 25))
        self.label_2.setMaximumSize(QSize(25, 25))
        self.label_2.setPixmap(QPixmap(u":/icon/icon/index.svg"))

        self.gridLayout_29.addWidget(self.label_2, 2, 0, 1, 1)

        self.queryiconlabel = QLabel(self.qregframe)
        self.queryiconlabel.setObjectName(u"queryiconlabel")
        self.queryiconlabel.setMinimumSize(QSize(25, 25))
        self.queryiconlabel.setMaximumSize(QSize(25, 25))
        self.queryiconlabel.setPixmap(QPixmap(u":/icon/icon/region.svg"))
        self.queryiconlabel.setScaledContents(True)

        self.gridLayout_29.addWidget(self.queryiconlabel, 0, 0, 1, 1)

        self.sim_lineEdit = QLineEdit(self.qregframe)
        self.sim_lineEdit.setObjectName(u"sim_lineEdit")
        self.sim_lineEdit.setMinimumSize(QSize(0, 30))
        self.sim_lineEdit.setStyleSheet(u"QLineEdit {\n"
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
"}")
        self.sim_lineEdit.setClearButtonEnabled(True)

        self.gridLayout_29.addWidget(self.sim_lineEdit, 2, 2, 1, 5)

        self.label = QLabel(self.qregframe)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))
        self.label.setMaximumSize(QSize(100, 16777215))
        self.label.setStyleSheet(u"QLabel {\n"
"color: #eeeeee;\n"
"\n"
"}")

        self.gridLayout_29.addWidget(self.label, 2, 1, 1, 1)

        self.qregion_comboBox = QComboBox(self.qregframe)
        self.qregion_comboBox.addItem("")
        self.qregion_comboBox.addItem("")
        self.qregion_comboBox.addItem("")
        self.qregion_comboBox.setObjectName(u"qregion_comboBox")
        sizePolicy4.setHeightForWidth(self.qregion_comboBox.sizePolicy().hasHeightForWidth())
        self.qregion_comboBox.setSizePolicy(sizePolicy4)
        self.qregion_comboBox.setMinimumSize(QSize(80, 30))
        self.qregion_comboBox.setMaximumSize(QSize(16777215, 30))
        self.qregion_comboBox.setFont(font)

        self.gridLayout_29.addWidget(self.qregion_comboBox, 0, 6, 1, 1)

        self.qregion_dspinBox = QDoubleSpinBox(self.qregframe)
        self.qregion_dspinBox.setObjectName(u"qregion_dspinBox")
        self.qregion_dspinBox.setMinimumSize(QSize(850, 30))
        self.qregion_dspinBox.setMaximumSize(QSize(16777215, 30))
        self.qregion_dspinBox.setFont(font2)
        self.qregion_dspinBox.setDecimals(3)
        self.qregion_dspinBox.setMaximum(59.999000000000002)
        self.qregion_dspinBox.setSingleStep(0.100000000000000)
        self.qregion_dspinBox.setValue(11.840000000000000)

        self.gridLayout_29.addWidget(self.qregion_dspinBox, 0, 2, 1, 4)


        self.gridLayout_9.addWidget(self.qregframe, 1, 0, 1, 2)

        self.frame_5 = QFrame(self.simframe)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 200))
        self.frame_5.setMaximumSize(QSize(16777215, 200))
        self.frame_5.setStyleSheet(u"QRadioButton{\n"
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
"}\n"
"\n"
"QCheckBox{\n"
"color: #eeeeee;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_5)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setHorizontalSpacing(10)
        self.gaia_frame_cat = QFrame(self.frame_5)
        self.gaia_frame_cat.setObjectName(u"gaia_frame_cat")
        self.gaia_frame_cat.setStyleSheet(u"#gaia_frame_cat {\n"
"border: 2px solid #524eee;\n"
"border-radius: 15px;\n"
"\n"
"}")
        self.gaia_frame_cat.setFrameShape(QFrame.StyledPanel)
        self.gaia_frame_cat.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.gaia_frame_cat)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gaialabel_2 = QLabel(self.gaia_frame_cat)
        self.gaialabel_2.setObjectName(u"gaialabel_2")
        self.gaialabel_2.setMinimumSize(QSize(40, 40))
        self.gaialabel_2.setMaximumSize(QSize(40, 40))
        self.gaialabel_2.setPixmap(QPixmap(u":/icon/icon/Logo_Gaia.png"))
        self.gaialabel_2.setScaledContents(True)

        self.gridLayout_35.addWidget(self.gaialabel_2, 0, 0, 1, 1, Qt.AlignHCenter)

        self.gaia_checkBox = QCheckBox(self.gaia_frame_cat)
        self.gaia_checkBox.setObjectName(u"gaia_checkBox")
        self.gaia_checkBox.setMinimumSize(QSize(0, 20))
        self.gaia_checkBox.setMaximumSize(QSize(16777215, 20))
        self.gaia_checkBox.setFont(font)

        self.gridLayout_35.addWidget(self.gaia_checkBox, 1, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_31.addWidget(self.gaia_frame_cat, 0, 4, 1, 1)

        self.simbad_frame_cat = QFrame(self.frame_5)
        self.simbad_frame_cat.setObjectName(u"simbad_frame_cat")
        self.simbad_frame_cat.setStyleSheet(u"#simbad_frame_cat{\n"
"border: 2px solid #524eee;\n"
"border-radius: 15px;\n"
"\n"
"}")
        self.simbad_frame_cat.setFrameShape(QFrame.StyledPanel)
        self.simbad_frame_cat.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.simbad_frame_cat)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_32.addItem(self.verticalSpacer_10, 2, 0, 1, 1)

        self.simtype_combobox = QComboBox(self.simbad_frame_cat)
        self.simtype_combobox.addItem("")
        self.simtype_combobox.addItem("")
        self.simtype_combobox.setObjectName(u"simtype_combobox")
        self.simtype_combobox.setMinimumSize(QSize(80, 0))
        self.simtype_combobox.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_32.addWidget(self.simtype_combobox, 4, 0, 1, 1, Qt.AlignHCenter)

        self.simlabel_2 = QLabel(self.simbad_frame_cat)
        self.simlabel_2.setObjectName(u"simlabel_2")
        self.simlabel_2.setMinimumSize(QSize(80, 40))
        self.simlabel_2.setMaximumSize(QSize(80, 40))
        self.simlabel_2.setPixmap(QPixmap(u":/icon/icon/simbad.png"))
        self.simlabel_2.setScaledContents(True)

        self.gridLayout_32.addWidget(self.simlabel_2, 1, 0, 1, 1, Qt.AlignHCenter)

        self.simbad_checkBox = QCheckBox(self.simbad_frame_cat)
        self.simbad_checkBox.setObjectName(u"simbad_checkBox")
        self.simbad_checkBox.setMinimumSize(QSize(0, 20))
        self.simbad_checkBox.setMaximumSize(QSize(16777215, 20))
        self.simbad_checkBox.setFont(font)
        self.simbad_checkBox.setChecked(True)

        self.gridLayout_32.addWidget(self.simbad_checkBox, 3, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_32.addItem(self.verticalSpacer_11, 0, 0, 1, 1)


        self.gridLayout_31.addWidget(self.simbad_frame_cat, 0, 0, 1, 1)

        self.tmass_frame_cat = QFrame(self.frame_5)
        self.tmass_frame_cat.setObjectName(u"tmass_frame_cat")
        self.tmass_frame_cat.setStyleSheet(u"#tmass_frame_cat {\n"
"border: 2px solid #524eee;\n"
"border-radius: 15px;\n"
"\n"
"}")
        self.tmass_frame_cat.setFrameShape(QFrame.StyledPanel)
        self.tmass_frame_cat.setFrameShadow(QFrame.Raised)
        self.gridLayout_33 = QGridLayout(self.tmass_frame_cat)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.irsa_checkBox = QCheckBox(self.tmass_frame_cat)
        self.irsa_checkBox.setObjectName(u"irsa_checkBox")
        self.irsa_checkBox.setMinimumSize(QSize(0, 20))
        self.irsa_checkBox.setFont(font)

        self.gridLayout_33.addWidget(self.irsa_checkBox, 1, 0, 1, 2)

        self.twomasslabel_2 = QLabel(self.tmass_frame_cat)
        self.twomasslabel_2.setObjectName(u"twomasslabel_2")
        self.twomasslabel_2.setMinimumSize(QSize(80, 40))
        self.twomasslabel_2.setMaximumSize(QSize(80, 40))
        self.twomasslabel_2.setPixmap(QPixmap(u":/icon/icon/2mass.png"))
        self.twomasslabel_2.setScaledContents(True)

        self.gridLayout_33.addWidget(self.twomasslabel_2, 0, 1, 1, 1)

        self.irsalabel_2 = QLabel(self.tmass_frame_cat)
        self.irsalabel_2.setObjectName(u"irsalabel_2")
        self.irsalabel_2.setMinimumSize(QSize(80, 40))
        self.irsalabel_2.setMaximumSize(QSize(80, 40))
        self.irsalabel_2.setPixmap(QPixmap(u":/icon/icon/irsa.png"))
        self.irsalabel_2.setScaledContents(True)

        self.gridLayout_33.addWidget(self.irsalabel_2, 0, 0, 1, 1)


        self.gridLayout_31.addWidget(self.tmass_frame_cat, 0, 1, 1, 1)

        self.wise_frame_cat = QFrame(self.frame_5)
        self.wise_frame_cat.setObjectName(u"wise_frame_cat")
        self.wise_frame_cat.setStyleSheet(u"#wise_frame_cat {\n"
"border: 2px solid#524eee;\n"
"border-radius: 15px;\n"
"\n"
"}")
        self.wise_frame_cat.setFrameShape(QFrame.StyledPanel)
        self.wise_frame_cat.setFrameShadow(QFrame.Raised)
        self.gridLayout_34 = QGridLayout(self.wise_frame_cat)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.irsalabel_3 = QLabel(self.wise_frame_cat)
        self.irsalabel_3.setObjectName(u"irsalabel_3")
        self.irsalabel_3.setMinimumSize(QSize(80, 40))
        self.irsalabel_3.setMaximumSize(QSize(80, 40))
        self.irsalabel_3.setPixmap(QPixmap(u":/icon/icon/irsa.png"))
        self.irsalabel_3.setScaledContents(True)

        self.gridLayout_34.addWidget(self.irsalabel_3, 0, 0, 1, 1)

        self.irsalabel_4 = QLabel(self.wise_frame_cat)
        self.irsalabel_4.setObjectName(u"irsalabel_4")
        self.irsalabel_4.setMinimumSize(QSize(80, 40))
        self.irsalabel_4.setMaximumSize(QSize(80, 40))
        self.irsalabel_4.setPixmap(QPixmap(u":/icon/icon/WISE_logo.png"))
        self.irsalabel_4.setScaledContents(True)

        self.gridLayout_34.addWidget(self.irsalabel_4, 0, 1, 1, 1)

        self.wise_checkBox = QCheckBox(self.wise_frame_cat)
        self.wise_checkBox.setObjectName(u"wise_checkBox")
        self.wise_checkBox.setMinimumSize(QSize(0, 20))
        self.wise_checkBox.setMaximumSize(QSize(16777215, 20))
        self.wise_checkBox.setFont(font)

        self.gridLayout_34.addWidget(self.wise_checkBox, 1, 0, 1, 2)


        self.gridLayout_31.addWidget(self.wise_frame_cat, 0, 3, 1, 1)

        self.ztf_frame_cat = QFrame(self.frame_5)
        self.ztf_frame_cat.setObjectName(u"ztf_frame_cat")
        self.ztf_frame_cat.setStyleSheet(u"#ztf_frame_cat {\n"
"border: 2px solid #524eee;\n"
"border-radius: 15px;\n"
"\n"
"}")
        self.ztf_frame_cat.setFrameShape(QFrame.StyledPanel)
        self.ztf_frame_cat.setFrameShadow(QFrame.Raised)
        self.gridLayout_36 = QGridLayout(self.ztf_frame_cat)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.ztflabel_2 = QLabel(self.ztf_frame_cat)
        self.ztflabel_2.setObjectName(u"ztflabel_2")
        self.ztflabel_2.setMinimumSize(QSize(65, 40))
        self.ztflabel_2.setMaximumSize(QSize(65, 40))
        self.ztflabel_2.setPixmap(QPixmap(u":/icon/icon/ztf_logo.png"))
        self.ztflabel_2.setScaledContents(True)

        self.gridLayout_36.addWidget(self.ztflabel_2, 0, 0, 1, 1, Qt.AlignHCenter)

        self.ztf_checkBox = QCheckBox(self.ztf_frame_cat)
        self.ztf_checkBox.setObjectName(u"ztf_checkBox")
        self.ztf_checkBox.setMinimumSize(QSize(0, 20))
        self.ztf_checkBox.setMaximumSize(QSize(16777215, 20))
        self.ztf_checkBox.setFont(font)

        self.gridLayout_36.addWidget(self.ztf_checkBox, 1, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_31.addWidget(self.ztf_frame_cat, 0, 5, 1, 1)


        self.gridLayout_9.addWidget(self.frame_5, 3, 0, 1, 2)

        self.frame_3 = QFrame(self.simframe)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(200, 60))
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"background-color:  #6316AC;\n"
"border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #765cde;\n"
"}\n"
"    \n"
"QPushButton:pressed {\n"
"    background-color: #7e31b5;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_3)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 6, 0, 6)
        self.searchBtn = QPushButton(self.frame_3)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setMinimumSize(QSize(0, 40))
        self.searchBtn.setMaximumSize(QSize(16777215, 16777215))
        self.searchBtn.setStyleSheet(u"")
        self.searchBtn.setIcon(icon2)
        self.searchBtn.setAutoDefault(True)

        self.gridLayout_30.addWidget(self.searchBtn, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame_3, 4, 0, 1, 2)

        self.label_3 = QLabel(self.simframe)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 200))
        self.label_3.setMaximumSize(QSize(16777215, 200))
        font6 = QFont()
        font6.setFamilies([u"Bahnschrift Light Condensed"])
        font6.setBold(False)
        font6.setItalic(False)
        self.label_3.setFont(font6)
        self.label_3.setStyleSheet(u"QLabel{\n"
"background-image : url(:/icon/icon/catalog.png);\n"
"border-radius: 30px;\n"
"}")
        self.label_3.setTextFormat(Qt.RichText)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(False)
        self.label_3.setIndent(-1)

        self.gridLayout_9.addWidget(self.label_3, 0, 0, 1, 2)


        self.gridLayout_12.addWidget(self.simframe, 0, 0, 1, 1)

        self.pages.addWidget(self.simdataPage)
        self.convPage = QWidget()
        self.convPage.setObjectName(u"convPage")
        self.convPage.setStyleSheet(u"QTextEdit {\n"
"background: #2d3259;\n"
"border-radius: 15px;\n"
"padding: 10px;\n"
"font-size: 9pt;\n"
"color: #eeeeee;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:  #6316AC;\n"
"border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #765cde;\n"
"}\n"
"    \n"
"QPushButton:pressed {\n"
"    background-color: #7e31b5;\n"
"}")
        self.gridLayout_16 = QGridLayout(self.convPage)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(6, 6, 6, 6)
        self.groupBox_conv = QGroupBox(self.convPage)
        self.groupBox_conv.setObjectName(u"groupBox_conv")
        self.groupBox_conv.setStyleSheet(u"#groupBox_conv {\n"
"background-color: #1c1c27;\n"
"border-radius: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#groupBox_conv::title {\n"
"                subcontrol-origin: margin;\n"
"                subcontrol-position: top center;    /* position at the top center */\n"
"                padding: 10px;\n"
"}")
        self.gridLayout_13 = QGridLayout(self.groupBox_conv)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.conv_spinbox_deg = QSpinBox(self.groupBox_conv)
        self.conv_spinbox_deg.setObjectName(u"conv_spinbox_deg")
        self.conv_spinbox_deg.setMinimumSize(QSize(0, 30))
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(11)
        font7.setBold(False)
        self.conv_spinbox_deg.setFont(font7)
        self.conv_spinbox_deg.setMinimum(0)
        self.conv_spinbox_deg.setMaximum(180)
        self.conv_spinbox_deg.setValue(39)

        self.gridLayout_13.addWidget(self.conv_spinbox_deg, 1, 0, 1, 1)

        self.convd_seclabel = QLabel(self.groupBox_conv)
        self.convd_seclabel.setObjectName(u"convd_seclabel")
        self.convd_seclabel.setMaximumSize(QSize(10, 16777215))

        self.gridLayout_13.addWidget(self.convd_seclabel, 1, 5, 1, 1)

        self.conv_spinbox_min = QSpinBox(self.groupBox_conv)
        self.conv_spinbox_min.setObjectName(u"conv_spinbox_min")
        self.conv_spinbox_min.setMinimumSize(QSize(0, 30))
        self.conv_spinbox_min.setFont(font2)
        self.conv_spinbox_min.setMaximum(59)
        self.conv_spinbox_min.setValue(50)

        self.gridLayout_13.addWidget(self.conv_spinbox_min, 1, 2, 1, 1)

        self.convd_deglabel = QLabel(self.groupBox_conv)
        self.convd_deglabel.setObjectName(u"convd_deglabel")
        self.convd_deglabel.setMaximumSize(QSize(10, 16777215))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        font8.setPointSize(12)
        self.convd_deglabel.setFont(font8)

        self.gridLayout_13.addWidget(self.convd_deglabel, 1, 1, 1, 1)

        self.convd_minlabel = QLabel(self.groupBox_conv)
        self.convd_minlabel.setObjectName(u"convd_minlabel")
        self.convd_minlabel.setMaximumSize(QSize(10, 16777215))

        self.gridLayout_13.addWidget(self.convd_minlabel, 1, 3, 1, 1)

        self.conv_dspinbox_sec = QDoubleSpinBox(self.groupBox_conv)
        self.conv_dspinbox_sec.setObjectName(u"conv_dspinbox_sec")
        self.conv_dspinbox_sec.setMinimumSize(QSize(0, 30))
        self.conv_dspinbox_sec.setFont(font2)
        self.conv_dspinbox_sec.setMaximum(59.990000000000002)
        self.conv_dspinbox_sec.setValue(37.000000000000000)

        self.gridLayout_13.addWidget(self.conv_dspinbox_sec, 1, 4, 1, 1)

        self.conv_pushButton = QPushButton(self.groupBox_conv)
        self.conv_pushButton.setObjectName(u"conv_pushButton")
        self.conv_pushButton.setMinimumSize(QSize(0, 40))
        self.conv_pushButton.setStyleSheet(u"")
        self.conv_pushButton.setIcon(icon3)

        self.gridLayout_13.addWidget(self.conv_pushButton, 2, 0, 1, 6)

        self.verticalSpacer_5 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_13.addItem(self.verticalSpacer_5, 0, 2, 1, 1)

        self.conv_textEdit = QTextEdit(self.groupBox_conv)
        self.conv_textEdit.setObjectName(u"conv_textEdit")
        font9 = QFont()
        font9.setPointSize(9)
        self.conv_textEdit.setFont(font9)
        self.conv_textEdit.setStyleSheet(u"")
        self.conv_textEdit.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout_13.addWidget(self.conv_textEdit, 3, 0, 1, 6)


        self.gridLayout_16.addWidget(self.groupBox_conv, 0, 0, 1, 1)

        self.groupBox_conv_2 = QGroupBox(self.convPage)
        self.groupBox_conv_2.setObjectName(u"groupBox_conv_2")
        self.groupBox_conv_2.setStyleSheet(u"#groupBox_conv_2 {\n"
"background-color: #1c1c27;\n"
"border-radius: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#groupBox_conv_2::title {\n"
"                subcontrol-origin: margin;\n"
"                subcontrol-position: top center;    /* position at the top center */\n"
"                padding: 10px;\n"
"}")
        self.gridLayout_14 = QGridLayout(self.groupBox_conv_2)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.conv_textEdit_2 = QTextEdit(self.groupBox_conv_2)
        self.conv_textEdit_2.setObjectName(u"conv_textEdit_2")
        self.conv_textEdit_2.setFont(font9)
        self.conv_textEdit_2.setStyleSheet(u"")
        self.conv_textEdit_2.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout_14.addWidget(self.conv_textEdit_2, 3, 0, 1, 6)

        self.verticalSpacer_6 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_14.addItem(self.verticalSpacer_6, 0, 2, 1, 1)

        self.conv_spinbox_hour = QSpinBox(self.groupBox_conv_2)
        self.conv_spinbox_hour.setObjectName(u"conv_spinbox_hour")
        self.conv_spinbox_hour.setMinimumSize(QSize(0, 30))
        self.conv_spinbox_hour.setFont(font2)
        self.conv_spinbox_hour.setMaximum(24)
        self.conv_spinbox_hour.setValue(2)

        self.gridLayout_14.addWidget(self.conv_spinbox_hour, 1, 0, 1, 1)

        self.convh_hourlabel = QLabel(self.groupBox_conv_2)
        self.convh_hourlabel.setObjectName(u"convh_hourlabel")
        self.convh_hourlabel.setMaximumSize(QSize(10, 16777215))
        self.convh_hourlabel.setFont(font8)

        self.gridLayout_14.addWidget(self.convh_hourlabel, 1, 1, 1, 1)

        self.conv_dspinbox_sec_2 = QDoubleSpinBox(self.groupBox_conv_2)
        self.conv_dspinbox_sec_2.setObjectName(u"conv_dspinbox_sec_2")
        self.conv_dspinbox_sec_2.setMinimumSize(QSize(0, 30))
        self.conv_dspinbox_sec_2.setFont(font2)
        self.conv_dspinbox_sec_2.setMaximum(59.990000000000002)
        self.conv_dspinbox_sec_2.setValue(7.000000000000000)

        self.gridLayout_14.addWidget(self.conv_dspinbox_sec_2, 1, 4, 1, 1)

        self.convh_seclabel = QLabel(self.groupBox_conv_2)
        self.convh_seclabel.setObjectName(u"convh_seclabel")
        self.convh_seclabel.setMaximumSize(QSize(10, 16777215))

        self.gridLayout_14.addWidget(self.convh_seclabel, 1, 5, 1, 1)

        self.conv_spinbox_min_2 = QSpinBox(self.groupBox_conv_2)
        self.conv_spinbox_min_2.setObjectName(u"conv_spinbox_min_2")
        self.conv_spinbox_min_2.setMinimumSize(QSize(0, 30))
        self.conv_spinbox_min_2.setFont(font2)
        self.conv_spinbox_min_2.setMaximum(59)
        self.conv_spinbox_min_2.setValue(11)

        self.gridLayout_14.addWidget(self.conv_spinbox_min_2, 1, 2, 1, 1)

        self.convh_minlabel = QLabel(self.groupBox_conv_2)
        self.convh_minlabel.setObjectName(u"convh_minlabel")
        self.convh_minlabel.setMaximumSize(QSize(10, 16777215))

        self.gridLayout_14.addWidget(self.convh_minlabel, 1, 3, 1, 1)

        self.conv_pushButton_2 = QPushButton(self.groupBox_conv_2)
        self.conv_pushButton_2.setObjectName(u"conv_pushButton_2")
        self.conv_pushButton_2.setMinimumSize(QSize(0, 40))
        self.conv_pushButton_2.setStyleSheet(u"")
        self.conv_pushButton_2.setIcon(icon3)

        self.gridLayout_14.addWidget(self.conv_pushButton_2, 2, 0, 1, 6)


        self.gridLayout_16.addWidget(self.groupBox_conv_2, 0, 1, 1, 1)

        self.pages.addWidget(self.convPage)
        self.infoPage = QWidget()
        self.infoPage.setObjectName(u"infoPage")
        self.gridLayout_17 = QGridLayout(self.infoPage)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(6, 6, 6, 6)
        self.frame_9 = QFrame(self.infoPage)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(750, 0))
        self.frame_9.setMaximumSize(QSize(16777215, 16777215))
        self.frame_9.setStyleSheet(u"#frame_9{\n"
"border:3px solid #2A363B;\n"
"border-radius: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.frame_9.setFrameShape(QFrame.Box)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_9)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.inst_textBrowser = QTextBrowser(self.frame_9)
        self.inst_textBrowser.setObjectName(u"inst_textBrowser")
        self.inst_textBrowser.setMinimumSize(QSize(600, 0))
        font10 = QFont()
        font10.setFamilies([u"Segoe UI"])
        font10.setPointSize(11)
        self.inst_textBrowser.setFont(font10)
        self.inst_textBrowser.setStyleSheet(u"#inst_textBrowser{\n"
"background-color: #1c1c27;\n"
"border-radius: 15px;\n"
"padding: 5px;\n"
"color:#eeeeee;\n"
"}\n"
"")

        self.gridLayout_25.addWidget(self.inst_textBrowser, 0, 1, 1, 1)


        self.gridLayout_17.addWidget(self.frame_9, 0, 0, 1, 1)

        self.pages.addWidget(self.infoPage)
        self.softwPage = QWidget()
        self.softwPage.setObjectName(u"softwPage")
        self.gridLayout_23 = QGridLayout(self.softwPage)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.label_25 = QLabel(self.softwPage)
        self.label_25.setObjectName(u"label_25")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy6)
        self.label_25.setMinimumSize(QSize(350, 350))
        self.label_25.setMaximumSize(QSize(350, 350))
        self.label_25.setFocusPolicy(Qt.NoFocus)
        self.label_25.setAutoFillBackground(False)
        self.label_25.setFrameShadow(QFrame.Plain)
        self.label_25.setPixmap(QPixmap(u":/icon/icon/icon.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setAlignment(Qt.AlignCenter)
        self.label_25.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout_23.addWidget(self.label_25, 0, 0, 1, 1)

        self.softinf_frame = QFrame(self.softwPage)
        self.softinf_frame.setObjectName(u"softinf_frame")
        self.softinf_frame.setMinimumSize(QSize(0, 430))
        self.softinf_frame.setMaximumSize(QSize(430, 16777215))
        self.softinf_frame.setStyleSheet(u"#softinf_frame{\n"
"background-color: #1c1c27;\n"
"border-radius: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.softinf_frame.setFrameShape(QFrame.Box)
        self.softinf_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.softinf_frame)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.dev_frame = QFrame(self.softinf_frame)
        self.dev_frame.setObjectName(u"dev_frame")
        self.dev_frame.setMinimumSize(QSize(400, 128))
        self.dev_frame.setStyleSheet(u"#dev_frame {\n"
"background: #2d3259;\n"
"border-radius: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#dev_frame {\n"
"                subcontrol-origin: margin;\n"
"                subcontrol-position: top center;    /* position at the top center */\n"
"}\n"
"\n"
"")
        self.dev_frame.setFrameShape(QFrame.StyledPanel)
        self.dev_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.dev_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.label_18 = QLabel(self.dev_frame)
        self.label_18.setObjectName(u"label_18")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy7)
        self.label_18.setMaximumSize(QSize(110, 110))
        self.label_18.setBaseSize(QSize(0, 0))
        self.label_18.setTextFormat(Qt.RichText)
        self.label_18.setPixmap(QPixmap(u":/icon/icon/dev_2.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setMargin(5)
        self.label_18.setIndent(10)

        self.horizontalLayout_6.addWidget(self.label_18)

        self.label_20 = QLabel(self.dev_frame)
        self.label_20.setObjectName(u"label_20")
        sizePolicy7.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy7)
        self.label_20.setMinimumSize(QSize(300, 0))
        self.label_20.setMaximumSize(QSize(150, 120))
        font11 = QFont()
        font11.setFamilies([u"Segoe UI"])
        self.label_20.setFont(font11)
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_20.setWordWrap(True)
        self.label_20.setMargin(5)
        self.label_20.setIndent(10)

        self.horizontalLayout_6.addWidget(self.label_20)

        self.horizontalSpacer_4 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.gridLayout_19.addWidget(self.dev_frame, 3, 0, 1, 1)

        self.contact_groupBox = QGroupBox(self.softinf_frame)
        self.contact_groupBox.setObjectName(u"contact_groupBox")
        self.contact_groupBox.setMinimumSize(QSize(400, 80))
        self.contact_groupBox.setStyleSheet(u"#contact_groupBox {\n"
"background: #2d3259;\n"
"border-radius: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#contact_groupBox::title {\n"
"                subcontrol-origin: margin;\n"
"                subcontrol-position: top left;    /* position at the top center */\n"
"padding: 5px;\n"
"                \n"
"}\n"
"")
        self.contact_groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_20 = QGridLayout(self.contact_groupBox)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.label_61 = QLabel(self.contact_groupBox)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(35, 25))
        self.label_61.setMaximumSize(QSize(35, 25))
        self.label_61.setPixmap(QPixmap(u":/icon/icon/mail.svg"))
        self.label_61.setScaledContents(True)

        self.gridLayout_20.addWidget(self.label_61, 0, 1, 1, 1)

        self.label_60 = QLabel(self.contact_groupBox)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMaximumSize(QSize(175, 16777215))
        self.label_60.setFont(font3)

        self.gridLayout_20.addWidget(self.label_60, 0, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_6, 0, 3, 1, 1)


        self.gridLayout_19.addWidget(self.contact_groupBox, 5, 0, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_19.addItem(self.verticalSpacer_15, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_19.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.label_57 = QLabel(self.softinf_frame)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(0, 80))
        self.label_57.setMaximumSize(QSize(16777215, 80))
        font12 = QFont()
        font12.setFamilies([u"Bahnschrift SemiBold Condensed"])
        font12.setPointSize(18)
        font12.setBold(True)
        self.label_57.setFont(font12)
        self.label_57.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_57, 1, 0, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_19.addItem(self.verticalSpacer_16, 2, 0, 1, 1)

        self.thx_textBrowser = QTextBrowser(self.softinf_frame)
        self.thx_textBrowser.setObjectName(u"thx_textBrowser")
        self.thx_textBrowser.setMinimumSize(QSize(0, 250))
        self.thx_textBrowser.setMaximumSize(QSize(16777215, 250))
        self.thx_textBrowser.setStyleSheet(u"#thx_textBrowser{\n"
"background: #2d3259;\n"
"border-radius: 15px;\n"
"padding: 5px;\n"
"color:#eeeeee\n"
"}")

        self.gridLayout_19.addWidget(self.thx_textBrowser, 4, 0, 1, 1)

        self.icons_groupBox = QGroupBox(self.softinf_frame)
        self.icons_groupBox.setObjectName(u"icons_groupBox")
        self.icons_groupBox.setMinimumSize(QSize(0, 100))
        self.icons_groupBox.setStyleSheet(u"#icons_groupBox {\n"
"background: #2d3259;\n"
"border-radius: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#icons_groupBox::title {\n"
"                subcontrol-origin: margin;\n"
"                subcontrol-position: top left;    /* position at the top center */\n"
"padding: 5px;\n"
"                \n"
"}\n"
"")
        self.gridLayout_10 = QGridLayout(self.icons_groupBox)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(-1, 6, -1, 9)
        self.icon_textEdit = QTextEdit(self.icons_groupBox)
        self.icon_textEdit.setObjectName(u"icon_textEdit")
        self.icon_textEdit.setMinimumSize(QSize(0, 125))
        self.icon_textEdit.setMaximumSize(QSize(16777215, 100))
        self.icon_textEdit.setStyleSheet(u"#icon_textEdit {\n"
"background: #2d3259;\n"
"border-radius: 15px;\n"
"padding: 10px;\n"
"font-size: 9pt;\n"
"color: #eeeeee;\n"
"}")
        self.icon_textEdit.setInputMethodHints(Qt.ImhMultiLine)
        self.icon_textEdit.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout_10.addWidget(self.icon_textEdit, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.icons_groupBox, 6, 0, 1, 1)


        self.gridLayout_23.addWidget(self.softinf_frame, 0, 1, 2, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_30 = QLabel(self.softwPage)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(300, 50))
        self.label_30.setPixmap(QPixmap(u":/icon/icon/aukr.png"))
        self.label_30.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_30, 0, 0, 1, 2)

        self.label_26 = QLabel(self.softwPage)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(120, 120))
        self.label_26.setPixmap(QPixmap(u":/icon/icon/python.png"))
        self.label_26.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_26, 1, 0, 1, 1)

        self.label_41 = QLabel(self.softwPage)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(150, 150))
        self.label_41.setPixmap(QPixmap(u":/icon/icon/qt.png"))
        self.label_41.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_41, 1, 1, 1, 1)


        self.gridLayout_23.addLayout(self.gridLayout_6, 1, 0, 1, 1)

        self.oprsys_frame = QFrame(self.softwPage)
        self.oprsys_frame.setObjectName(u"oprsys_frame")
        self.oprsys_frame.setMinimumSize(QSize(325, 0))
        self.oprsys_frame.setMaximumSize(QSize(400, 16777215))
        self.oprsys_frame.setStyleSheet(u"#oprsys_frame{\n"
"background-color: #1c1c27;\n"
"border-radius: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.oprsys_frame.setFrameShape(QFrame.Box)
        self.oprsys_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.oprsys_frame)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.verticalSpacer_9 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_21.addItem(self.verticalSpacer_9, 0, 1, 1, 1)

        self.label_24 = QLabel(self.oprsys_frame)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 80))
        self.label_24.setMaximumSize(QSize(16777215, 80))
        self.label_24.setFont(font12)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_24, 1, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_21.addItem(self.verticalSpacer_8, 2, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_21.addItem(self.verticalSpacer_7, 5, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_29 = QLabel(self.oprsys_frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(75, 75))
        self.label_29.setMaximumSize(QSize(75, 75))
        self.label_29.setPixmap(QPixmap(u":/icon/icon/ubuntu-logo.png"))
        self.label_29.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_29)

        self.label_31 = QLabel(self.oprsys_frame)
        self.label_31.setObjectName(u"label_31")
        font13 = QFont()
        font13.setFamilies([u"Bahnschrift Light SemiCondensed"])
        font13.setPointSize(20)
        self.label_31.setFont(font13)

        self.horizontalLayout_7.addWidget(self.label_31)


        self.gridLayout_22.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_27 = QLabel(self.oprsys_frame)
        self.label_27.setObjectName(u"label_27")
        sizePolicy6.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy6)
        self.label_27.setMinimumSize(QSize(75, 75))
        self.label_27.setMaximumSize(QSize(75, 75))
        self.label_27.setPixmap(QPixmap(u":/icon/icon/windows10_2.png"))
        self.label_27.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_27)

        self.label_28 = QLabel(self.oprsys_frame)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font13)

        self.horizontalLayout_5.addWidget(self.label_28)


        self.gridLayout_22.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_36 = QLabel(self.oprsys_frame)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(75, 75))
        self.label_36.setMaximumSize(QSize(75, 75))
        self.label_36.setPixmap(QPixmap(u":/icon/icon/windows-11.png"))
        self.label_36.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_36)

        self.label_37 = QLabel(self.oprsys_frame)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font13)

        self.horizontalLayout_10.addWidget(self.label_37)


        self.gridLayout_22.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_22, 3, 1, 1, 1)


        self.gridLayout_23.addWidget(self.oprsys_frame, 0, 2, 2, 1)

        self.pages.addWidget(self.softwPage)

        self.gridLayout_2.addWidget(self.pages, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.latlineEdit, self.longlineEdit)
        QWidget.setTabOrder(self.longlineEdit, self.elevlineEdit)
        QWidget.setTabOrder(self.elevlineEdit, self.tlimitslineEdit)
        QWidget.setTabOrder(self.tlimitslineEdit, self.utclineEdit)
        QWidget.setTabOrder(self.utclineEdit, self.setBtn)
        QWidget.setTabOrder(self.setBtn, self.savesetBtn)
        QWidget.setTabOrder(self.savesetBtn, self.dateEdit)
        QWidget.setTabOrder(self.dateEdit, self.periodlineEdit)
        QWidget.setTabOrder(self.periodlineEdit, self.reftimelineEdit)
        QWidget.setTabOrder(self.reftimelineEdit, self.opr_resultlineEdit)
        QWidget.setTabOrder(self.opr_resultlineEdit, self.staralt_radioButton)
        QWidget.setTabOrder(self.staralt_radioButton, self.starobs_radioButton)
        QWidget.setTabOrder(self.starobs_radioButton, self.plainTextEdit)
        QWidget.setTabOrder(self.plainTextEdit, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.clearBtn)
        QWidget.setTabOrder(self.clearBtn, self.sim_ms_lineEdit)
        QWidget.setTabOrder(self.sim_ms_lineEdit, self.sim_ms_textEdit)
        QWidget.setTabOrder(self.sim_ms_textEdit, self.daylight_lineEdit)
        QWidget.setTabOrder(self.daylight_lineEdit, self.ct1_lineEdit)
        QWidget.setTabOrder(self.ct1_lineEdit, self.nt1_lineEdit)
        QWidget.setTabOrder(self.nt1_lineEdit, self.at1_lineEdit)
        QWidget.setTabOrder(self.at1_lineEdit, self.night_lineEdit)
        QWidget.setTabOrder(self.night_lineEdit, self.at2_lineEdit)
        QWidget.setTabOrder(self.at2_lineEdit, self.nt2_lineEdit)
        QWidget.setTabOrder(self.nt2_lineEdit, self.ct2_lineEdit)
        QWidget.setTabOrder(self.ct2_lineEdit, self.conv_spinbox_min)
        QWidget.setTabOrder(self.conv_spinbox_min, self.conv_dspinbox_sec)
        QWidget.setTabOrder(self.conv_dspinbox_sec, self.conv_spinbox_deg)
        QWidget.setTabOrder(self.conv_spinbox_deg, self.conv_pushButton)
        QWidget.setTabOrder(self.conv_pushButton, self.minimizeButton)
        QWidget.setTabOrder(self.minimizeButton, self.restoreButton)
        QWidget.setTabOrder(self.restoreButton, self.closeButton)
        QWidget.setTabOrder(self.closeButton, self.conv_textEdit)
        QWidget.setTabOrder(self.conv_textEdit, self.conv_dspinbox_sec_2)
        QWidget.setTabOrder(self.conv_dspinbox_sec_2, self.conv_spinbox_hour)
        QWidget.setTabOrder(self.conv_spinbox_hour, self.conv_textEdit_2)
        QWidget.setTabOrder(self.conv_textEdit_2, self.objvisBtn)
        QWidget.setTabOrder(self.objvisBtn, self.conv_pushButton_2)
        QWidget.setTabOrder(self.conv_pushButton_2, self.conv_spinbox_min_2)
        QWidget.setTabOrder(self.conv_spinbox_min_2, self.simdataBtn)
        QWidget.setTabOrder(self.simdataBtn, self.convBtn)
        QWidget.setTabOrder(self.convBtn, self.infoBtn)
        QWidget.setTabOrder(self.infoBtn, self.sofwBtn)

        self.retranslateUi(MainWindow)
        self.comboBox.activated.connect(self.utclineEdit.update)
        self.comboBox.currentIndexChanged.connect(self.latlineEdit.update)
        self.comboBox.currentIndexChanged.connect(self.longlineEdit.update)
        self.comboBox.currentIndexChanged.connect(self.elevlineEdit.update)

        self.simdataBtn.setDefault(False)
        self.pages.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(0)
        self.ms_qregion_comboBox.setCurrentIndex(1)
        self.qregion_comboBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Astro Observer Plan", None))
        self.objvisBtn.setText("")
        self.simdataBtn.setText("")
        self.convBtn.setText("")
        self.infoBtn.setText("")
        self.sofwBtn.setText("")
        self.headerlabel.setText("")
        self.minimizeButton.setText("")
        self.restoreButton.setText("")
        self.closeButton.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#eeeeee;\">v23.2.1</span></p></body></html>", None))
        self.astinf_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Astronomical Times", None))
        self.daylighttextlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Daylight</span></p></body></html>", None))
        self.elevcoryes_radioBtn.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.elevcorno_radioBtn.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.elevcortextlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Elevation (at sea level) Correction</span></p></body></html>", None))
        self.elevinfoBtn.setText("")
        self.daylight_lineEdit.setText("")
        self.daylight_lineEdit.setPlaceholderText("")
        self.asttwi2textlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Astro. Twilight</span></p></body></html>", None))
        self.at2_lineEdit.setText("")
        self.at2_lineEdit.setPlaceholderText("")
        self.nighttextlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Night</span></p></body></html>", None))
        self.nautwitextlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Nau. Twilight</span></p></body></html>", None))
        self.at1_lineEdit.setText("")
        self.at1_lineEdit.setPlaceholderText("")
        self.night_lineEdit.setText("")
        self.night_lineEdit.setPlaceholderText("")
        self.civiltwi2textlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Civil Twilight</span></p></body></html>", None))
        self.nt2_lineEdit.setText("")
        self.nt2_lineEdit.setPlaceholderText("")
        self.nautwi2textlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Nau. Twilight</span></p></body></html>", None))
        self.civiltwilabel.setText("")
        self.daylighticonlabel.setText("")
        self.asttwilabel.setText("")
        self.nightlabel.setText("")
        self.ct1_lineEdit.setText("")
        self.ct1_lineEdit.setPlaceholderText("")
        self.nautwilabel.setText("")
        self.civiltiwitextlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Civil Twilight</span></p></body></html>", None))
        self.nautwi2label.setText("")
        self.asttwitextlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Astro. Twilight</span></p></body></html>", None))
        self.asttwi2label.setText("")
        self.nt1_lineEdit.setText("")
        self.nt1_lineEdit.setPlaceholderText("")
        self.ct2_lineEdit.setText("")
        self.ct2_lineEdit.setPlaceholderText("")
        self.civiltwi2label.setText("")
        self.illutextlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Illumination</span></p></body></html>", None))
        self.phasetextlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Phase</span></p></body></html>", None))
        self.moonphaseline.setText("")
        self.moonphaseline.setPlaceholderText("")
        self.illuminationline.setText("")
        self.illuminationline.setPlaceholderText("")
        self.moonsetline.setText("")
        self.moonsetline.setPlaceholderText("")
        self.settextlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Set</span></p></body></html>", None))
        self.illuiconlabel.setText("")
        self.seticonlabel.setText("")
        self.phaseiconlabel.setText("")
        self.elevcortextlabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#eeeeee;\">Moon</span></p></body></html>", None))
        self.risetextlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Rise</span></p></body></html>", None))
        self.riseiconlabel.setText("")
        self.moonriseline.setText("")
        self.moonriseline.setPlaceholderText("")
        self.loc_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Location, Timezone and Telescope Limits Settings", None))
        self.teliconlabel.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Manual", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"19 May\u0131s University Observatory (Turkey)", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"500m-Aperture Spherical Telescope (China)", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Ad\u0131yaman University Observatory (Turkey)", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Ali Observatory (China)", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Ankara University Kreiken Observatory (Turkey)", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Anton Pannekoek Observatory (Netherlands)", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Apache Point Observatory (USA)", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Arecibo Observatory (Puerto Rico)", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Armagh Observatory (UK)", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Astronomical Station Vidojevica (Serbia)", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"Atacama Large Millimeter Array (Chile)", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"Atacama Pathfinder Experiment (Chile)", None))
        self.comboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"Australia Telescope Compact Array (Australia)", None))
        self.comboBox.setItemText(14, QCoreApplication.translate("MainWindow", u"Australian Astronomical Observatory (Australia)", None))
        self.comboBox.setItemText(15, QCoreApplication.translate("MainWindow", u"Beijing XingLong Observatory (China)", None))
        self.comboBox.setItemText(16, QCoreApplication.translate("MainWindow", u"Biruni Observatory (Iran)", None))
        self.comboBox.setItemText(17, QCoreApplication.translate("MainWindow", u"Bulgarian National Astronomical Observatory (Bulgaria)", None))
        self.comboBox.setItemText(18, QCoreApplication.translate("MainWindow", u"Calar Alto (Spain)", None))
        self.comboBox.setItemText(19, QCoreApplication.translate("MainWindow", u"Canada-France-Hawaii Telescope (USA)", None))
        self.comboBox.setItemText(20, QCoreApplication.translate("MainWindow", u"Catalina Observatory: 61 inch telescope (USA)", None))
        self.comboBox.setItemText(21, QCoreApplication.translate("MainWindow", u"Cerro Tololo Interamerican Observatory (Chile)", None))
        self.comboBox.setItemText(22, QCoreApplication.translate("MainWindow", u"Crimean Astrophysical Observatory (Ukraine)", None))
        self.comboBox.setItemText(23, QCoreApplication.translate("MainWindow", u"\u00c7anakkale 18 Mart University Ulup\u0131nar Observatory (Turkey)", None))
        self.comboBox.setItemText(24, QCoreApplication.translate("MainWindow", u"Discovery Channel Telescope (USA)", None))
        self.comboBox.setItemText(25, QCoreApplication.translate("MainWindow", u"Dominion Astrophysical Observatory (Canada)", None))
        self.comboBox.setItemText(26, QCoreApplication.translate("MainWindow", u"Dominion Radio Astrophysical Observatory (Canada)", None))
        self.comboBox.setItemText(27, QCoreApplication.translate("MainWindow", u"Dwingeloo Radio Observatory (Netherlands)", None))
        self.comboBox.setItemText(28, QCoreApplication.translate("MainWindow", u"Effelsberg 100m Telescope (Germany)", None))
        self.comboBox.setItemText(29, QCoreApplication.translate("MainWindow", u"Ege University Observatory (Turkey)", None))
        self.comboBox.setItemText(30, QCoreApplication.translate("MainWindow", u"Erciyes University Astronomy and Space Sciences Observatory (Turkey)", None))
        self.comboBox.setItemText(31, QCoreApplication.translate("MainWindow", u"European Extremely Large Telescope (Chile)", None))
        self.comboBox.setItemText(32, QCoreApplication.translate("MainWindow", u"Gemini North (USA)", None))
        self.comboBox.setItemText(33, QCoreApplication.translate("MainWindow", u"Gemini South (Chile)", None))
        self.comboBox.setItemText(34, QCoreApplication.translate("MainWindow", u"Gordon Southam Observatory (Canada)", None))
        self.comboBox.setItemText(35, QCoreApplication.translate("MainWindow", u"Green Bank Observatory (USA)", None))
        self.comboBox.setItemText(36, QCoreApplication.translate("MainWindow", u"Griffith Observatory (USA)", None))
        self.comboBox.setItemText(37, QCoreApplication.translate("MainWindow", u"Haleakala Observatories (USA)", None))
        self.comboBox.setItemText(38, QCoreApplication.translate("MainWindow", u"Halley's Mount (Saint Helena)", None))
        self.comboBox.setItemText(39, QCoreApplication.translate("MainWindow", u"INAF Catania Astrophysical Observatory (Italy)", None))
        self.comboBox.setItemText(40, QCoreApplication.translate("MainWindow", u"IRAM 30m Telescope (Spain)", None))
        self.comboBox.setItemText(41, QCoreApplication.translate("MainWindow", u"IUCAA Girawali Observatory (Ind\u0131a)", None))
        self.comboBox.setItemText(42, QCoreApplication.translate("MainWindow", u"Indian Astronomical Observatory (India)", None))
        self.comboBox.setItemText(43, QCoreApplication.translate("MainWindow", u"In\u00f6n\u00fc University Observatory (Turkey)", None))
        self.comboBox.setItemText(44, QCoreApplication.translate("MainWindow", u"International Liquid Mirror Telescope (India)", None))
        self.comboBox.setItemText(45, QCoreApplication.translate("MainWindow", u"Iranian National Observatory (Iran)", None))
        self.comboBox.setItemText(46, QCoreApplication.translate("MainWindow", u"Ishigaki Astronomical Observatory (Japan)", None))
        self.comboBox.setItemText(47, QCoreApplication.translate("MainWindow", u"Istanbul University Observatory (Turkey)", None))
        self.comboBox.setItemText(48, QCoreApplication.translate("MainWindow", u"James Clerk Maxwell Telescope (USA)", None))
        self.comboBox.setItemText(49, QCoreApplication.translate("MainWindow", u"Jena Observatory (Germany)", None))
        self.comboBox.setItemText(50, QCoreApplication.translate("MainWindow", u"Jodrell Bank Observatory (UK)", None))
        self.comboBox.setItemText(51, QCoreApplication.translate("MainWindow", u"Kiso Observatory (Japan)", None))
        self.comboBox.setItemText(52, QCoreApplication.translate("MainWindow", u"Kitt Peak National Observatory (USA)", None))
        self.comboBox.setItemText(53, QCoreApplication.translate("MainWindow", u"LIGO (Hanford) (USA)", None))
        self.comboBox.setItemText(54, QCoreApplication.translate("MainWindow", u"LIGO (Livingston) (USA)", None))
        self.comboBox.setItemText(55, QCoreApplication.translate("MainWindow", u"La Silla Observatory (ESO) (Chile)", None))
        self.comboBox.setItemText(56, QCoreApplication.translate("MainWindow", u"Landessternwarte Heidelberg-K\u00f6nigstuhl (Germany)", None))
        self.comboBox.setItemText(57, QCoreApplication.translate("MainWindow", u"Large Binocular Telescope (USA)", None))
        self.comboBox.setItemText(58, QCoreApplication.translate("MainWindow", u"Large Millimeter Telescope (Mexico)", None))
        self.comboBox.setItemText(59, QCoreApplication.translate("MainWindow", u"Las Campanas Observatory (Chile)", None))
        self.comboBox.setItemText(60, QCoreApplication.translate("MainWindow", u"Leibniz-Institut f\u00fcr Astrophysik Potsdam (Germany)", None))
        self.comboBox.setItemText(61, QCoreApplication.translate("MainWindow", u"Leoncito Astronomical Complex (Argentina)", None))
        self.comboBox.setItemText(62, QCoreApplication.translate("MainWindow", u"Lick Observatory (USA)", None))
        self.comboBox.setItemText(63, QCoreApplication.translate("MainWindow", u"Loiano Observatory (Italy)", None))
        self.comboBox.setItemText(64, QCoreApplication.translate("MainWindow", u"Los Nogales de Roan Jase (Chile)", None))
        self.comboBox.setItemText(65, QCoreApplication.translate("MainWindow", u"Lowell Observatory (USA)", None))
        self.comboBox.setItemText(66, QCoreApplication.translate("MainWindow", u"Manastash Ridge Observatory (USA)", None))
        self.comboBox.setItemText(67, QCoreApplication.translate("MainWindow", u"McDonald Observatory (USA)", None))
        self.comboBox.setItemText(68, QCoreApplication.translate("MainWindow", u"Medicina Radio Telescope (Italy)", None))
        self.comboBox.setItemText(69, QCoreApplication.translate("MainWindow", u"Mets\u00e4hovi Radio Observatory (Finland)", None))
        self.comboBox.setItemText(70, QCoreApplication.translate("MainWindow", u"Michigan-Dartmouth-MIT Observatory (USA)", None))
        self.comboBox.setItemText(71, QCoreApplication.translate("MainWindow", u"Molonglo Observatory Synthesis Telescope (Australia)", None))
        self.comboBox.setItemText(72, QCoreApplication.translate("MainWindow", u"Mount Abu InfraRed Observatory (Ind\u0131a)", None))
        self.comboBox.setItemText(73, QCoreApplication.translate("MainWindow", u"Mount Ekar 182 cm. Telescope (Italy)", None))
        self.comboBox.setItemText(74, QCoreApplication.translate("MainWindow", u"Mount Wilson Observatory (USA)", None))
        self.comboBox.setItemText(75, QCoreApplication.translate("MainWindow", u"Mt. Stromlo Observatory (Australia)", None))
        self.comboBox.setItemText(76, QCoreApplication.translate("MainWindow", u"Mullard Radio Astronomy Observatory (UK)", None))
        self.comboBox.setItemText(77, QCoreApplication.translate("MainWindow", u"Multiple Mirror Telescope (USA)", None))
        self.comboBox.setItemText(78, QCoreApplication.translate("MainWindow", u"Murchison Radio-astronomy Observatory (Australia)", None))
        self.comboBox.setItemText(79, QCoreApplication.translate("MainWindow", u"NASA Infrared Telescope Facility (USA)", None))
        self.comboBox.setItemText(80, QCoreApplication.translate("MainWindow", u"National Observatory of Venezuela (Venezuela)", None))
        self.comboBox.setItemText(81, QCoreApplication.translate("MainWindow", u"Next-Generation Transit Survey (Chile)", None))
        self.comboBox.setItemText(82, QCoreApplication.translate("MainWindow", u"Nishi-Harima Astronomical Observatory (Japan)", None))
        self.comboBox.setItemText(83, QCoreApplication.translate("MainWindow", u"Nobeyama 45m Telescope (Japan)", None))
        self.comboBox.setItemText(84, QCoreApplication.translate("MainWindow", u"Noto Radio Telescope (Italy)", None))
        self.comboBox.setItemText(85, QCoreApplication.translate("MainWindow", u"Observatoire Sirene (France)", None))
        self.comboBox.setItemText(86, QCoreApplication.translate("MainWindow", u"Observatoire de Haute Provence (France)", None))
        self.comboBox.setItemText(87, QCoreApplication.translate("MainWindow", u"Observatoire de de la C\u00f4te d\u2019Azur (France)", None))
        self.comboBox.setItemText(88, QCoreApplication.translate("MainWindow", u"Observatoire du Pic du Midi (France)", None))
        self.comboBox.setItemText(89, QCoreApplication.translate("MainWindow", u"Observatorio Astrof\u00edsico de Javalambre (Spain)", None))
        self.comboBox.setItemText(90, QCoreApplication.translate("MainWindow", u"Observatorio Astronomico Nacional, San Pedro Martir (Mexico)", None))
        self.comboBox.setItemText(91, QCoreApplication.translate("MainWindow", u"Observatorio Astronomico Nacional, Tonantzintla (Mexico)", None))
        self.comboBox.setItemText(92, QCoreApplication.translate("MainWindow", u"Observatorio Astron\u00f3mico Nacional de Chile (Chile)", None))
        self.comboBox.setItemText(93, QCoreApplication.translate("MainWindow", u"Observatorio Astron\u00f3mico Nacional de Colombia (Colombia)", None))
        self.comboBox.setItemText(94, QCoreApplication.translate("MainWindow", u"Observatorio de Yebes (Spain)", None))
        self.comboBox.setItemText(95, QCoreApplication.translate("MainWindow", u"Observat\u00f3rio Pico dos Dias (Brazil)", None))
        self.comboBox.setItemText(96, QCoreApplication.translate("MainWindow", u"Observat\u00f3rio do Valongo (Brazil)", None))
        self.comboBox.setItemText(97, QCoreApplication.translate("MainWindow", u"Okayama Astrophysical Observatory (Japan)", None))
        self.comboBox.setItemText(98, QCoreApplication.translate("MainWindow", u"Olin Science Center (USA)", None))
        self.comboBox.setItemText(99, QCoreApplication.translate("MainWindow", u"Oliver Observing Station (USA)", None))
        self.comboBox.setItemText(100, QCoreApplication.translate("MainWindow", u"Onsala Space Observatory (Sweden)", None))
        self.comboBox.setItemText(101, QCoreApplication.translate("MainWindow", u"Osservatorio Astrofisico di Asiago (Italy)", None))
        self.comboBox.setItemText(102, QCoreApplication.translate("MainWindow", u"Palomar Observatory (USA)", None))
        self.comboBox.setItemText(103, QCoreApplication.translate("MainWindow", u"Paranal Observatory (ESO) (Chile)", None))
        self.comboBox.setItemText(104, QCoreApplication.translate("MainWindow", u"Parkes 64m Telescope (Australia)", None))
        self.comboBox.setItemText(105, QCoreApplication.translate("MainWindow", u"Peyton Observatory (USA)", None))
        self.comboBox.setItemText(106, QCoreApplication.translate("MainWindow", u"Plateau de Bure Interferometer (France)", None))
        self.comboBox.setItemText(107, QCoreApplication.translate("MainWindow", u"Pointe V\u00e9nus (French Polynesia)", None))
        self.comboBox.setItemText(108, QCoreApplication.translate("MainWindow", u"Pulkovo Observatory (Russia)", None))
        self.comboBox.setItemText(109, QCoreApplication.translate("MainWindow", u"Roque de los Muchachos, La Palma (Spain)", None))
        self.comboBox.setItemText(110, QCoreApplication.translate("MainWindow", u"Royal Observatory Greenwich (UK)", None))
        self.comboBox.setItemText(111, QCoreApplication.translate("MainWindow", u"Royal Observatory, Edinburgh (UK)", None))
        self.comboBox.setItemText(112, QCoreApplication.translate("MainWindow", u"Sardinia Radio Telescope (Italy)", None))
        self.comboBox.setItemText(113, QCoreApplication.translate("MainWindow", u"Seoul National University Astronomical Observatory (South Korea)", None))
        self.comboBox.setItemText(114, QCoreApplication.translate("MainWindow", u"Sharjah Optical Observatory (UAE)", None))
        self.comboBox.setItemText(115, QCoreApplication.translate("MainWindow", u"Skinakas Observatory (Greece)", None))
        self.comboBox.setItemText(116, QCoreApplication.translate("MainWindow", u"South Pole Telescope", None))
        self.comboBox.setItemText(117, QCoreApplication.translate("MainWindow", u"Southern African Large Telescope (South Africa)", None))
        self.comboBox.setItemText(118, QCoreApplication.translate("MainWindow", u"Special Astrophysical Observatory (Russia)", None))
        self.comboBox.setItemText(119, QCoreApplication.translate("MainWindow", u"Square Kilometre Array (South Africa)", None))
        self.comboBox.setItemText(120, QCoreApplication.translate("MainWindow", u"Subaru Telescope (USA)", None))
        self.comboBox.setItemText(121, QCoreApplication.translate("MainWindow", u"Submillimeter Array (USA)", None))
        self.comboBox.setItemText(122, QCoreApplication.translate("MainWindow", u"Teide Observatory (Spain)", None))
        self.comboBox.setItemText(123, QCoreApplication.translate("MainWindow", u"Thai National Observatory (Thailand)", None))
        self.comboBox.setItemText(124, QCoreApplication.translate("MainWindow", u"Tubitak National Observatory (Turkey)", None))
        self.comboBox.setItemText(125, QCoreApplication.translate("MainWindow", u"University College London Observatory (UK)", None))
        self.comboBox.setItemText(126, QCoreApplication.translate("MainWindow", u"University of Canterbury Mount John Observatory (New Zealand)", None))
        self.comboBox.setItemText(127, QCoreApplication.translate("MainWindow", u"Usuda Deep Space Center (Japan)", None))
        self.comboBox.setItemText(128, QCoreApplication.translate("MainWindow", u"VISTA (Chile)", None))
        self.comboBox.setItemText(129, QCoreApplication.translate("MainWindow", u"Vainu Bappu Observatory (India)", None))
        self.comboBox.setItemText(130, QCoreApplication.translate("MainWindow", u"Val d'Aosta Observatory (Italy)", None))
        self.comboBox.setItemText(131, QCoreApplication.translate("MainWindow", u"Very Large Array (USA)", None))
        self.comboBox.setItemText(132, QCoreApplication.translate("MainWindow", u"Vienna Observatory (Austria)", None))
        self.comboBox.setItemText(133, QCoreApplication.translate("MainWindow", u"W. M. Keck Observatory (USA)", None))
        self.comboBox.setItemText(134, QCoreApplication.translate("MainWindow", u"Wendelstein Observatory (Germany)", None))
        self.comboBox.setItemText(135, QCoreApplication.translate("MainWindow", u"Whipple Observatory (USA)", None))
        self.comboBox.setItemText(136, QCoreApplication.translate("MainWindow", u"Wise Observatory (Israel)", None))
        self.comboBox.setItemText(137, QCoreApplication.translate("MainWindow", u"Wright's Tower (UK)", None))

        self.eleviconlabel.setText("")
        self.utclineEdit.setText(QCoreApplication.translate("MainWindow", u"Europe/Istanbul", None))
        self.utciconlabel.setText("")
        self.laticonlabel.setText("")
        self.obsiconlabel.setText("")
        self.latlineEdit.setText(QCoreApplication.translate("MainWindow", u"39\u00b0 50' 37.0\" N", None))
        self.longiconlabel.setText("")
        self.tlimitslineEdit.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.elevlineEdit.setText(QCoreApplication.translate("MainWindow", u"1256.69", None))
        self.longlineEdit.setText(QCoreApplication.translate("MainWindow", u"32\u00b0 46' 45.0\" E", None))
        self.savesetBtn.setText(QCoreApplication.translate("MainWindow", u" Save Settings", None))
        self.setBtn.setText(QCoreApplication.translate("MainWindow", u" Edit Settings", None))
        self.datetime_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Date", None))
        self.dateiconlabel.setText("")
        self.datetextlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Date:</span></p></body></html>", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"d/M/yyyy", None))
        self.datetime_groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Observable Phase Range on Selected Date", None))
        self.periodlineEdit.setText("")
        self.phrangeiconlabel.setText("")
        self.reftimeiconlabel.setText("")
        self.reftimetextLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Ref Time (T</span><span style=\" color:#eeeeee; vertical-align:sub;\">0</span><span style=\" color:#eeeeee;\">):</span></p></body></html>", None))
        self.periodtextLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Period (P):</span></p></body></html>", None))
        self.periodiconlabel.setText("")
        self.phrangeTextLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Phase Range:</span></p></body></html>", None))
        self.opr_resultlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result screen", None))
        self.oprcalcBtn.setText(QCoreApplication.translate("MainWindow", u"Calculate Phase Range", None))
        self.oprclearBtn.setText(QCoreApplication.translate("MainWindow", u" Clear Result", None))
        self.sim_ms_groupBox.setTitle("")
        self.simbadlabel.setText("")
        self.ms_querylabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Query Region:</span></p></body></html>", None))
        self.ms_queryiconlabel.setText("")
        self.ms_qregion_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"arc min", None))
        self.ms_qregion_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"arc sec", None))

        self.sim_ms_lineEdit.setText("")
        self.sim_ms_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter the object's name or ICRS coordinate.", None))
        self.sim_ms_searchBtn.setText("")
        self.sim_ms_clearBtn.setText("")
        self.addBtn.setText("")
        self.sim_ms_textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Information Screen", None))
        self.coord_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Coordinates of the object ( ep = J2000 )", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Show Object Visibility", None))
        self.clearBtn.setText(QCoreApplication.translate("MainWindow", u" Clear Coordinates", None))
        self.graphsetBtn.setText("")
        self.staralt_radioButton.setText(QCoreApplication.translate("MainWindow", u"Staralt", None))
        self.starobs_radioButton.setText(QCoreApplication.translate("MainWindow", u"Starobs", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"hh:mm:ss dd:mm:ss", None))
        self.querylabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Field of View (FOV) :</span></p></body></html>", None))
        self.label_2.setText("")
        self.queryiconlabel.setText("")
        self.sim_lineEdit.setText("")
        self.sim_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter the star's name or ICRS coordinate.", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name / coord :", None))
        self.qregion_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"deg", None))
        self.qregion_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"arc min", None))
        self.qregion_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"arc sec", None))

        self.gaialabel_2.setText("")
        self.gaia_checkBox.setText(QCoreApplication.translate("MainWindow", u"Gaia DR3", None))
        self.simtype_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.simtype_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Only stars", None))

        self.simlabel_2.setText("")
        self.simbad_checkBox.setText(QCoreApplication.translate("MainWindow", u"SIMBAD", None))
        self.irsa_checkBox.setText(QCoreApplication.translate("MainWindow", u"IRSA / 2MASS All-Sky PSC", None))
        self.twomasslabel_2.setText("")
        self.irsalabel_2.setText("")
        self.irsalabel_3.setText("")
        self.irsalabel_4.setText("")
        self.wise_checkBox.setText(QCoreApplication.translate("MainWindow", u"IRSA / AllWise Source Catalog", None))
        self.ztflabel_2.setText("")
        self.ztf_checkBox.setText(QCoreApplication.translate("MainWindow", u"ZTF DR 19", None))
        self.searchBtn.setText(QCoreApplication.translate("MainWindow", u"Search and Show FOV", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#eeeeee;\">ASTRONOMICAL CATALOGS SEARCH</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#eeeeee;\">Multiple catalogs can be searched and the FOV image appears.</span></p></body></html>", None))
        self.groupBox_conv.setTitle(QCoreApplication.translate("MainWindow", u"Degrees Minutes Seconds to Hours Minutes Seconds", None))
        self.convd_seclabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">''</span></p></body></html>", None))
        self.convd_deglabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">\u00b0</span></p></body></html>", None))
        self.convd_minlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">'</span></p></body></html>", None))
        self.conv_pushButton.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.conv_textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result Screen", None))
        self.groupBox_conv_2.setTitle(QCoreApplication.translate("MainWindow", u"Hours Minutes Seconds to Degrees Minutes Seconds", None))
        self.conv_textEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result Screen", None))
        self.convh_hourlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; color:#eeeeee;\">h</span></p></body></html>", None))
        self.convh_seclabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">s</span></p></body></html>", None))
        self.convh_minlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">m</span></p></body></html>", None))
        self.conv_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.inst_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#d5d5d5;\">INSTRUCTIONS FOR USE AND IMPORTANT NOTES </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#ffaa00;\"># OBJECT VISIBILITY AND OBSERVABLE PHASE RANGE</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d5d5d5;\">For object visibility, our program includes 138 observa"
                        "tories. The information of the observatories other than the few observatories we have added is taken from </span><span style=\" font-style:italic; color:#d5d5d5;\">https://github.com/astropy/astropy-data/tree/gh-pages/coordinates</span><span style=\" color:#d5d5d5;\">. The existing observatory settings cannot be changed. Please select the manual option to make your own settings or edit the settings. You can click the &quot;Edit Settings&quot; button in the location, timezone and telescope limits settings section, fill in the relevant fields and edit the settings with the confirm button. When you open the program again, please click the &quot;Save Settings&quot; button to open the program with the settings you entered before. Please make sure you have entered the correct UTC. If you do not want to see the limits of the telescope on the object visibility graph, you can leave the minimum altitude and maximum altitude values of the telescope blank. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; m"
                        "argin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d5d5d5;\">You can select the day you will observe from the Date section. The program opens with today's date by default. Date is valid for both object visibility and Observable Phase Range part. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d5d5d5;\">In the Observable Phase Range on Selected Date section, period should be in days, and reference time should be in julian date. Phase range shows the phase range of the star you selected during the night hours of the date you selected. (for example, binary or multiple star systems). If astronomical night is not available for the current location, if astronomical twilight is available, the phase range is calculated according to the hours of the astronomical twilight interval. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; mar"
                        "gin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d5d5d5;\">For example, the result in Phase Range: </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d5d5d5;\">0.8704 - 0.9062 (1.0348) </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d5d5d5;\">Here 0.8704 is the beginning of the phase and 0.9062 is the end of the phase. The 1.0348 written in parentheses is the completed phase. For example, if the period of the star is 0.24 days (5.76 hours) and the night interval on that day is 6 hours, the observable phase for that night is 6 / 5.76 = 1.0416. Of course the phase range is always in the 0-1 range, we just show it so you can see the phase you've completed. According to the sample result, you completed one full phase and started to complete a new phase again. </span></"
                        "p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d5d5d5;\">In the &quot;Coordinates of the object&quot; section, enter the coordinates in RA (right ascension) and DEC (declination) formats. Enter the coordinate of only 1 object per line. For example, you should add the coordinates of the star Vega and Rigel as follows (hh:mm:ss dd:mm:ss): </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d5d5d5;\">18 36 56.3363 +38 47 01.280 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d5d5d5;\">05 14 32.2721 -08 12 05.898 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d5d5d5;\">You can chan"
                        "ge the theme and two properties of the object visibility graph. You can adjust the theme and these features according to your desire by clicking the button with the settings icon on the far right in the object visibility section. In addition, after the graphic appears, you can adjust the settings related to appearance and naming from the upper part according to your desire. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d5d5d5;\">Also, when you search from Simbad, you will see informations about the relevant object. When you click the &quot;+&quot; button, Simbad will add the coordinates of the object you are searching from the database to the &quot;Coordinates of the object&quot; part. You can search the Simbad database by object name or coordinate. </span><span style=\" font-weight:600; color:#d5d5d5;\">The query region option shows the objects in the area you specify. If you want to see only the"
                        " information of the main object while searching (especially with the name), we recommend that you search in the range of 5-10 arcsec in the query region option. Apart from that, when you search in degrees, if there are too many objects in the area, the search may take a long time. For this reason, we have set a 1 degree limit for this program to work efficiently and properly for now. In the future, we will find a solution to this depending on the situation.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d5d5d5;\">The Staralt option gives the altitude of the related object or objects on the date you selected. When Staralt is selected, when you click the &quot;Show Object Visibility&quot; button, the values written on the related object or objects every hour on the graph that comes before you are the angular distance value of the related object to the Moon. It also automatically adds the name of the r"
                        "elevant object to the chart. It gets the names from the simbad database. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d5d5d5;\">Starobs, on the other hand, gives the one-year altitude values of the related object or objects. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d5d5d5;\">In the astronomical times section, there are important hours for observation. Elevation(for sea level) correction option should be used under certain conditions. For example, for an observer on a mountain, it would be correct to use this option if the horizon line is below its current position. In summary, consider the horizon line at sea level and consider an observer on the mountain at this position. This option corrects for sunrise and sunset, taking into account elevation in addition to atmospheric refra"
                        "ction and solar disk diameter. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d5d5d5;\">It also contains information about the Moon. You can see the Moon's rise, sunset, percent illuminated and phase for the relevant location and date. The position and phase of the Moon in the sky is very important in scientific observations and astrophotography. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#ffaa00;\"># ASTRONOMICAL CATALOGS SEARCH</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d5d5d5;\">When you click on the search button on the 2nd line of the main menu, you will see the astronomical catalogs search section. You can search in SIMBAD, 2MASS "
                        "All-Sky Point Source Catalog, AllWise Source Catalog, Gaia DR3 and ZTF DR 19 catalogues. You can also search in more than one catalogue. You can also limit the SIMBAD search to stars.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d5d5d5;\">Apart from this, when you search in degrees, the search may take a long time if there are many objects in the area. For this reason, we have set a 1 degree limit for now in order for this program to work efficiently and properly. We will find a solution to this in the future, depending on the situation. Enter the area seen by your CCD or CMOS into the FOV value. For now the FOV is limited to a square area. We plan to customize this a lot in the future. After entering the FOV value and selecting the catalogs you want, click on the &quot;Search and Show FOV&quot; button and the search will start and when the search is finished, the results screen will open. The resul"
                        "ts screen includes an area image depending on your FOV value. You can see the results by clicking on the icons of the catalogs you searched in the vertical menu. Objects that you click or select with arrows in the grid are marked with a red square in the FOV area.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#d5d5d5;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d5d5d5;\">In the SIMBAD section, you can filter the results according to color B-V, G-V, U-B, g-r and i-z color indices. In the 2MASS section, you can filter the results according to J-H, H-K, J-K color indices. The reason why we put color indices is that they have an important place in astronomy. It is most commonly used in analysis and is used in the selection of check and comparison stars for observations of binary star"
                        "s or multiple star systems.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#d5d5d5;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d5d5d5;\">For example, when J-H is selected in the 2MASS section, you must enter the J-H value of your main star in the &quot;Index Value&quot; box and then enter a value for a range in the &quot;Range \u00b1&quot; box. For example, let's say the J-H index of our main star is 0.500. When we filter by entering 0.050 in the &quot;Range \u00b1&quot; box, you will only see objects with J-H index between 0.450 and 0.550. These indices and filtering options will help you, but apart from these indices, the characteristics of the main star, the comparison star and the check star, such as their spectral type, object type and whether they show period change or not,"
                        " whether they show brightness change or not, are also very important. Therefore, do not just stick to this program. We always recommend you analyze in more detail.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#d5d5d5;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#d5d5d5;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#d5d5d5;\">\u00a0 </span></p></body></html>", None))
        self.label_25.setText("")
        self.label_18.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#eeeeee;\">DEVELOPERS:</span></p><p><span style=\" font-size:12pt; color:#eeeeee;\">KEREM ERDEM (Astronomer)</span></p><p><span style=\" font-size:12pt; color:#eeeeee;\">KORHAN KARA (Astronomer)</span></p></body></html>", None))
        self.contact_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.label_61.setText("")
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:8pt; font-weight:600; font-style:italic; color:#eeeeee;\">keremdive@gmail.com</span></p><p align=\"justify\"><span style=\" font-size:8pt; font-weight:600; font-style:italic; color:#eeeeee;\">korhankara98@gmail.com</span></p></body></html>", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">SOFTWARE INFORMATION</span></p></body></html>", None))
        self.thx_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">We would like to thank</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left"
                        ":0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">O\u011eUZHAN KARADEN\u0130Z (Astronomer)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Prof. HAKAN VOLKAN \u015eENAVCI</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Assoc. Prof. MESUT YILMAZ</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Asst. Prof. \u0130BRAH\u0130M \u00d6"
                        "ZAVCI</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Asst. Prof. DO\u011eU\u015e \u00d6ZUYAR</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Assoc. Prof. TOLGAHAN KILI\u00c7O\u011eLU</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Res. Asst. PhD ENG\u0130N BAHAR</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Res. Asst. SEL\u00c7UK YAL\u00c7INKAYA</span></p>\n"
"<p align=\"center\" style=\"-qt-paragra"
                        "ph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">for their contributions</span></p></body></html>", None))
        self.icons_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Icons", None))
        self.icon_textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://icons8.com\"><span style=\" text-decoration: underline; color:#eeeeee;\">https://icons8.com</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.clipartmax.com/\"><span style=\" text-decoration: underline; color:#eeeeee;\">https://www.clipartmax.com/</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0"
                        "px;\"><a href=\"https://feathericons.com/\"><span style=\" text-decoration: underline; color:#eeeeee;\">https://feathericons.com/</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://brandeps.com/\"><span style=\" text-decoration: underline; color:#eeeeee;\">https://brandeps.com/</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://brandeps.com/\"><span style=\" text-decoration: underline; color:#eeeeee;\">https://cds.unistra.fr/</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://brandeps.com/\"><span style=\" text-decoration: underline; color:#eeeeee;\">https://irsa.ipac.caltech.edu/</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; m"
                        "argin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline; color:#eeeeee;\">https://wise2.ipac.caltech.edu/</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline; color:#eeeeee;\">https://www.cosmos.esa.int/web/gaia/data-release-3</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline; color:#eeeeee;\">https://www.ztf.caltech.edu/</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; text-decoration: underline; color:#eeeeee;\"><br /></p></body></html>", None))
        self.icon_textEdit.setPlaceholderText("")
        self.label_30.setText("")
        self.label_26.setText("")
        self.label_41.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">OPERATING SYSTEMS</span></p></body></html>", None))
        self.label_29.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Ubuntu</span></p></body></html>", None))
        self.label_27.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Windows 10</span></p></body></html>", None))
        self.label_36.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Windows 11</span></p></body></html>", None))
    # retranslateUi

