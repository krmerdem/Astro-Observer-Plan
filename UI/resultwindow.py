# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resultwindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QStackedWidget, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from mplwidget2 import MplWidget2
import icon_rc

class Ui_resultwindow(object):
    def setupUi(self, resultwindow):
        if not resultwindow.objectName():
            resultwindow.setObjectName(u"resultwindow")
        resultwindow.resize(1491, 844)
        icon = QIcon()
        icon.addFile(u":/icon/icon/colors-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        resultwindow.setWindowIcon(icon)
        resultwindow.setStyleSheet(u"QLineEdit {\n"
"background: #2d3259;\n"
"border-radius: 10px;\n"
"color: #eeeeee;\n"
"font-family:Arial ;\n"
"padding: 5px;\n"
"}\n"
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
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
""
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
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
" QScrollBar:horizontal {\n"
"    border: none;\n"
" "
                        "   background: rgb(45, 45, 68);\n"
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
"QScrollBar::sub-line:horizontal:pressed {	\n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    backgrou"
                        "nd-color: rgb(59, 59, 90);\n"
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
"QPushButton{\n"
"background-color:  #6316AC;\n"
"border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #765cde;\n"
"}\n"
"    \n"
"QPushButton:pressed {\n"
"    background-colo"
                        "r: #7e31b5;\n"
"}\n"
"\n"
"QFrame {\n"
"background: #000221;\n"
"border-radius: 15px;\n"
"\n"
"}")
        self.centralwidget = QWidget(resultwindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"background: #121212;\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.pointerlabel = QLabel(self.frame_4)
        self.pointerlabel.setObjectName(u"pointerlabel")
        self.pointerlabel.setMinimumSize(QSize(100, 0))
        self.pointerlabel.setMaximumSize(QSize(100, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        self.pointerlabel.setFont(font)

        self.gridLayout_8.addWidget(self.pointerlabel, 0, 0, 1, 1)

        self.pointer_horizontalSlider = QSlider(self.frame_4)
        self.pointer_horizontalSlider.setObjectName(u"pointer_horizontalSlider")
        self.pointer_horizontalSlider.setMinimum(3)
        self.pointer_horizontalSlider.setMaximum(20)
        self.pointer_horizontalSlider.setValue(10)
        self.pointer_horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_8.addWidget(self.pointer_horizontalSlider, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_4, 0, 2, 1, 1)

        self.MplWidget2 = MplWidget2(self.centralwidget)
        self.MplWidget2.setObjectName(u"MplWidget2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MplWidget2.sizePolicy().hasHeightForWidth())
        self.MplWidget2.setSizePolicy(sizePolicy)
        self.MplWidget2.setMinimumSize(QSize(750, 750))
        self.MplWidget2.setMaximumSize(QSize(750, 750))

        self.gridLayout.addWidget(self.MplWidget2, 1, 0, 2, 1, Qt.AlignHCenter)

        self.frame_17 = QFrame(self.centralwidget)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 50))
        self.frame_17.setMaximumSize(QSize(16777215, 50))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_17)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_13 = QLabel(self.frame_17)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(40, 25))
        self.label_13.setMaximumSize(QSize(40, 25))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        self.label_13.setFont(font1)

        self.horizontalLayout.addWidget(self.label_13)

        self.fov_lineEdit = QLineEdit(self.frame_17)
        self.fov_lineEdit.setObjectName(u"fov_lineEdit")
        self.fov_lineEdit.setMinimumSize(QSize(0, 25))
        self.fov_lineEdit.setMaximumSize(QSize(16777215, 25))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(11)
        self.fov_lineEdit.setFont(font2)
        self.fov_lineEdit.setStyleSheet(u"#fov_lineEdit{\n"
"	background: transparent;\n"
"}")
        self.fov_lineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.fov_lineEdit)


        self.gridLayout.addWidget(self.frame_17, 0, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(50, 0))
        self.widget.setMaximumSize(QSize(50, 16777215))
        self.widget.setStyleSheet(u"QWidget {\n"
"	background-color: #1c1c27;\n"
"    border-radius: 15px;\n"
"	border: 2px solid #2d3259;\n"
"}\n"
"\n"
"#frame_6 {\n"
"	border: None;\n"
"}\n"
"\n"
"QPushButton {\n"
"border-radius: 15px;\n"
"background-color:#1c1c27;\n"
"border: None;\n"
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
        self.verticalLayout_4.setContentsMargins(0, 15, 0, 0)
        self.frame_6 = QFrame(self.widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(40, 0))
        self.frame_6.setMaximumSize(QSize(40, 400))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setSpacing(25)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.genindexBtn = QPushButton(self.frame_6)
        self.genindexBtn.setObjectName(u"genindexBtn")
        self.genindexBtn.setMinimumSize(QSize(40, 40))
        self.genindexBtn.setMaximumSize(QSize(40, 40))
        self.genindexBtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.genindexBtn.setIcon(icon1)
        self.genindexBtn.setIconSize(QSize(24, 24))
        self.genindexBtn.setCheckable(False)
        self.genindexBtn.setAutoDefault(True)

        self.verticalLayout_5.addWidget(self.genindexBtn, 0, Qt.AlignHCenter)

        self.simbadBtn = QPushButton(self.frame_6)
        self.simbadBtn.setObjectName(u"simbadBtn")
        self.simbadBtn.setMinimumSize(QSize(40, 40))
        self.simbadBtn.setMaximumSize(QSize(40, 40))
        self.simbadBtn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/simbad.png", QSize(), QIcon.Normal, QIcon.Off)
        self.simbadBtn.setIcon(icon2)
        self.simbadBtn.setIconSize(QSize(24, 24))
        self.simbadBtn.setCheckable(False)
        self.simbadBtn.setChecked(False)
        self.simbadBtn.setAutoDefault(True)
        self.simbadBtn.setFlat(False)

        self.verticalLayout_5.addWidget(self.simbadBtn, 0, Qt.AlignHCenter)

        self.irsaBtn = QPushButton(self.frame_6)
        self.irsaBtn.setObjectName(u"irsaBtn")
        self.irsaBtn.setMinimumSize(QSize(40, 40))
        self.irsaBtn.setMaximumSize(QSize(40, 40))
        self.irsaBtn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/2mass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.irsaBtn.setIcon(icon3)
        self.irsaBtn.setIconSize(QSize(24, 24))
        self.irsaBtn.setCheckable(False)
        self.irsaBtn.setAutoDefault(True)

        self.verticalLayout_5.addWidget(self.irsaBtn, 0, Qt.AlignHCenter)

        self.wiseBtn = QPushButton(self.frame_6)
        self.wiseBtn.setObjectName(u"wiseBtn")
        self.wiseBtn.setMinimumSize(QSize(40, 40))
        self.wiseBtn.setMaximumSize(QSize(40, 40))
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/WISE_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.wiseBtn.setIcon(icon4)
        self.wiseBtn.setIconSize(QSize(40, 40))

        self.verticalLayout_5.addWidget(self.wiseBtn, 0, Qt.AlignHCenter)

        self.gaiaBtn = QPushButton(self.frame_6)
        self.gaiaBtn.setObjectName(u"gaiaBtn")
        self.gaiaBtn.setMinimumSize(QSize(40, 40))
        self.gaiaBtn.setMaximumSize(QSize(40, 40))
        self.gaiaBtn.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/Logo_Gaia.png", QSize(), QIcon.Normal, QIcon.Off)
        self.gaiaBtn.setIcon(icon5)
        self.gaiaBtn.setIconSize(QSize(24, 24))
        self.gaiaBtn.setCheckable(False)
        self.gaiaBtn.setAutoDefault(True)

        self.verticalLayout_5.addWidget(self.gaiaBtn, 0, Qt.AlignHCenter)

        self.ztfBtn = QPushButton(self.frame_6)
        self.ztfBtn.setObjectName(u"ztfBtn")
        self.ztfBtn.setMinimumSize(QSize(40, 40))
        self.ztfBtn.setMaximumSize(QSize(40, 40))
        self.ztfBtn.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/ztf_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ztfBtn.setIcon(icon6)
        self.ztfBtn.setIconSize(QSize(24, 24))
        self.ztfBtn.setCheckable(False)
        self.ztfBtn.setAutoDefault(True)

        self.verticalLayout_5.addWidget(self.ztfBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_6, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.gridLayout.addWidget(self.widget, 0, 1, 3, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QStackedWidget {\n"
"	background: #28293d;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#geninfo_page {\n"
"	background: #28293d;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#simbad_page {\n"
"	background: #28293d;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#irsa_page {\n"
"	background: #28293d;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#wise_page {\n"
"	background: #28293d;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"#gaia_page {\n"
"	background: #28293d;\n"
"}\n"
"\n"
"#ztf_page {\n"
"	background: #28293d;\n"
"}\n"
"\n"
"#colorindex_page {\n"
"	background: #28293d;\n"
"}\n"
"\n"
"\n"
"QTableView {\n"
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
"            background:#ffaa00;           "
                        " \n"
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
        self.geninfo_page = QWidget()
        self.geninfo_page.setObjectName(u"geninfo_page")
        self.geninfo_page.setStyleSheet(u"QLabel {\n"
"	border-top-right-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-top-left-radius: 0px;\n"
"	padding: 7px;\n"
"}")
        self.gridLayout_23 = QGridLayout(self.geninfo_page)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.frame_16 = QFrame(self.geninfo_page)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 60))
        self.frame_16.setMaximumSize(QSize(16777215, 60))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_16)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_2 = QLabel(self.frame_16)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_22.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout_23.addWidget(self.frame_16, 0, 0, 1, 2)

        self.label_3 = QLabel(self.geninfo_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(90, 35))
        self.label_3.setMaximumSize(QSize(16777215, 35))
        self.label_3.setFont(font)

        self.gridLayout_23.addWidget(self.label_3, 1, 0, 1, 1)

        self.mainid_lineEdit = QLineEdit(self.geninfo_page)
        self.mainid_lineEdit.setObjectName(u"mainid_lineEdit")
        self.mainid_lineEdit.setMinimumSize(QSize(0, 35))
        self.mainid_lineEdit.setMaximumSize(QSize(16777215, 35))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        self.mainid_lineEdit.setFont(font3)
        self.mainid_lineEdit.setReadOnly(True)

        self.gridLayout_23.addWidget(self.mainid_lineEdit, 1, 1, 1, 1)

        self.label_9 = QLabel(self.geninfo_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(90, 35))
        self.label_9.setMaximumSize(QSize(16777215, 35))
        self.label_9.setFont(font)

        self.gridLayout_23.addWidget(self.label_9, 2, 0, 1, 1)

        self.radec_lineEdit = QLineEdit(self.geninfo_page)
        self.radec_lineEdit.setObjectName(u"radec_lineEdit")
        self.radec_lineEdit.setMinimumSize(QSize(0, 35))
        self.radec_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.radec_lineEdit.setFont(font3)
        self.radec_lineEdit.setReadOnly(True)

        self.gridLayout_23.addWidget(self.radec_lineEdit, 2, 1, 1, 1)

        self.label_24 = QLabel(self.geninfo_page)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(90, 35))
        self.label_24.setMaximumSize(QSize(16777215, 35))
        self.label_24.setFont(font)

        self.gridLayout_23.addWidget(self.label_24, 3, 0, 1, 1)

        self.otype_lineEdit = QLineEdit(self.geninfo_page)
        self.otype_lineEdit.setObjectName(u"otype_lineEdit")
        self.otype_lineEdit.setMinimumSize(QSize(0, 35))
        self.otype_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.otype_lineEdit.setFont(font3)
        self.otype_lineEdit.setReadOnly(True)

        self.gridLayout_23.addWidget(self.otype_lineEdit, 3, 1, 1, 1)

        self.label_25 = QLabel(self.geninfo_page)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(90, 35))
        self.label_25.setMaximumSize(QSize(16777215, 35))
        self.label_25.setFont(font)

        self.gridLayout_23.addWidget(self.label_25, 4, 0, 1, 1)

        self.sptype_lineEdit = QLineEdit(self.geninfo_page)
        self.sptype_lineEdit.setObjectName(u"sptype_lineEdit")
        self.sptype_lineEdit.setMinimumSize(QSize(0, 35))
        self.sptype_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.sptype_lineEdit.setFont(font3)
        self.sptype_lineEdit.setReadOnly(True)

        self.gridLayout_23.addWidget(self.sptype_lineEdit, 4, 1, 1, 1)

        self.label_26 = QLabel(self.geninfo_page)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(90, 120))
        self.label_26.setMaximumSize(QSize(16777215, 120))
        self.label_26.setFont(font)

        self.gridLayout_23.addWidget(self.label_26, 5, 0, 1, 1)

        self.frame_18 = QFrame(self.geninfo_page)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 120))
        self.frame_18.setMaximumSize(QSize(16777215, 120))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_18)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(-1, 9, -1, -1)
        self.magk_lineEdit = QLineEdit(self.frame_18)
        self.magk_lineEdit.setObjectName(u"magk_lineEdit")
        self.magk_lineEdit.setMinimumSize(QSize(60, 35))
        self.magk_lineEdit.setMaximumSize(QSize(60, 35))
        self.magk_lineEdit.setFont(font3)
        self.magk_lineEdit.setReadOnly(True)

        self.gridLayout_24.addWidget(self.magk_lineEdit, 1, 7, 1, 1)

        self.magg_lineEdit = QLineEdit(self.frame_18)
        self.magg_lineEdit.setObjectName(u"magg_lineEdit")
        self.magg_lineEdit.setMinimumSize(QSize(60, 35))
        self.magg_lineEdit.setMaximumSize(QSize(60, 35))
        self.magg_lineEdit.setFont(font3)
        self.magg_lineEdit.setReadOnly(True)

        self.gridLayout_24.addWidget(self.magg_lineEdit, 1, 1, 1, 1)

        self.label_18 = QLabel(self.frame_18)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(35, 35))
        self.label_18.setMaximumSize(QSize(35, 35))
        self.label_18.setFont(font)

        self.gridLayout_24.addWidget(self.label_18, 0, 8, 1, 1)

        self.label_20 = QLabel(self.frame_18)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(35, 35))
        self.label_20.setMaximumSize(QSize(35, 35))
        self.label_20.setFont(font)

        self.gridLayout_24.addWidget(self.label_20, 1, 2, 1, 1)

        self.magj_lineEdit = QLineEdit(self.frame_18)
        self.magj_lineEdit.setObjectName(u"magj_lineEdit")
        self.magj_lineEdit.setMinimumSize(QSize(60, 35))
        self.magj_lineEdit.setMaximumSize(QSize(60, 35))
        self.magj_lineEdit.setFont(font3)
        self.magj_lineEdit.setReadOnly(True)

        self.gridLayout_24.addWidget(self.magj_lineEdit, 1, 3, 1, 1)

        self.label_19 = QLabel(self.frame_18)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(35, 35))
        self.label_19.setMaximumSize(QSize(35, 35))
        self.label_19.setFont(font)

        self.gridLayout_24.addWidget(self.label_19, 1, 0, 1, 1)

        self.label_21 = QLabel(self.frame_18)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(35, 35))
        self.label_21.setMaximumSize(QSize(35, 35))
        self.label_21.setFont(font)

        self.gridLayout_24.addWidget(self.label_21, 1, 4, 1, 1)

        self.label_16 = QLabel(self.frame_18)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(35, 35))
        self.label_16.setMaximumSize(QSize(35, 35))
        self.label_16.setFont(font)

        self.gridLayout_24.addWidget(self.label_16, 0, 4, 1, 1)

        self.magr_lineEdit = QLineEdit(self.frame_18)
        self.magr_lineEdit.setObjectName(u"magr_lineEdit")
        self.magr_lineEdit.setMinimumSize(QSize(60, 35))
        self.magr_lineEdit.setMaximumSize(QSize(60, 35))
        self.magr_lineEdit.setFont(font3)
        self.magr_lineEdit.setReadOnly(True)

        self.gridLayout_24.addWidget(self.magr_lineEdit, 0, 7, 1, 1)

        self.magu_lineEdit = QLineEdit(self.frame_18)
        self.magu_lineEdit.setObjectName(u"magu_lineEdit")
        self.magu_lineEdit.setMinimumSize(QSize(60, 35))
        self.magu_lineEdit.setMaximumSize(QSize(60, 35))
        self.magu_lineEdit.setFont(font3)
        self.magu_lineEdit.setReadOnly(True)

        self.gridLayout_24.addWidget(self.magu_lineEdit, 0, 1, 1, 1)

        self.magi_lineEdit = QLineEdit(self.frame_18)
        self.magi_lineEdit.setObjectName(u"magi_lineEdit")
        self.magi_lineEdit.setMinimumSize(QSize(60, 35))
        self.magi_lineEdit.setMaximumSize(QSize(60, 35))
        self.magi_lineEdit.setFont(font3)
        self.magi_lineEdit.setReadOnly(True)

        self.gridLayout_24.addWidget(self.magi_lineEdit, 0, 9, 1, 1)

        self.label_14 = QLabel(self.frame_18)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(35, 35))
        self.label_14.setMaximumSize(QSize(35, 35))
        self.label_14.setFont(font)

        self.gridLayout_24.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_15 = QLabel(self.frame_18)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(35, 35))
        self.label_15.setMaximumSize(QSize(35, 35))
        self.label_15.setFont(font)

        self.gridLayout_24.addWidget(self.label_15, 0, 2, 1, 1)

        self.magb_lineEdit = QLineEdit(self.frame_18)
        self.magb_lineEdit.setObjectName(u"magb_lineEdit")
        self.magb_lineEdit.setMinimumSize(QSize(60, 35))
        self.magb_lineEdit.setMaximumSize(QSize(60, 35))
        self.magb_lineEdit.setFont(font3)
        self.magb_lineEdit.setReadOnly(True)

        self.gridLayout_24.addWidget(self.magb_lineEdit, 0, 3, 1, 1)

        self.magv_lineEdit = QLineEdit(self.frame_18)
        self.magv_lineEdit.setObjectName(u"magv_lineEdit")
        self.magv_lineEdit.setMinimumSize(QSize(60, 35))
        self.magv_lineEdit.setMaximumSize(QSize(60, 35))
        self.magv_lineEdit.setFont(font3)
        self.magv_lineEdit.setReadOnly(True)

        self.gridLayout_24.addWidget(self.magv_lineEdit, 0, 5, 1, 1)

        self.label_17 = QLabel(self.frame_18)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(35, 35))
        self.label_17.setMaximumSize(QSize(35, 35))
        self.label_17.setFont(font)

        self.gridLayout_24.addWidget(self.label_17, 0, 6, 1, 1)

        self.label_23 = QLabel(self.frame_18)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(35, 35))
        self.label_23.setMaximumSize(QSize(35, 35))
        self.label_23.setFont(font)

        self.gridLayout_24.addWidget(self.label_23, 1, 6, 1, 1)

        self.magh_lineEdit = QLineEdit(self.frame_18)
        self.magh_lineEdit.setObjectName(u"magh_lineEdit")
        self.magh_lineEdit.setMinimumSize(QSize(60, 35))
        self.magh_lineEdit.setMaximumSize(QSize(60, 35))
        self.magh_lineEdit.setFont(font3)
        self.magh_lineEdit.setReadOnly(True)

        self.gridLayout_24.addWidget(self.magh_lineEdit, 1, 5, 1, 1)


        self.gridLayout_23.addWidget(self.frame_18, 5, 1, 1, 1)

        self.label_10 = QLabel(self.geninfo_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(90, 35))
        self.label_10.setMaximumSize(QSize(16777215, 35))
        self.label_10.setFont(font)

        self.gridLayout_23.addWidget(self.label_10, 6, 0, 1, 1)

        self.tycid_lineEdit = QLineEdit(self.geninfo_page)
        self.tycid_lineEdit.setObjectName(u"tycid_lineEdit")
        self.tycid_lineEdit.setMinimumSize(QSize(0, 35))
        self.tycid_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.tycid_lineEdit.setFont(font3)
        self.tycid_lineEdit.setReadOnly(True)

        self.gridLayout_23.addWidget(self.tycid_lineEdit, 6, 1, 1, 1)

        self.label_11 = QLabel(self.geninfo_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(90, 35))
        self.label_11.setMaximumSize(QSize(16777215, 35))
        self.label_11.setFont(font)

        self.gridLayout_23.addWidget(self.label_11, 7, 0, 1, 1)

        self.hipid_lineEdit = QLineEdit(self.geninfo_page)
        self.hipid_lineEdit.setObjectName(u"hipid_lineEdit")
        self.hipid_lineEdit.setMinimumSize(QSize(0, 35))
        self.hipid_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.hipid_lineEdit.setFont(font3)
        self.hipid_lineEdit.setReadOnly(True)

        self.gridLayout_23.addWidget(self.hipid_lineEdit, 7, 1, 1, 1)

        self.label_8 = QLabel(self.geninfo_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(90, 35))
        self.label_8.setMaximumSize(QSize(16777215, 35))
        self.label_8.setFont(font)

        self.gridLayout_23.addWidget(self.label_8, 8, 0, 1, 1)

        self.ticid_lineEdit = QLineEdit(self.geninfo_page)
        self.ticid_lineEdit.setObjectName(u"ticid_lineEdit")
        self.ticid_lineEdit.setMinimumSize(QSize(0, 35))
        self.ticid_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.ticid_lineEdit.setFont(font3)
        self.ticid_lineEdit.setReadOnly(True)

        self.gridLayout_23.addWidget(self.ticid_lineEdit, 8, 1, 1, 1)

        self.label_4 = QLabel(self.geninfo_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(90, 35))
        self.label_4.setMaximumSize(QSize(16777215, 35))
        self.label_4.setFont(font)

        self.gridLayout_23.addWidget(self.label_4, 9, 0, 1, 1)

        self.twomassid_lineEdit = QLineEdit(self.geninfo_page)
        self.twomassid_lineEdit.setObjectName(u"twomassid_lineEdit")
        self.twomassid_lineEdit.setMinimumSize(QSize(0, 35))
        self.twomassid_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.twomassid_lineEdit.setFont(font3)
        self.twomassid_lineEdit.setReadOnly(True)

        self.gridLayout_23.addWidget(self.twomassid_lineEdit, 9, 1, 1, 1)

        self.label_5 = QLabel(self.geninfo_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(90, 35))
        self.label_5.setMaximumSize(QSize(16777215, 35))
        self.label_5.setFont(font)

        self.gridLayout_23.addWidget(self.label_5, 10, 0, 1, 1)

        self.wiseid_lineEdit = QLineEdit(self.geninfo_page)
        self.wiseid_lineEdit.setObjectName(u"wiseid_lineEdit")
        self.wiseid_lineEdit.setMinimumSize(QSize(0, 35))
        self.wiseid_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.wiseid_lineEdit.setFont(font3)
        self.wiseid_lineEdit.setReadOnly(True)

        self.gridLayout_23.addWidget(self.wiseid_lineEdit, 10, 1, 1, 1)

        self.label_6 = QLabel(self.geninfo_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(90, 35))
        self.label_6.setMaximumSize(QSize(16777215, 35))
        self.label_6.setFont(font)

        self.gridLayout_23.addWidget(self.label_6, 11, 0, 1, 1)

        self.gaiadr_lineEdit = QLineEdit(self.geninfo_page)
        self.gaiadr_lineEdit.setObjectName(u"gaiadr_lineEdit")
        self.gaiadr_lineEdit.setMinimumSize(QSize(0, 35))
        self.gaiadr_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.gaiadr_lineEdit.setFont(font3)
        self.gaiadr_lineEdit.setReadOnly(True)

        self.gridLayout_23.addWidget(self.gaiadr_lineEdit, 11, 1, 1, 1)

        self.label_7 = QLabel(self.geninfo_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(90, 35))
        self.label_7.setMaximumSize(QSize(16777215, 35))
        self.label_7.setFont(font)

        self.gridLayout_23.addWidget(self.label_7, 12, 0, 1, 1)

        self.atoid_lineEdit = QLineEdit(self.geninfo_page)
        self.atoid_lineEdit.setObjectName(u"atoid_lineEdit")
        self.atoid_lineEdit.setMinimumSize(QSize(0, 35))
        self.atoid_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.atoid_lineEdit.setFont(font3)
        self.atoid_lineEdit.setReadOnly(True)

        self.gridLayout_23.addWidget(self.atoid_lineEdit, 12, 1, 1, 1)

        self.label_12 = QLabel(self.geninfo_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(90, 35))
        self.label_12.setMaximumSize(QSize(16777215, 35))
        self.label_12.setFont(font)

        self.gridLayout_23.addWidget(self.label_12, 13, 0, 1, 1)

        self.crtsid_lineEdit = QLineEdit(self.geninfo_page)
        self.crtsid_lineEdit.setObjectName(u"crtsid_lineEdit")
        self.crtsid_lineEdit.setMinimumSize(QSize(0, 35))
        self.crtsid_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.crtsid_lineEdit.setFont(font3)
        self.crtsid_lineEdit.setReadOnly(True)

        self.gridLayout_23.addWidget(self.crtsid_lineEdit, 13, 1, 1, 1)

        self.stackedWidget.addWidget(self.geninfo_page)
        self.simbad_page = QWidget()
        self.simbad_page.setObjectName(u"simbad_page")
        self.gridLayout_2 = QGridLayout(self.simbad_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_2 = QFrame(self.simbad_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 60))
        self.frame_2.setMaximumSize(QSize(16777215, 60))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(90, 40))
        self.label.setMaximumSize(QSize(90, 40))
        self.label.setPixmap(QPixmap(u":/icon/icon/simbad.png"))
        self.label.setScaledContents(True)

        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_13 = QFrame(self.simbad_page)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_13)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.rangelabel_2 = QLabel(self.frame_13)
        self.rangelabel_2.setObjectName(u"rangelabel_2")
        self.rangelabel_2.setMinimumSize(QSize(75, 0))
        self.rangelabel_2.setMaximumSize(QSize(75, 16777215))
        self.rangelabel_2.setFont(font)

        self.gridLayout_18.addWidget(self.rangelabel_2, 2, 0, 1, 1)

        self.sim_index_lineEdit = QLineEdit(self.frame_13)
        self.sim_index_lineEdit.setObjectName(u"sim_index_lineEdit")
        self.sim_index_lineEdit.setMinimumSize(QSize(0, 30))
        self.sim_index_lineEdit.setMaximumSize(QSize(16777215, 30))
        self.sim_index_lineEdit.setFont(font2)
        self.sim_index_lineEdit.setClearButtonEnabled(True)

        self.gridLayout_18.addWidget(self.sim_index_lineEdit, 1, 1, 1, 1)

        self.indexwidget_3 = QWidget(self.frame_13)
        self.indexwidget_3.setObjectName(u"indexwidget_3")
        self.indexwidget_3.setMinimumSize(QSize(0, 40))
        self.indexwidget_3.setStyleSheet(u"QRadioButton{\n"
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
        self.horizontalLayout_4 = QHBoxLayout(self.indexwidget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.sim_bv_radioButton = QRadioButton(self.indexwidget_3)
        self.sim_bv_radioButton.setObjectName(u"sim_bv_radioButton")
        self.sim_bv_radioButton.setMinimumSize(QSize(0, 30))
        self.sim_bv_radioButton.setMaximumSize(QSize(16777215, 30))
        self.sim_bv_radioButton.setFont(font)
        self.sim_bv_radioButton.setChecked(True)

        self.horizontalLayout_4.addWidget(self.sim_bv_radioButton)

        self.sim_gv_radioButton = QRadioButton(self.indexwidget_3)
        self.sim_gv_radioButton.setObjectName(u"sim_gv_radioButton")
        self.sim_gv_radioButton.setMinimumSize(QSize(0, 30))
        self.sim_gv_radioButton.setMaximumSize(QSize(16777215, 30))
        self.sim_gv_radioButton.setFont(font)

        self.horizontalLayout_4.addWidget(self.sim_gv_radioButton)

        self.sim_ub_radioButton = QRadioButton(self.indexwidget_3)
        self.sim_ub_radioButton.setObjectName(u"sim_ub_radioButton")
        self.sim_ub_radioButton.setMinimumSize(QSize(0, 30))
        self.sim_ub_radioButton.setMaximumSize(QSize(16777215, 30))
        self.sim_ub_radioButton.setFont(font)

        self.horizontalLayout_4.addWidget(self.sim_ub_radioButton)

        self.sim_gr_radioButton = QRadioButton(self.indexwidget_3)
        self.sim_gr_radioButton.setObjectName(u"sim_gr_radioButton")
        self.sim_gr_radioButton.setMinimumSize(QSize(0, 30))
        self.sim_gr_radioButton.setMaximumSize(QSize(16777215, 30))
        self.sim_gr_radioButton.setFont(font)

        self.horizontalLayout_4.addWidget(self.sim_gr_radioButton)

        self.sim_iz_radioButton = QRadioButton(self.indexwidget_3)
        self.sim_iz_radioButton.setObjectName(u"sim_iz_radioButton")
        self.sim_iz_radioButton.setMinimumSize(QSize(0, 30))
        self.sim_iz_radioButton.setMaximumSize(QSize(16777215, 30))
        self.sim_iz_radioButton.setFont(font)

        self.horizontalLayout_4.addWidget(self.sim_iz_radioButton)


        self.gridLayout_18.addWidget(self.indexwidget_3, 0, 0, 1, 2)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 30))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_14)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 9, 0, 6)
        self.sim_showallBtn = QPushButton(self.frame_14)
        self.sim_showallBtn.setObjectName(u"sim_showallBtn")
        self.sim_showallBtn.setMinimumSize(QSize(0, 30))
        self.sim_showallBtn.setMaximumSize(QSize(16777215, 30))
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/index.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sim_showallBtn.setIcon(icon7)

        self.gridLayout_19.addWidget(self.sim_showallBtn, 0, 1, 1, 1)

        self.sim_showBtn = QPushButton(self.frame_14)
        self.sim_showBtn.setObjectName(u"sim_showBtn")
        self.sim_showBtn.setMinimumSize(QSize(0, 30))
        self.sim_showBtn.setMaximumSize(QSize(16777215, 30))
        self.sim_showBtn.setStyleSheet(u"QPushButton{\n"
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
        self.sim_showBtn.setIcon(icon7)
        self.sim_showBtn.setAutoDefault(True)

        self.gridLayout_19.addWidget(self.sim_showBtn, 0, 0, 1, 1)


        self.gridLayout_18.addWidget(self.frame_14, 4, 0, 1, 2)

        self.sim_range_lineEdit = QLineEdit(self.frame_13)
        self.sim_range_lineEdit.setObjectName(u"sim_range_lineEdit")
        self.sim_range_lineEdit.setMinimumSize(QSize(0, 30))
        self.sim_range_lineEdit.setMaximumSize(QSize(16777215, 30))
        self.sim_range_lineEdit.setFont(font2)
        self.sim_range_lineEdit.setClearButtonEnabled(True)

        self.gridLayout_18.addWidget(self.sim_range_lineEdit, 2, 1, 1, 1)

        self.indexlabel_2 = QLabel(self.frame_13)
        self.indexlabel_2.setObjectName(u"indexlabel_2")
        self.indexlabel_2.setMinimumSize(QSize(75, 0))
        self.indexlabel_2.setMaximumSize(QSize(75, 16777215))
        self.indexlabel_2.setFont(font)

        self.gridLayout_18.addWidget(self.indexlabel_2, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_13, 1, 0, 1, 1)

        self.simbad_tableWidget = QTableWidget(self.simbad_page)
        self.simbad_tableWidget.setObjectName(u"simbad_tableWidget")
        self.simbad_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_2.addWidget(self.simbad_tableWidget, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.simbad_page)
        self.irsa_page = QWidget()
        self.irsa_page.setObjectName(u"irsa_page")
        self.gridLayout_4 = QGridLayout(self.irsa_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_7 = QFrame(self.irsa_page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 60))
        self.frame_7.setMaximumSize(QSize(16777215, 80))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_7)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.irsalabel = QLabel(self.frame_7)
        self.irsalabel.setObjectName(u"irsalabel")
        self.irsalabel.setMinimumSize(QSize(90, 40))
        self.irsalabel.setMaximumSize(QSize(90, 40))
        self.irsalabel.setPixmap(QPixmap(u":/icon/icon/irsa.png"))
        self.irsalabel.setScaledContents(True)

        self.gridLayout_12.addWidget(self.irsalabel, 0, 0, 1, 1)

        self.twomasslabel = QLabel(self.frame_7)
        self.twomasslabel.setObjectName(u"twomasslabel")
        self.twomasslabel.setMinimumSize(QSize(90, 40))
        self.twomasslabel.setMaximumSize(QSize(90, 40))
        self.twomasslabel.setPixmap(QPixmap(u":/icon/icon/2mass.png"))
        self.twomasslabel.setScaledContents(True)

        self.gridLayout_12.addWidget(self.twomasslabel, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_7, 0, 0, 1, 1)

        self.frame_10 = QFrame(self.irsa_page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_10)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.tmass_rangelabel = QLabel(self.frame_10)
        self.tmass_rangelabel.setObjectName(u"tmass_rangelabel")
        self.tmass_rangelabel.setMinimumSize(QSize(75, 0))
        self.tmass_rangelabel.setMaximumSize(QSize(75, 16777215))
        self.tmass_rangelabel.setFont(font)

        self.gridLayout_15.addWidget(self.tmass_rangelabel, 2, 0, 1, 1)

        self.tmass_index_lineEdit = QLineEdit(self.frame_10)
        self.tmass_index_lineEdit.setObjectName(u"tmass_index_lineEdit")
        self.tmass_index_lineEdit.setMinimumSize(QSize(0, 30))
        self.tmass_index_lineEdit.setMaximumSize(QSize(16777215, 30))
        self.tmass_index_lineEdit.setFont(font2)
        self.tmass_index_lineEdit.setClearButtonEnabled(True)

        self.gridLayout_15.addWidget(self.tmass_index_lineEdit, 1, 1, 1, 1)

        self.indexwidget_2 = QWidget(self.frame_10)
        self.indexwidget_2.setObjectName(u"indexwidget_2")
        self.indexwidget_2.setMinimumSize(QSize(0, 40))
        self.indexwidget_2.setStyleSheet(u"QRadioButton{\n"
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
        self.horizontalLayout_3 = QHBoxLayout(self.indexwidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tmass_jh_radioButton = QRadioButton(self.indexwidget_2)
        self.tmass_jh_radioButton.setObjectName(u"tmass_jh_radioButton")
        self.tmass_jh_radioButton.setMinimumSize(QSize(0, 30))
        self.tmass_jh_radioButton.setFont(font)
        self.tmass_jh_radioButton.setChecked(True)

        self.horizontalLayout_3.addWidget(self.tmass_jh_radioButton)

        self.tmass_hk_radioButton = QRadioButton(self.indexwidget_2)
        self.tmass_hk_radioButton.setObjectName(u"tmass_hk_radioButton")
        self.tmass_hk_radioButton.setMinimumSize(QSize(0, 30))
        self.tmass_hk_radioButton.setFont(font)
        self.tmass_hk_radioButton.setChecked(False)

        self.horizontalLayout_3.addWidget(self.tmass_hk_radioButton)

        self.tmass_jk_radioButton = QRadioButton(self.indexwidget_2)
        self.tmass_jk_radioButton.setObjectName(u"tmass_jk_radioButton")

        self.horizontalLayout_3.addWidget(self.tmass_jk_radioButton)


        self.gridLayout_15.addWidget(self.indexwidget_2, 0, 0, 1, 2)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 30))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_11)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 9, 0, 6)
        self.tmass_showallBtn = QPushButton(self.frame_11)
        self.tmass_showallBtn.setObjectName(u"tmass_showallBtn")
        self.tmass_showallBtn.setMinimumSize(QSize(0, 30))
        self.tmass_showallBtn.setMaximumSize(QSize(16777215, 30))
        self.tmass_showallBtn.setIcon(icon7)

        self.gridLayout_16.addWidget(self.tmass_showallBtn, 0, 1, 1, 1)

        self.tmass_showBtn = QPushButton(self.frame_11)
        self.tmass_showBtn.setObjectName(u"tmass_showBtn")
        self.tmass_showBtn.setMinimumSize(QSize(0, 30))
        self.tmass_showBtn.setMaximumSize(QSize(16777215, 30))
        self.tmass_showBtn.setStyleSheet(u"QPushButton{\n"
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
        self.tmass_showBtn.setIcon(icon7)
        self.tmass_showBtn.setAutoDefault(True)

        self.gridLayout_16.addWidget(self.tmass_showBtn, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frame_11, 4, 0, 1, 2)

        self.tmass_range_lineEdit = QLineEdit(self.frame_10)
        self.tmass_range_lineEdit.setObjectName(u"tmass_range_lineEdit")
        self.tmass_range_lineEdit.setMinimumSize(QSize(0, 30))
        self.tmass_range_lineEdit.setMaximumSize(QSize(16777215, 30))
        self.tmass_range_lineEdit.setFont(font2)
        self.tmass_range_lineEdit.setClearButtonEnabled(True)

        self.gridLayout_15.addWidget(self.tmass_range_lineEdit, 2, 1, 1, 1)

        self.tmass_indexlabel = QLabel(self.frame_10)
        self.tmass_indexlabel.setObjectName(u"tmass_indexlabel")
        self.tmass_indexlabel.setMinimumSize(QSize(75, 0))
        self.tmass_indexlabel.setMaximumSize(QSize(75, 16777215))
        self.tmass_indexlabel.setFont(font)

        self.gridLayout_15.addWidget(self.tmass_indexlabel, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_10, 1, 0, 1, 1)

        self.frame_12 = QFrame(self.irsa_page)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 80))
        self.frame_12.setStyleSheet(u"QCheckBox{\n"
"color: #eeeeee;\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_12)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.tmass_ra_checkBox = QCheckBox(self.frame_12)
        self.tmass_ra_checkBox.setObjectName(u"tmass_ra_checkBox")
        self.tmass_ra_checkBox.setMinimumSize(QSize(90, 0))
        self.tmass_ra_checkBox.setMaximumSize(QSize(90, 16777215))
        self.tmass_ra_checkBox.setStyleSheet(u"")
        self.tmass_ra_checkBox.setChecked(True)

        self.gridLayout_17.addWidget(self.tmass_ra_checkBox, 0, 0, 1, 1)

        self.tmass_dec_checkBox = QCheckBox(self.frame_12)
        self.tmass_dec_checkBox.setObjectName(u"tmass_dec_checkBox")
        self.tmass_dec_checkBox.setMinimumSize(QSize(90, 0))
        self.tmass_dec_checkBox.setMaximumSize(QSize(90, 16777215))
        self.tmass_dec_checkBox.setStyleSheet(u"")
        self.tmass_dec_checkBox.setChecked(True)

        self.gridLayout_17.addWidget(self.tmass_dec_checkBox, 0, 1, 1, 1)

        self.tmass_magj_checkBox = QCheckBox(self.frame_12)
        self.tmass_magj_checkBox.setObjectName(u"tmass_magj_checkBox")
        self.tmass_magj_checkBox.setMinimumSize(QSize(90, 0))
        self.tmass_magj_checkBox.setMaximumSize(QSize(90, 16777215))
        self.tmass_magj_checkBox.setStyleSheet(u"")
        self.tmass_magj_checkBox.setChecked(True)

        self.gridLayout_17.addWidget(self.tmass_magj_checkBox, 0, 2, 1, 1)

        self.tmass_magh_checkBox = QCheckBox(self.frame_12)
        self.tmass_magh_checkBox.setObjectName(u"tmass_magh_checkBox")
        self.tmass_magh_checkBox.setMinimumSize(QSize(90, 0))
        self.tmass_magh_checkBox.setMaximumSize(QSize(90, 16777215))
        self.tmass_magh_checkBox.setStyleSheet(u"")
        self.tmass_magh_checkBox.setChecked(True)

        self.gridLayout_17.addWidget(self.tmass_magh_checkBox, 0, 3, 1, 1)

        self.tmass_magk_checkBox = QCheckBox(self.frame_12)
        self.tmass_magk_checkBox.setObjectName(u"tmass_magk_checkBox")
        self.tmass_magk_checkBox.setMinimumSize(QSize(90, 0))
        self.tmass_magk_checkBox.setMaximumSize(QSize(90, 16777215))
        self.tmass_magk_checkBox.setStyleSheet(u"")
        self.tmass_magk_checkBox.setChecked(True)

        self.gridLayout_17.addWidget(self.tmass_magk_checkBox, 0, 4, 1, 1)

        self.tmass_jsnr_checkBox = QCheckBox(self.frame_12)
        self.tmass_jsnr_checkBox.setObjectName(u"tmass_jsnr_checkBox")
        self.tmass_jsnr_checkBox.setMinimumSize(QSize(90, 0))
        self.tmass_jsnr_checkBox.setMaximumSize(QSize(90, 16777215))
        self.tmass_jsnr_checkBox.setStyleSheet(u"")
        self.tmass_jsnr_checkBox.setChecked(True)

        self.gridLayout_17.addWidget(self.tmass_jsnr_checkBox, 1, 0, 1, 1)

        self.tmass_hsnr_checkBox = QCheckBox(self.frame_12)
        self.tmass_hsnr_checkBox.setObjectName(u"tmass_hsnr_checkBox")
        self.tmass_hsnr_checkBox.setMinimumSize(QSize(90, 0))
        self.tmass_hsnr_checkBox.setMaximumSize(QSize(90, 16777215))
        self.tmass_hsnr_checkBox.setStyleSheet(u"")
        self.tmass_hsnr_checkBox.setChecked(True)

        self.gridLayout_17.addWidget(self.tmass_hsnr_checkBox, 1, 1, 1, 1)

        self.tmass_ksnr_checkBox = QCheckBox(self.frame_12)
        self.tmass_ksnr_checkBox.setObjectName(u"tmass_ksnr_checkBox")
        self.tmass_ksnr_checkBox.setMinimumSize(QSize(90, 0))
        self.tmass_ksnr_checkBox.setMaximumSize(QSize(90, 16777215))
        self.tmass_ksnr_checkBox.setStyleSheet(u"")
        self.tmass_ksnr_checkBox.setChecked(True)

        self.gridLayout_17.addWidget(self.tmass_ksnr_checkBox, 1, 2, 1, 1)

        self.tmass_jh_checkBox = QCheckBox(self.frame_12)
        self.tmass_jh_checkBox.setObjectName(u"tmass_jh_checkBox")
        self.tmass_jh_checkBox.setMinimumSize(QSize(90, 0))
        self.tmass_jh_checkBox.setMaximumSize(QSize(90, 16777215))
        self.tmass_jh_checkBox.setStyleSheet(u"")
        self.tmass_jh_checkBox.setChecked(True)

        self.gridLayout_17.addWidget(self.tmass_jh_checkBox, 1, 3, 1, 1)

        self.tmass_hk_checkBox = QCheckBox(self.frame_12)
        self.tmass_hk_checkBox.setObjectName(u"tmass_hk_checkBox")
        self.tmass_hk_checkBox.setMinimumSize(QSize(90, 0))
        self.tmass_hk_checkBox.setMaximumSize(QSize(90, 16777215))
        self.tmass_hk_checkBox.setStyleSheet(u"")
        self.tmass_hk_checkBox.setChecked(True)

        self.gridLayout_17.addWidget(self.tmass_hk_checkBox, 1, 4, 1, 1)

        self.tmass_jk_checkBox = QCheckBox(self.frame_12)
        self.tmass_jk_checkBox.setObjectName(u"tmass_jk_checkBox")
        self.tmass_jk_checkBox.setChecked(True)

        self.gridLayout_17.addWidget(self.tmass_jk_checkBox, 1, 5, 1, 1)


        self.gridLayout_4.addWidget(self.frame_12, 2, 0, 1, 1)

        self.irsa_tableWidget = QTableWidget(self.irsa_page)
        self.irsa_tableWidget.setObjectName(u"irsa_tableWidget")
        self.irsa_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_4.addWidget(self.irsa_tableWidget, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.irsa_page)
        self.wise_page = QWidget()
        self.wise_page.setObjectName(u"wise_page")
        self.gridLayout_21 = QGridLayout(self.wise_page)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.frame_15 = QFrame(self.wise_page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 60))
        self.frame_15.setMaximumSize(QSize(16777215, 80))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_15)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.irsalabel_wise = QLabel(self.frame_15)
        self.irsalabel_wise.setObjectName(u"irsalabel_wise")
        self.irsalabel_wise.setMinimumSize(QSize(90, 40))
        self.irsalabel_wise.setMaximumSize(QSize(90, 40))
        self.irsalabel_wise.setPixmap(QPixmap(u":/icon/icon/irsa.png"))
        self.irsalabel_wise.setScaledContents(True)

        self.gridLayout_20.addWidget(self.irsalabel_wise, 0, 0, 1, 1)

        self.wiselabel = QLabel(self.frame_15)
        self.wiselabel.setObjectName(u"wiselabel")
        self.wiselabel.setMinimumSize(QSize(90, 40))
        self.wiselabel.setMaximumSize(QSize(90, 40))
        self.wiselabel.setPixmap(QPixmap(u":/icon/icon/WISE_logo.png"))
        self.wiselabel.setScaledContents(True)

        self.gridLayout_20.addWidget(self.wiselabel, 0, 1, 1, 1)


        self.gridLayout_21.addWidget(self.frame_15, 0, 0, 1, 1)

        self.wise_tableWidget = QTableWidget(self.wise_page)
        self.wise_tableWidget.setObjectName(u"wise_tableWidget")
        self.wise_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_21.addWidget(self.wise_tableWidget, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.wise_page)
        self.gaia_page = QWidget()
        self.gaia_page.setObjectName(u"gaia_page")
        self.gridLayout_5 = QGridLayout(self.gaia_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gaia_tableWidget = QTableWidget(self.gaia_page)
        self.gaia_tableWidget.setObjectName(u"gaia_tableWidget")
        self.gaia_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_5.addWidget(self.gaia_tableWidget, 1, 0, 1, 1)

        self.frame_8 = QFrame(self.gaia_page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 60))
        self.frame_8.setMaximumSize(QSize(16777215, 60))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_8)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gaialabel = QLabel(self.frame_8)
        self.gaialabel.setObjectName(u"gaialabel")
        self.gaialabel.setMinimumSize(QSize(50, 50))
        self.gaialabel.setMaximumSize(QSize(50, 50))
        self.gaialabel.setPixmap(QPixmap(u":/icon/icon/Logo_Gaia.png"))
        self.gaialabel.setScaledContents(True)

        self.gridLayout_13.addWidget(self.gaialabel, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_5.addWidget(self.frame_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.gaia_page)
        self.ztf_page = QWidget()
        self.ztf_page.setObjectName(u"ztf_page")
        self.gridLayout_6 = QGridLayout(self.ztf_page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.ztf_tableWidget = QTableWidget(self.ztf_page)
        self.ztf_tableWidget.setObjectName(u"ztf_tableWidget")
        self.ztf_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_6.addWidget(self.ztf_tableWidget, 1, 0, 1, 2)

        self.frame_9 = QFrame(self.ztf_page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 60))
        self.frame_9.setMaximumSize(QSize(16777215, 60))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_9)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.irsalabel_2 = QLabel(self.frame_9)
        self.irsalabel_2.setObjectName(u"irsalabel_2")
        self.irsalabel_2.setMinimumSize(QSize(90, 40))
        self.irsalabel_2.setMaximumSize(QSize(90, 40))
        self.irsalabel_2.setPixmap(QPixmap(u":/icon/icon/irsa.png"))
        self.irsalabel_2.setScaledContents(True)

        self.gridLayout_14.addWidget(self.irsalabel_2, 0, 0, 1, 1)

        self.ztflabel = QLabel(self.frame_9)
        self.ztflabel.setObjectName(u"ztflabel")
        self.ztflabel.setMinimumSize(QSize(70, 40))
        self.ztflabel.setMaximumSize(QSize(70, 40))
        self.ztflabel.setPixmap(QPixmap(u":/icon/icon/ztf_logo.png"))
        self.ztflabel.setScaledContents(True)

        self.gridLayout_14.addWidget(self.ztflabel, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_9, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.ztf_page)
        self.colorindex_page = QWidget()
        self.colorindex_page.setObjectName(u"colorindex_page")
        self.gridLayout_3 = QGridLayout(self.colorindex_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.colorindex_page)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.rangelabel = QLabel(self.frame)
        self.rangelabel.setObjectName(u"rangelabel")
        self.rangelabel.setMinimumSize(QSize(75, 0))
        self.rangelabel.setMaximumSize(QSize(75, 16777215))
        self.rangelabel.setFont(font)

        self.gridLayout_10.addWidget(self.rangelabel, 2, 0, 1, 1)

        self.index_lineEdit = QLineEdit(self.frame)
        self.index_lineEdit.setObjectName(u"index_lineEdit")
        self.index_lineEdit.setMinimumSize(QSize(0, 30))
        self.index_lineEdit.setMaximumSize(QSize(16777215, 30))
        self.index_lineEdit.setFont(font2)
        self.index_lineEdit.setClearButtonEnabled(True)

        self.gridLayout_10.addWidget(self.index_lineEdit, 1, 1, 1, 1)

        self.indexwidget = QWidget(self.frame)
        self.indexwidget.setObjectName(u"indexwidget")
        self.indexwidget.setMinimumSize(QSize(0, 40))
        self.indexwidget.setStyleSheet(u"QRadioButton{\n"
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
        self.horizontalLayout_2 = QHBoxLayout(self.indexwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bv_radioButton = QRadioButton(self.indexwidget)
        self.bv_radioButton.setObjectName(u"bv_radioButton")
        self.bv_radioButton.setMinimumSize(QSize(0, 30))
        self.bv_radioButton.setFont(font)
        self.bv_radioButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.bv_radioButton)

        self.jh_radioButton = QRadioButton(self.indexwidget)
        self.jh_radioButton.setObjectName(u"jh_radioButton")
        self.jh_radioButton.setMinimumSize(QSize(0, 30))
        self.jh_radioButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.jh_radioButton)


        self.gridLayout_10.addWidget(self.indexwidget, 0, 0, 1, 2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 30))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 9, 0, 6)
        self.showallBtn = QPushButton(self.frame_3)
        self.showallBtn.setObjectName(u"showallBtn")
        self.showallBtn.setMinimumSize(QSize(0, 30))
        self.showallBtn.setMaximumSize(QSize(16777215, 30))
        self.showallBtn.setIcon(icon7)

        self.gridLayout_11.addWidget(self.showallBtn, 0, 1, 1, 1)

        self.showBtn = QPushButton(self.frame_3)
        self.showBtn.setObjectName(u"showBtn")
        self.showBtn.setMinimumSize(QSize(0, 30))
        self.showBtn.setMaximumSize(QSize(16777215, 30))
        self.showBtn.setStyleSheet(u"QPushButton{\n"
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
        self.showBtn.setIcon(icon7)
        self.showBtn.setAutoDefault(True)

        self.gridLayout_11.addWidget(self.showBtn, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_3, 4, 0, 1, 2)

        self.range_lineEdit = QLineEdit(self.frame)
        self.range_lineEdit.setObjectName(u"range_lineEdit")
        self.range_lineEdit.setMinimumSize(QSize(0, 30))
        self.range_lineEdit.setMaximumSize(QSize(16777215, 30))
        self.range_lineEdit.setFont(font2)
        self.range_lineEdit.setClearButtonEnabled(True)

        self.gridLayout_10.addWidget(self.range_lineEdit, 2, 1, 1, 1)

        self.indexlabel = QLabel(self.frame)
        self.indexlabel.setObjectName(u"indexlabel")
        self.indexlabel.setMinimumSize(QSize(75, 0))
        self.indexlabel.setMaximumSize(QSize(75, 16777215))
        self.indexlabel.setFont(font)

        self.gridLayout_10.addWidget(self.indexlabel, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.colorindex_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 80))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.ra_checkBox = QCheckBox(self.frame_5)
        self.ra_checkBox.setObjectName(u"ra_checkBox")
        self.ra_checkBox.setMinimumSize(QSize(90, 0))
        self.ra_checkBox.setMaximumSize(QSize(90, 16777215))
        self.ra_checkBox.setStyleSheet(u"QCheckBox{\n"
"color: #eeeeee;\n"
"}")
        self.ra_checkBox.setChecked(True)

        self.gridLayout_9.addWidget(self.ra_checkBox, 0, 0, 1, 1)

        self.dec_checkBox = QCheckBox(self.frame_5)
        self.dec_checkBox.setObjectName(u"dec_checkBox")
        self.dec_checkBox.setMinimumSize(QSize(90, 0))
        self.dec_checkBox.setMaximumSize(QSize(90, 16777215))
        self.dec_checkBox.setStyleSheet(u"QCheckBox{\n"
"color: #eeeeee;\n"
"}")
        self.dec_checkBox.setChecked(True)

        self.gridLayout_9.addWidget(self.dec_checkBox, 0, 1, 1, 1)

        self.otype_checkBox = QCheckBox(self.frame_5)
        self.otype_checkBox.setObjectName(u"otype_checkBox")
        self.otype_checkBox.setMinimumSize(QSize(90, 0))
        self.otype_checkBox.setMaximumSize(QSize(90, 16777215))
        self.otype_checkBox.setStyleSheet(u"QCheckBox{\n"
"color: #eeeeee;\n"
"}")
        self.otype_checkBox.setChecked(True)

        self.gridLayout_9.addWidget(self.otype_checkBox, 0, 2, 1, 1)

        self.stype_checkBox = QCheckBox(self.frame_5)
        self.stype_checkBox.setObjectName(u"stype_checkBox")
        self.stype_checkBox.setMinimumSize(QSize(90, 0))
        self.stype_checkBox.setMaximumSize(QSize(90, 16777215))
        self.stype_checkBox.setStyleSheet(u"QCheckBox{\n"
"color: #eeeeee;\n"
"}")
        self.stype_checkBox.setChecked(True)

        self.gridLayout_9.addWidget(self.stype_checkBox, 0, 3, 1, 1)

        self.magb_checkBox = QCheckBox(self.frame_5)
        self.magb_checkBox.setObjectName(u"magb_checkBox")
        self.magb_checkBox.setMinimumSize(QSize(90, 0))
        self.magb_checkBox.setMaximumSize(QSize(90, 16777215))
        self.magb_checkBox.setStyleSheet(u"QCheckBox{\n"
"color: #eeeeee;\n"
"}")
        self.magb_checkBox.setChecked(True)

        self.gridLayout_9.addWidget(self.magb_checkBox, 1, 0, 1, 1)

        self.magv_checkBox = QCheckBox(self.frame_5)
        self.magv_checkBox.setObjectName(u"magv_checkBox")
        self.magv_checkBox.setMinimumSize(QSize(90, 0))
        self.magv_checkBox.setMaximumSize(QSize(90, 16777215))
        self.magv_checkBox.setStyleSheet(u"QCheckBox{\n"
"color: #eeeeee;\n"
"}")
        self.magv_checkBox.setChecked(True)

        self.gridLayout_9.addWidget(self.magv_checkBox, 1, 1, 1, 1)

        self.bv_checkBox = QCheckBox(self.frame_5)
        self.bv_checkBox.setObjectName(u"bv_checkBox")
        self.bv_checkBox.setMinimumSize(QSize(90, 0))
        self.bv_checkBox.setMaximumSize(QSize(90, 16777215))
        self.bv_checkBox.setStyleSheet(u"QCheckBox{\n"
"color: #eeeeee;\n"
"}")
        self.bv_checkBox.setChecked(True)

        self.gridLayout_9.addWidget(self.bv_checkBox, 1, 2, 1, 1)

        self.magj_checkBox = QCheckBox(self.frame_5)
        self.magj_checkBox.setObjectName(u"magj_checkBox")
        self.magj_checkBox.setMinimumSize(QSize(90, 0))
        self.magj_checkBox.setMaximumSize(QSize(90, 16777215))
        self.magj_checkBox.setStyleSheet(u"QCheckBox{\n"
"color: #eeeeee;\n"
"}")
        self.magj_checkBox.setChecked(True)

        self.gridLayout_9.addWidget(self.magj_checkBox, 1, 3, 1, 1)

        self.magh_checkBox = QCheckBox(self.frame_5)
        self.magh_checkBox.setObjectName(u"magh_checkBox")
        self.magh_checkBox.setMinimumSize(QSize(90, 0))
        self.magh_checkBox.setMaximumSize(QSize(90, 16777215))
        self.magh_checkBox.setStyleSheet(u"QCheckBox{\n"
"color: #eeeeee;\n"
"}")
        self.magh_checkBox.setChecked(True)

        self.gridLayout_9.addWidget(self.magh_checkBox, 1, 4, 1, 1)

        self.jh_checkBox = QCheckBox(self.frame_5)
        self.jh_checkBox.setObjectName(u"jh_checkBox")
        self.jh_checkBox.setMinimumSize(QSize(90, 0))
        self.jh_checkBox.setMaximumSize(QSize(90, 16777215))
        self.jh_checkBox.setStyleSheet(u"QCheckBox{\n"
"color: #eeeeee;\n"
"}")
        self.jh_checkBox.setChecked(True)

        self.gridLayout_9.addWidget(self.jh_checkBox, 1, 5, 1, 1)


        self.gridLayout_3.addWidget(self.frame_5, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.colorindex_page)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"background: #2d3259;\n"
"gridline-color:black;\n"
"border-radius: 15px;\n"
"border-color: #000000;\n"
"padding: 10px;\n"
"font-size: 9pt;\n"
"color: #eeeeee;\n"
"}\n"
"\n"
"QTableWidget::item \n"
"        {   \n"
"            color: white;\n"
"            background:black;            \n"
"        }\n"
" QTableWidget::item:hover\n"
"        {   \n"
"            color: black;\n"
"            background:#ffaa00;            \n"
"        }\n"
" QTableWidget::item:focus\n"
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
"}\n"
"\n"
"QTableCornerButton::section { \n"
"background-color:#232326; \n"
"border-top-left-radius: 10px;\n"
"}\n"
"\n"
"")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSortingEnabled(True)

        self.gridLayout_3.addWidget(self.tableWidget, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.colorindex_page)

        self.gridLayout.addWidget(self.stackedWidget, 2, 2, 1, 1)

        resultwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(resultwindow)
        self.statusbar.setObjectName(u"statusbar")
        resultwindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.pointer_horizontalSlider, self.sim_bv_radioButton)
        QWidget.setTabOrder(self.sim_bv_radioButton, self.sim_gv_radioButton)
        QWidget.setTabOrder(self.sim_gv_radioButton, self.sim_ub_radioButton)
        QWidget.setTabOrder(self.sim_ub_radioButton, self.sim_gr_radioButton)
        QWidget.setTabOrder(self.sim_gr_radioButton, self.sim_iz_radioButton)
        QWidget.setTabOrder(self.sim_iz_radioButton, self.sim_index_lineEdit)
        QWidget.setTabOrder(self.sim_index_lineEdit, self.sim_range_lineEdit)
        QWidget.setTabOrder(self.sim_range_lineEdit, self.sim_showBtn)
        QWidget.setTabOrder(self.sim_showBtn, self.sim_showallBtn)
        QWidget.setTabOrder(self.sim_showallBtn, self.simbad_tableWidget)
        QWidget.setTabOrder(self.simbad_tableWidget, self.irsaBtn)
        QWidget.setTabOrder(self.irsaBtn, self.simbadBtn)
        QWidget.setTabOrder(self.simbadBtn, self.gaiaBtn)
        QWidget.setTabOrder(self.gaiaBtn, self.tmass_index_lineEdit)
        QWidget.setTabOrder(self.tmass_index_lineEdit, self.tmass_jh_radioButton)
        QWidget.setTabOrder(self.tmass_jh_radioButton, self.tmass_hk_radioButton)
        QWidget.setTabOrder(self.tmass_hk_radioButton, self.tmass_jk_radioButton)
        QWidget.setTabOrder(self.tmass_jk_radioButton, self.tmass_showallBtn)
        QWidget.setTabOrder(self.tmass_showallBtn, self.tmass_showBtn)
        QWidget.setTabOrder(self.tmass_showBtn, self.tmass_range_lineEdit)
        QWidget.setTabOrder(self.tmass_range_lineEdit, self.tmass_ra_checkBox)
        QWidget.setTabOrder(self.tmass_ra_checkBox, self.tmass_dec_checkBox)
        QWidget.setTabOrder(self.tmass_dec_checkBox, self.tmass_magj_checkBox)
        QWidget.setTabOrder(self.tmass_magj_checkBox, self.tmass_magh_checkBox)
        QWidget.setTabOrder(self.tmass_magh_checkBox, self.tmass_magk_checkBox)
        QWidget.setTabOrder(self.tmass_magk_checkBox, self.tmass_jsnr_checkBox)
        QWidget.setTabOrder(self.tmass_jsnr_checkBox, self.tmass_hsnr_checkBox)
        QWidget.setTabOrder(self.tmass_hsnr_checkBox, self.tmass_ksnr_checkBox)
        QWidget.setTabOrder(self.tmass_ksnr_checkBox, self.tmass_jh_checkBox)
        QWidget.setTabOrder(self.tmass_jh_checkBox, self.tmass_hk_checkBox)
        QWidget.setTabOrder(self.tmass_hk_checkBox, self.tmass_jk_checkBox)
        QWidget.setTabOrder(self.tmass_jk_checkBox, self.irsa_tableWidget)
        QWidget.setTabOrder(self.irsa_tableWidget, self.gaia_tableWidget)
        QWidget.setTabOrder(self.gaia_tableWidget, self.ztf_tableWidget)
        QWidget.setTabOrder(self.ztf_tableWidget, self.index_lineEdit)
        QWidget.setTabOrder(self.index_lineEdit, self.bv_radioButton)
        QWidget.setTabOrder(self.bv_radioButton, self.jh_radioButton)
        QWidget.setTabOrder(self.jh_radioButton, self.showallBtn)
        QWidget.setTabOrder(self.showallBtn, self.showBtn)
        QWidget.setTabOrder(self.showBtn, self.range_lineEdit)
        QWidget.setTabOrder(self.range_lineEdit, self.ra_checkBox)
        QWidget.setTabOrder(self.ra_checkBox, self.dec_checkBox)
        QWidget.setTabOrder(self.dec_checkBox, self.otype_checkBox)
        QWidget.setTabOrder(self.otype_checkBox, self.stype_checkBox)
        QWidget.setTabOrder(self.stype_checkBox, self.magb_checkBox)
        QWidget.setTabOrder(self.magb_checkBox, self.magv_checkBox)
        QWidget.setTabOrder(self.magv_checkBox, self.bv_checkBox)
        QWidget.setTabOrder(self.bv_checkBox, self.magj_checkBox)
        QWidget.setTabOrder(self.magj_checkBox, self.magh_checkBox)
        QWidget.setTabOrder(self.magh_checkBox, self.jh_checkBox)
        QWidget.setTabOrder(self.jh_checkBox, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.ztfBtn)

        self.retranslateUi(resultwindow)

        self.irsaBtn.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(resultwindow)
    # setupUi

    def retranslateUi(self, resultwindow):
        resultwindow.setWindowTitle(QCoreApplication.translate("resultwindow", u"Search Results", None))
        self.pointerlabel.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Pointer size:</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">FOV :</span></p></body></html>", None))
        self.fov_lineEdit.setText("")
        self.genindexBtn.setText("")
        self.simbadBtn.setText("")
        self.irsaBtn.setText("")
        self.wiseBtn.setText("")
        self.gaiaBtn.setText("")
        self.ztfBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#eeeeee;\">GENERAL INFORMATION OF THE MAIN OBJECT</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">MAIN ID</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">RA / DEC</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">OBJ TYPE</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">SP TYPE</span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">MAG</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#eeeeee;\">I</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#eeeeee;\">J</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#eeeeee;\">G</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#eeeeee;\">H</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#eeeeee;\">V</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#eeeeee;\">U</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#eeeeee;\">B</span></p></body></html>", None))
        self.magb_lineEdit.setText("")
        self.label_17.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#eeeeee;\">R</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#eeeeee;\">K</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Tycho ID</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">HIP ID</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">TIC ID</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">2MASS ID</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">WISE ID</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#eeeeee;\">GAIA DR3 ID</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">ATO ID</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">CRTS ID</span></p></body></html>", None))
        self.label.setText("")
        self.rangelabel_2.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Range \u00b1: </span></p></body></html>", None))
        self.sim_bv_radioButton.setText(QCoreApplication.translate("resultwindow", u"B-V", None))
        self.sim_gv_radioButton.setText(QCoreApplication.translate("resultwindow", u"G-V", None))
        self.sim_ub_radioButton.setText(QCoreApplication.translate("resultwindow", u"U-B", None))
        self.sim_gr_radioButton.setText(QCoreApplication.translate("resultwindow", u"g-r", None))
        self.sim_iz_radioButton.setText(QCoreApplication.translate("resultwindow", u"i-z", None))
        self.sim_showallBtn.setText(QCoreApplication.translate("resultwindow", u"Show All Data", None))
        self.sim_showBtn.setText(QCoreApplication.translate("resultwindow", u"Show Filtered Data", None))
        self.indexlabel_2.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Index Value: </span></p></body></html>", None))
        self.irsalabel.setText("")
        self.twomasslabel.setText("")
        self.tmass_rangelabel.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Range \u00b1: </span></p></body></html>", None))
        self.tmass_jh_radioButton.setText(QCoreApplication.translate("resultwindow", u"J-H", None))
        self.tmass_hk_radioButton.setText(QCoreApplication.translate("resultwindow", u"H-K", None))
        self.tmass_jk_radioButton.setText(QCoreApplication.translate("resultwindow", u"J-K", None))
        self.tmass_showallBtn.setText(QCoreApplication.translate("resultwindow", u"Show All Data", None))
        self.tmass_showBtn.setText(QCoreApplication.translate("resultwindow", u"Show Filtered Data", None))
        self.tmass_indexlabel.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Index Value: </span></p></body></html>", None))
        self.tmass_ra_checkBox.setText(QCoreApplication.translate("resultwindow", u"RA", None))
        self.tmass_dec_checkBox.setText(QCoreApplication.translate("resultwindow", u"DEC", None))
        self.tmass_magj_checkBox.setText(QCoreApplication.translate("resultwindow", u"Mag J", None))
        self.tmass_magh_checkBox.setText(QCoreApplication.translate("resultwindow", u"Mag H", None))
        self.tmass_magk_checkBox.setText(QCoreApplication.translate("resultwindow", u"Mag K", None))
        self.tmass_jsnr_checkBox.setText(QCoreApplication.translate("resultwindow", u"J_snr", None))
        self.tmass_hsnr_checkBox.setText(QCoreApplication.translate("resultwindow", u"H_snr", None))
        self.tmass_ksnr_checkBox.setText(QCoreApplication.translate("resultwindow", u"K_snr", None))
        self.tmass_jh_checkBox.setText(QCoreApplication.translate("resultwindow", u"J-H", None))
        self.tmass_hk_checkBox.setText(QCoreApplication.translate("resultwindow", u"H-K", None))
        self.tmass_jk_checkBox.setText(QCoreApplication.translate("resultwindow", u"J-K", None))
        self.irsalabel_wise.setText("")
        self.wiselabel.setText("")
        self.gaialabel.setText("")
        self.irsalabel_2.setText("")
        self.ztflabel.setText("")
        self.rangelabel.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Range \u00b1: </span></p></body></html>", None))
        self.bv_radioButton.setText(QCoreApplication.translate("resultwindow", u"B-V", None))
        self.jh_radioButton.setText(QCoreApplication.translate("resultwindow", u"J-H", None))
        self.showallBtn.setText(QCoreApplication.translate("resultwindow", u"Show All Data", None))
        self.showBtn.setText(QCoreApplication.translate("resultwindow", u"Show Filtered Data", None))
        self.indexlabel.setText(QCoreApplication.translate("resultwindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Index Value: </span></p></body></html>", None))
        self.ra_checkBox.setText(QCoreApplication.translate("resultwindow", u"RA", None))
        self.dec_checkBox.setText(QCoreApplication.translate("resultwindow", u"DEC", None))
        self.otype_checkBox.setText(QCoreApplication.translate("resultwindow", u"Object Type", None))
        self.stype_checkBox.setText(QCoreApplication.translate("resultwindow", u"Spectral Type", None))
        self.magb_checkBox.setText(QCoreApplication.translate("resultwindow", u"Mag B", None))
        self.magv_checkBox.setText(QCoreApplication.translate("resultwindow", u"Mag V", None))
        self.bv_checkBox.setText(QCoreApplication.translate("resultwindow", u"B-V", None))
        self.magj_checkBox.setText(QCoreApplication.translate("resultwindow", u"Mag J", None))
        self.magh_checkBox.setText(QCoreApplication.translate("resultwindow", u"Mag H", None))
        self.jh_checkBox.setText(QCoreApplication.translate("resultwindow", u"J-H", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("resultwindow", u"MAIN ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("resultwindow", u"Object Type", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("resultwindow", u"Spectral Type", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("resultwindow", u"B-V Index", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("resultwindow", u"J-H Index", None));
    # retranslateUi

