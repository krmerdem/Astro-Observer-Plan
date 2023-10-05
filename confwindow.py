# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QWidget)
import icon_rc
import icon_rc

class Ui_ConfWindow(object):
    def setupUi(self, ConfWindow):
        if not ConfWindow.objectName():
            ConfWindow.setObjectName(u"ConfWindow")
        ConfWindow.resize(400, 747)
        ConfWindow.setStyleSheet(u"QMainWindow {\n"
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
        self.centralwidget = QWidget(ConfWindow)
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
        self.loc_groupBox = QGroupBox(self.centralwidget)
        self.loc_groupBox.setObjectName(u"loc_groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loc_groupBox.sizePolicy().hasHeightForWidth())
        self.loc_groupBox.setSizePolicy(sizePolicy)
        self.loc_groupBox.setMinimumSize(QSize(380, 200))
        self.loc_groupBox.setMaximumSize(QSize(550, 16777215))
        self.loc_groupBox.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.loc_groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_22 = QLabel(self.loc_groupBox)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(10, 16777215))

        self.gridLayout_3.addWidget(self.label_22, 1, 5, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer, 0, 4, 1, 1)

        self.lat_spinbox_min = QSpinBox(self.loc_groupBox)
        self.lat_spinbox_min.setObjectName(u"lat_spinbox_min")
        self.lat_spinbox_min.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        self.lat_spinbox_min.setFont(font)
        self.lat_spinbox_min.setMaximum(59)
        self.lat_spinbox_min.setValue(50)

        self.gridLayout_3.addWidget(self.lat_spinbox_min, 1, 4, 1, 1)

        self.long_spinbox_min = QSpinBox(self.loc_groupBox)
        self.long_spinbox_min.setObjectName(u"long_spinbox_min")
        self.long_spinbox_min.setMinimumSize(QSize(0, 30))
        self.long_spinbox_min.setFont(font)
        self.long_spinbox_min.setMaximum(59)
        self.long_spinbox_min.setValue(46)

        self.gridLayout_3.addWidget(self.long_spinbox_min, 2, 4, 1, 1)

        self.label_23 = QLabel(self.loc_groupBox)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(10, 16777215))

        self.gridLayout_3.addWidget(self.label_23, 2, 5, 1, 1)

        self.label_24 = QLabel(self.loc_groupBox)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(10, 16777215))

        self.gridLayout_3.addWidget(self.label_24, 1, 7, 1, 1)

        self.long_dspinbox_sec = QDoubleSpinBox(self.loc_groupBox)
        self.long_dspinbox_sec.setObjectName(u"long_dspinbox_sec")
        self.long_dspinbox_sec.setMinimumSize(QSize(0, 30))
        self.long_dspinbox_sec.setFont(font)
        self.long_dspinbox_sec.setMaximum(59.990000000000002)
        self.long_dspinbox_sec.setValue(45.000000000000000)

        self.gridLayout_3.addWidget(self.long_dspinbox_sec, 2, 6, 1, 1)

        self.label_25 = QLabel(self.loc_groupBox)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(10, 16777215))

        self.gridLayout_3.addWidget(self.label_25, 2, 7, 1, 1)

        self.lat_comboBox = QComboBox(self.loc_groupBox)
        self.lat_comboBox.addItem("")
        self.lat_comboBox.addItem("")
        self.lat_comboBox.setObjectName(u"lat_comboBox")
        self.lat_comboBox.setMinimumSize(QSize(40, 30))
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.lat_comboBox.setFont(font1)

        self.gridLayout_3.addWidget(self.lat_comboBox, 1, 8, 1, 1)

        self.lat_dspinbox_sec = QDoubleSpinBox(self.loc_groupBox)
        self.lat_dspinbox_sec.setObjectName(u"lat_dspinbox_sec")
        self.lat_dspinbox_sec.setMinimumSize(QSize(0, 30))
        self.lat_dspinbox_sec.setFont(font)
        self.lat_dspinbox_sec.setMaximum(59.990000000000002)
        self.lat_dspinbox_sec.setValue(37.000000000000000)

        self.gridLayout_3.addWidget(self.lat_dspinbox_sec, 1, 6, 1, 1)

        self.label_21 = QLabel(self.loc_groupBox)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(10, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        self.label_21.setFont(font2)

        self.gridLayout_3.addWidget(self.label_21, 2, 3, 1, 1)

        self.label_9 = QLabel(self.loc_groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setMaximumSize(QSize(10, 16777215))

        self.gridLayout_3.addWidget(self.label_9, 3, 8, 1, 1)

        self.label_3 = QLabel(self.loc_groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(75, 0))
        self.label_3.setMaximumSize(QSize(75, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        self.label_3.setFont(font3)

        self.gridLayout_3.addWidget(self.label_3, 3, 1, 1, 1)

        self.long_comboBox = QComboBox(self.loc_groupBox)
        self.long_comboBox.addItem("")
        self.long_comboBox.addItem("")
        self.long_comboBox.setObjectName(u"long_comboBox")
        self.long_comboBox.setMinimumSize(QSize(40, 30))
        self.long_comboBox.setFont(font1)

        self.gridLayout_3.addWidget(self.long_comboBox, 2, 8, 1, 1)

        self.long_spinbox_deg = QSpinBox(self.loc_groupBox)
        self.long_spinbox_deg.setObjectName(u"long_spinbox_deg")
        self.long_spinbox_deg.setMinimumSize(QSize(0, 30))
        self.long_spinbox_deg.setFont(font)
        self.long_spinbox_deg.setMaximum(180)
        self.long_spinbox_deg.setValue(32)

        self.gridLayout_3.addWidget(self.long_spinbox_deg, 2, 2, 1, 1)

        self.label_2 = QLabel(self.loc_groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(75, 0))
        self.label_2.setMaximumSize(QSize(75, 16777215))
        self.label_2.setFont(font3)

        self.gridLayout_3.addWidget(self.label_2, 2, 1, 1, 1)

        self.elev_lineEdit = QLineEdit(self.loc_groupBox)
        self.elev_lineEdit.setObjectName(u"elev_lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.elev_lineEdit.sizePolicy().hasHeightForWidth())
        self.elev_lineEdit.setSizePolicy(sizePolicy1)
        self.elev_lineEdit.setMinimumSize(QSize(0, 30))
        self.elev_lineEdit.setFont(font)
        self.elev_lineEdit.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.elev_lineEdit, 3, 2, 1, 6)

        self.label_20 = QLabel(self.loc_groupBox)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(10, 16777215))
        self.label_20.setFont(font2)

        self.gridLayout_3.addWidget(self.label_20, 1, 3, 1, 1)

        self.lat_spinbox_deg = QSpinBox(self.loc_groupBox)
        self.lat_spinbox_deg.setObjectName(u"lat_spinbox_deg")
        self.lat_spinbox_deg.setMinimumSize(QSize(0, 30))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(11)
        font4.setBold(False)
        self.lat_spinbox_deg.setFont(font4)
        self.lat_spinbox_deg.setMinimum(0)
        self.lat_spinbox_deg.setMaximum(90)
        self.lat_spinbox_deg.setValue(39)

        self.gridLayout_3.addWidget(self.lat_spinbox_deg, 1, 2, 1, 1)

        self.label_28 = QLabel(self.loc_groupBox)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(30, 30))
        self.label_28.setMaximumSize(QSize(30, 30))
        self.label_28.setPixmap(QPixmap(u":/icon/icon/earth.png"))
        self.label_28.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_28, 1, 0, 1, 1)

        self.label_29 = QLabel(self.loc_groupBox)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(30, 30))
        self.label_29.setMaximumSize(QSize(30, 30))
        self.label_29.setPixmap(QPixmap(u":/icon/icon/earth.png"))
        self.label_29.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_29, 2, 0, 1, 1)

        self.label_40 = QLabel(self.loc_groupBox)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(30, 30))
        self.label_40.setMaximumSize(QSize(30, 30))
        self.label_40.setPixmap(QPixmap(u":/icon/icon/elev.png"))
        self.label_40.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_40, 3, 0, 1, 1)

        self.label = QLabel(self.loc_groupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(75, 0))
        self.label.setMaximumSize(QSize(75, 16777215))
        self.label.setFont(font3)

        self.gridLayout_3.addWidget(self.label, 1, 1, 1, 1)

        self.utcBox = QComboBox(self.loc_groupBox)
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.addItem("")
        self.utcBox.setObjectName(u"utcBox")
        self.utcBox.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.utcBox.sizePolicy().hasHeightForWidth())
        self.utcBox.setSizePolicy(sizePolicy1)
        self.utcBox.setMinimumSize(QSize(0, 30))
        self.utcBox.setMaximumSize(QSize(16777215, 30))
        self.utcBox.setFont(font4)
        self.utcBox.setStyleSheet(u"")
        self.utcBox.setEditable(False)
        self.utcBox.setDuplicatesEnabled(False)

        self.gridLayout_3.addWidget(self.utcBox, 4, 2, 1, 6)

        self.label_18 = QLabel(self.loc_groupBox)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(75, 30))
        self.label_18.setMaximumSize(QSize(75, 30))
        self.label_18.setFont(font3)

        self.gridLayout_3.addWidget(self.label_18, 4, 1, 1, 1)

        self.label_31 = QLabel(self.loc_groupBox)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(30, 30))
        self.label_31.setMaximumSize(QSize(30, 30))
        self.label_31.setPixmap(QPixmap(u":/icon/icon/utc.png"))
        self.label_31.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_31, 4, 0, 1, 1)


        self.gridLayout.addWidget(self.loc_groupBox, 0, 0, 1, 1)

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

        self.gridLayout.addWidget(self.confirmBtn, 2, 0, 1, 1)

        self.teleslim_groupBox = QGroupBox(self.centralwidget)
        self.teleslim_groupBox.setObjectName(u"teleslim_groupBox")
        sizePolicy.setHeightForWidth(self.teleslim_groupBox.sizePolicy().hasHeightForWidth())
        self.teleslim_groupBox.setSizePolicy(sizePolicy)
        self.teleslim_groupBox.setMinimumSize(QSize(380, 130))
        self.teleslim_groupBox.setMaximumSize(QSize(550, 16777215))
        self.teleslim_groupBox.setStyleSheet(u"")
        self.gridLayout_8 = QGridLayout(self.teleslim_groupBox)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_16 = QLabel(self.teleslim_groupBox)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(10, 16777215))
        self.label_16.setFont(font2)

        self.gridLayout_8.addWidget(self.label_16, 2, 3, 1, 1)

        self.label_27 = QLabel(self.teleslim_groupBox)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(10, 16777215))
        self.label_27.setFont(font2)

        self.gridLayout_8.addWidget(self.label_27, 1, 3, 1, 1)

        self.label_17 = QLabel(self.teleslim_groupBox)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(75, 0))
        self.label_17.setMaximumSize(QSize(75, 16777215))
        self.label_17.setFont(font3)

        self.gridLayout_8.addWidget(self.label_17, 2, 1, 1, 1)

        self.label_26 = QLabel(self.teleslim_groupBox)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(75, 0))
        self.label_26.setMaximumSize(QSize(75, 16777215))
        self.label_26.setFont(font3)

        self.gridLayout_8.addWidget(self.label_26, 1, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_4, 0, 2, 1, 1)

        self.label_41 = QLabel(self.teleslim_groupBox)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(30, 30))
        self.label_41.setMaximumSize(QSize(30, 30))
        self.label_41.setPixmap(QPixmap(u":/icon/icon/telescope.png"))
        self.label_41.setScaledContents(True)

        self.gridLayout_8.addWidget(self.label_41, 1, 0, 1, 1)

        self.label_42 = QLabel(self.teleslim_groupBox)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(30, 30))
        self.label_42.setMaximumSize(QSize(30, 30))
        self.label_42.setPixmap(QPixmap(u":/icon/icon/telescope.png"))
        self.label_42.setScaledContents(True)

        self.gridLayout_8.addWidget(self.label_42, 2, 0, 1, 1)

        self.tmin_lineEdit = QLineEdit(self.teleslim_groupBox)
        self.tmin_lineEdit.setObjectName(u"tmin_lineEdit")
        self.tmin_lineEdit.setMinimumSize(QSize(0, 30))
        self.tmin_lineEdit.setMaximumSize(QSize(16777215, 30))
        self.tmin_lineEdit.setFont(font)

        self.gridLayout_8.addWidget(self.tmin_lineEdit, 1, 2, 1, 1)

        self.tmax_lineEdit = QLineEdit(self.teleslim_groupBox)
        self.tmax_lineEdit.setObjectName(u"tmax_lineEdit")
        self.tmax_lineEdit.setMinimumSize(QSize(0, 30))
        self.tmax_lineEdit.setMaximumSize(QSize(16777215, 30))
        self.tmax_lineEdit.setFont(font)

        self.gridLayout_8.addWidget(self.tmax_lineEdit, 2, 2, 1, 1)


        self.gridLayout.addWidget(self.teleslim_groupBox, 1, 0, 1, 1)

        ConfWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ConfWindow)
        self.statusbar.setObjectName(u"statusbar")
        ConfWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ConfWindow)

        self.utcBox.setCurrentIndex(17)


        QMetaObject.connectSlotsByName(ConfWindow)
    # setupUi

    def retranslateUi(self, ConfWindow):
        ConfWindow.setWindowTitle(QCoreApplication.translate("ConfWindow", u"Astro Observer Plan- Location and Other Settings", None))
        self.loc_groupBox.setTitle(QCoreApplication.translate("ConfWindow", u"Location", None))
        self.label_22.setText(QCoreApplication.translate("ConfWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">'</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("ConfWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">'</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("ConfWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">''</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("ConfWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">''</span></p></body></html>", None))
        self.lat_comboBox.setItemText(0, QCoreApplication.translate("ConfWindow", u"N", None))
        self.lat_comboBox.setItemText(1, QCoreApplication.translate("ConfWindow", u"S", None))

        self.label_21.setText(QCoreApplication.translate("ConfWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">\u00b0</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("ConfWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">m</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("ConfWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Elevation:</span></p></body></html>", None))
        self.long_comboBox.setItemText(0, QCoreApplication.translate("ConfWindow", u"E", None))
        self.long_comboBox.setItemText(1, QCoreApplication.translate("ConfWindow", u"W", None))

        self.label_2.setText(QCoreApplication.translate("ConfWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Longitude:</span></p></body></html>", None))
        self.elev_lineEdit.setText(QCoreApplication.translate("ConfWindow", u"1256.69", None))
        self.label_20.setText(QCoreApplication.translate("ConfWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">\u00b0</span></p></body></html>", None))
        self.label_28.setText("")
        self.label_29.setText("")
        self.label_40.setText("")
        self.label.setText(QCoreApplication.translate("ConfWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Latitude:</span></p></body></html>", None))
        self.utcBox.setItemText(0, QCoreApplication.translate("ConfWindow", u"\u221212:00", None))
        self.utcBox.setItemText(1, QCoreApplication.translate("ConfWindow", u"\u221211:00", None))
        self.utcBox.setItemText(2, QCoreApplication.translate("ConfWindow", u"\u221210:00", None))
        self.utcBox.setItemText(3, QCoreApplication.translate("ConfWindow", u"\u221209:30", None))
        self.utcBox.setItemText(4, QCoreApplication.translate("ConfWindow", u"\u221209:00", None))
        self.utcBox.setItemText(5, QCoreApplication.translate("ConfWindow", u"\u221208:00", None))
        self.utcBox.setItemText(6, QCoreApplication.translate("ConfWindow", u"\u221207:00", None))
        self.utcBox.setItemText(7, QCoreApplication.translate("ConfWindow", u"\u221206:00", None))
        self.utcBox.setItemText(8, QCoreApplication.translate("ConfWindow", u"\u221205:00", None))
        self.utcBox.setItemText(9, QCoreApplication.translate("ConfWindow", u"\u221204:00", None))
        self.utcBox.setItemText(10, QCoreApplication.translate("ConfWindow", u"\u221203:30", None))
        self.utcBox.setItemText(11, QCoreApplication.translate("ConfWindow", u"\u221203:00", None))
        self.utcBox.setItemText(12, QCoreApplication.translate("ConfWindow", u"\u221202:00", None))
        self.utcBox.setItemText(13, QCoreApplication.translate("ConfWindow", u"\u221201:00", None))
        self.utcBox.setItemText(14, QCoreApplication.translate("ConfWindow", u"00:00", None))
        self.utcBox.setItemText(15, QCoreApplication.translate("ConfWindow", u"+01:00", None))
        self.utcBox.setItemText(16, QCoreApplication.translate("ConfWindow", u"+02:00", None))
        self.utcBox.setItemText(17, QCoreApplication.translate("ConfWindow", u"+03:00", None))
        self.utcBox.setItemText(18, QCoreApplication.translate("ConfWindow", u"+03:30", None))
        self.utcBox.setItemText(19, QCoreApplication.translate("ConfWindow", u"+04:00", None))
        self.utcBox.setItemText(20, QCoreApplication.translate("ConfWindow", u"+04:30", None))
        self.utcBox.setItemText(21, QCoreApplication.translate("ConfWindow", u"+05:00", None))
        self.utcBox.setItemText(22, QCoreApplication.translate("ConfWindow", u"+05:30", None))
        self.utcBox.setItemText(23, QCoreApplication.translate("ConfWindow", u"+05:45", None))
        self.utcBox.setItemText(24, QCoreApplication.translate("ConfWindow", u"+06:00", None))
        self.utcBox.setItemText(25, QCoreApplication.translate("ConfWindow", u"+06:30", None))
        self.utcBox.setItemText(26, QCoreApplication.translate("ConfWindow", u"+07:00", None))
        self.utcBox.setItemText(27, QCoreApplication.translate("ConfWindow", u"+08:00", None))
        self.utcBox.setItemText(28, QCoreApplication.translate("ConfWindow", u"+08:45", None))
        self.utcBox.setItemText(29, QCoreApplication.translate("ConfWindow", u"+09:00", None))
        self.utcBox.setItemText(30, QCoreApplication.translate("ConfWindow", u"+09:30", None))
        self.utcBox.setItemText(31, QCoreApplication.translate("ConfWindow", u"+10:00", None))
        self.utcBox.setItemText(32, QCoreApplication.translate("ConfWindow", u"+10:30", None))
        self.utcBox.setItemText(33, QCoreApplication.translate("ConfWindow", u"+11:00", None))
        self.utcBox.setItemText(34, QCoreApplication.translate("ConfWindow", u"+12:00", None))
        self.utcBox.setItemText(35, QCoreApplication.translate("ConfWindow", u"+12:45", None))
        self.utcBox.setItemText(36, QCoreApplication.translate("ConfWindow", u"+13:00", None))
        self.utcBox.setItemText(37, QCoreApplication.translate("ConfWindow", u"+14:00", None))

        self.label_18.setText(QCoreApplication.translate("ConfWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">UTC:</span></p></body></html>", None))
        self.label_31.setText("")
        self.confirmBtn.setText(QCoreApplication.translate("ConfWindow", u"Confirm", None))
        self.teleslim_groupBox.setTitle(QCoreApplication.translate("ConfWindow", u"Telescope limits", None))
        self.label_16.setText(QCoreApplication.translate("ConfWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">\u00b0</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("ConfWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">\u00b0</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("ConfWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Alt max:</span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("ConfWindow", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Alt min:</span></p></body></html>", None))
        self.label_41.setText("")
        self.label_42.setText("")
    # retranslateUi

