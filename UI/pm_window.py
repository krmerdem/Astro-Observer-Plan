# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pm_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFrame,
    QGridLayout, QHeaderView, QLabel, QSizePolicy,
    QTableWidget, QTableWidgetItem, QTextBrowser, QWidget)
import icon_rc

class Ui_pecaut_mamajek(object):
    def setupUi(self, pecaut_mamajek):
        if not pecaut_mamajek.objectName():
            pecaut_mamajek.setObjectName(u"pecaut_mamajek")
        pecaut_mamajek.resize(800, 466)
        pecaut_mamajek.setMinimumSize(QSize(800, 465))
        icon = QIcon()
        icon.addFile(u":/icon/icon/parameters.png", QSize(), QIcon.Normal, QIcon.Off)
        pecaut_mamajek.setWindowIcon(icon)
        pecaut_mamajek.setStyleSheet(u"QDialog {\n"
"background: #121212;\n"
"}\n"
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
"            background:#ffaa00;            \n"
"        }\n"
" QTableView::item:focus\n"
"        {   \n"
"            color: #eeeeee;\n"
"            background:#6316AC;            \n"
"        }\n"
"\n"
"QTableView::item:selected {\n"
"    color: #eeeeee;\n"
"    background: #6316AC;\n"
"}\n"
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
"border-top-left"
                        "-radius: 10px;\n"
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
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
""
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
"    background: rgb(45, 45, 68);\n"
"    height: 14px;\n"
"    margin: 0 15px 0 15px;\n"
"    border-radius: "
                        "0px;\n"
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
"    background-color: rgb(59, 59, 90);\n"
"    width: 15px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-"
                        "right-radius: 7px;\n"
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
"")
        self.gridLayout = QGridLayout(pecaut_mamajek)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(pecaut_mamajek)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 60))
        self.frame_2.setMaximumSize(QSize(16777215, 60))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"background: #000221;\n"
"border-radius: 15px;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"color: #eeeeee;\n"
"}")

        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        self.pm_tableWidget = QTableWidget(pecaut_mamajek)
        self.pm_tableWidget.setObjectName(u"pm_tableWidget")
        self.pm_tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.pm_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pm_tableWidget.setShowGrid(True)
        self.pm_tableWidget.setGridStyle(Qt.DashLine)
        self.pm_tableWidget.verticalHeader().setProperty("showSortIndicator", False)

        self.gridLayout.addWidget(self.pm_tableWidget, 1, 0, 1, 1)

        self.textBrowser = QTextBrowser(pecaut_mamajek)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(0, 55))
        self.textBrowser.setMaximumSize(QSize(16777215, 55))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        self.textBrowser.setFont(font1)
        self.textBrowser.setStyleSheet(u"QTextBrowser {\n"
"color: #eeeeee;\n"
"background-color:#000221;\n"
"border: 1px solid;\n"
"border-radius: 3px;\n"
"}")

        self.gridLayout.addWidget(self.textBrowser, 2, 0, 1, 1)


        self.retranslateUi(pecaut_mamajek)

        QMetaObject.connectSlotsByName(pecaut_mamajek)
    # setupUi

    def retranslateUi(self, pecaut_mamajek):
        pecaut_mamajek.setWindowTitle(QCoreApplication.translate("pecaut_mamajek", u"Pecaut and Mamajek Teff-SpT", None))
        self.label.setText(QCoreApplication.translate("pecaut_mamajek", u"<html><head/><body><p align=\"center\">A Modern Mean Dwarf Stellar Color and Effective Temperature Sequence</p></body></html>", None))
        self.textBrowser.setHtml(QCoreApplication.translate("pecaut_mamajek", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The color indexes of the star selected in the relevant catalog are taken and scanned in the EEM_dwarf_UBVIJHK_colors_Teff table. The two color index values closest to the color index in the catalog are selected from the EEM_dwarf_UBVIJHK_colors_Teff table and the corresponding parameters are displayed.</p></body></html>", None))
    # retranslateUi

