# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wormhole_update.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_wormhole_update_tool(object):
    def setupUi(self, wormhole_update_tool):
        if wormhole_update_tool.objectName():
            wormhole_update_tool.setObjectName(u"wormhole_update_tool")
        wormhole_update_tool.resize(736, 599)
        self.Wormhole_update_tool_label = QLabel(wormhole_update_tool)
        self.Wormhole_update_tool_label.setObjectName(u"Wormhole_update_tool_label")
        self.Wormhole_update_tool_label.setGeometry(QRect(30, 20, 241, 31))
        self.textb_log = QTextBrowser(wormhole_update_tool)
        self.textb_log.setObjectName(u"textb_log")
        self.textb_log.setGeometry(QRect(30, 410, 671, 111))
        self.layoutWidget = QWidget(wormhole_update_tool)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(90, 150, 251, 81))
        self.wh_ssh_server = QFormLayout(self.layoutWidget)
        self.wh_ssh_server.setObjectName(u"wh_ssh_server")
        self.wh_ssh_server.setContentsMargins(0, 0, 0, 0)
        self.label_port = QLabel(self.layoutWidget)
        self.label_port.setObjectName(u"label_port")

        self.wh_ssh_server.setWidget(0, QFormLayout.LabelRole, self.label_port)

        self.input_port = QLineEdit(self.layoutWidget)
        self.input_port.setObjectName(u"input_port")

        self.wh_ssh_server.setWidget(0, QFormLayout.FieldRole, self.input_port)

        self.label_id = QLabel(self.layoutWidget)
        self.label_id.setObjectName(u"label_id")

        self.wh_ssh_server.setWidget(1, QFormLayout.LabelRole, self.label_id)

        self.input_id = QLineEdit(self.layoutWidget)
        self.input_id.setObjectName(u"input_id")

        self.wh_ssh_server.setWidget(1, QFormLayout.FieldRole, self.input_id)

        self.label_pw = QLabel(self.layoutWidget)
        self.label_pw.setObjectName(u"label_pw")

        self.wh_ssh_server.setWidget(2, QFormLayout.LabelRole, self.label_pw)

        self.input_pw = QLineEdit(self.layoutWidget)
        self.input_pw.setObjectName(u"input_pw")

        self.wh_ssh_server.setWidget(2, QFormLayout.FieldRole, self.input_pw)

        self.pushb_server_login = QPushButton(wormhole_update_tool)
        self.pushb_server_login.setObjectName(u"pushb_server_login")
        self.pushb_server_login.setEnabled(False)
        self.pushb_server_login.setGeometry(QRect(190, 240, 151, 31))
        self.pushb_server_login.setFocusPolicy(Qt.NoFocus)
        self.label_ssh_connect_info = QLabel(wormhole_update_tool)
        self.label_ssh_connect_info.setObjectName(u"label_ssh_connect_info")
        self.label_ssh_connect_info.setGeometry(QRect(50, 120, 151, 16))
        self.pushb_wh_update = QPushButton(wormhole_update_tool)
        self.pushb_wh_update.setObjectName(u"pushb_wh_update")
        self.pushb_wh_update.setEnabled(False)
        self.pushb_wh_update.setGeometry(QRect(550, 360, 151, 31))
        self.pushb_wh_update.setFocusPolicy(Qt.NoFocus)
        self.pushb_wh_update.setAcceptDrops(False)
        self.label_wh_update = QLabel(wormhole_update_tool)
        self.label_wh_update.setObjectName(u"label_wh_update")
        self.label_wh_update.setGeometry(QRect(60, 290, 151, 16))
        self.layoutWidget1 = QWidget(wormhole_update_tool)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(90, 320, 601, 31))
        self.update_file = QGridLayout(self.layoutWidget1)
        self.update_file.setObjectName(u"update_file")
        self.update_file.setContentsMargins(0, 0, 0, 0)
        self.label_update_file = QLabel(self.layoutWidget1)
        self.label_update_file.setObjectName(u"label_update_file")

        self.update_file.addWidget(self.label_update_file, 0, 0, 1, 1)

        self.input_update_file_path = QLineEdit(self.layoutWidget1)
        self.input_update_file_path.setObjectName(u"input_update_file_path")
        self.input_update_file_path.setEnabled(False)

        self.update_file.addWidget(self.input_update_file_path, 0, 1, 1, 1)

        self.toolb_find_file = QToolButton(self.layoutWidget1)
        self.toolb_find_file.setObjectName(u"toolb_find_file")
        self.toolb_find_file.setEnabled(False)

        self.update_file.addWidget(self.toolb_find_file, 0, 2, 1, 1)

        self.input_host = QLineEdit(wormhole_update_tool)
        self.input_host.setObjectName(u"input_host")
        self.input_host.setGeometry(QRect(169, 70, 531, 20))
        self.label_host = QLabel(wormhole_update_tool)
        self.label_host.setObjectName(u"label_host")
        self.label_host.setGeometry(QRect(50, 70, 111, 20))
        self.label_http_connect_info = QLabel(wormhole_update_tool)
        self.label_http_connect_info.setObjectName(u"label_http_connect_info")
        self.label_http_connect_info.setGeometry(QRect(400, 120, 171, 16))
        self.layoutWidget_2 = QWidget(wormhole_update_tool)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(440, 150, 251, 81))
        self.wh_http = QFormLayout(self.layoutWidget_2)
        self.wh_http.setObjectName(u"wh_http")
        self.wh_http.setContentsMargins(0, 0, 0, 0)
        self.label_http_port = QLabel(self.layoutWidget_2)
        self.label_http_port.setObjectName(u"label_http_port")

        self.wh_http.setWidget(0, QFormLayout.LabelRole, self.label_http_port)

        self.input_http_port = QLineEdit(self.layoutWidget_2)
        self.input_http_port.setObjectName(u"input_http_port")
        self.input_http_port.setEnabled(False)

        self.wh_http.setWidget(0, QFormLayout.FieldRole, self.input_http_port)

        self.label_http_id = QLabel(self.layoutWidget_2)
        self.label_http_id.setObjectName(u"label_http_id")

        self.wh_http.setWidget(1, QFormLayout.LabelRole, self.label_http_id)

        self.input_http_id = QLineEdit(self.layoutWidget_2)
        self.input_http_id.setObjectName(u"input_http_id")
        self.input_http_id.setEnabled(False)

        self.wh_http.setWidget(1, QFormLayout.FieldRole, self.input_http_id)

        self.label_http_pw = QLabel(self.layoutWidget_2)
        self.label_http_pw.setObjectName(u"label_http_pw")

        self.wh_http.setWidget(2, QFormLayout.LabelRole, self.label_http_pw)

        self.input_http_pw = QLineEdit(self.layoutWidget_2)
        self.input_http_pw.setObjectName(u"input_http_pw")
        self.input_http_pw.setEnabled(False)

        self.wh_http.setWidget(2, QFormLayout.FieldRole, self.input_http_pw)

        self.pushb_http_login = QPushButton(wormhole_update_tool)
        self.pushb_http_login.setObjectName(u"pushb_http_login")
        self.pushb_http_login.setEnabled(False)
        self.pushb_http_login.setGeometry(QRect(610, 240, 81, 31))
        self.pushb_http_login.setFocusPolicy(Qt.NoFocus)
        self.wh_version = QLabel(wormhole_update_tool)
        self.wh_version.setObjectName(u"wh_version")
        self.wh_version.setGeometry(QRect(405, 10, 291, 41))
        self.wh_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushb_wormhole_hompage = QPushButton(wormhole_update_tool)
        self.pushb_wormhole_hompage.setObjectName(u"pushb_wormhole_hompage")
        self.pushb_wormhole_hompage.setEnabled(False)
        self.pushb_wormhole_hompage.setGeometry(QRect(440, 240, 161, 31))
        self.pushb_wormhole_hompage.setFocusPolicy(Qt.NoFocus)
        self.pushb_reset = QPushButton(wormhole_update_tool)
        self.pushb_reset.setObjectName(u"pushb_reset")
        self.pushb_reset.setGeometry(QRect(30, 540, 75, 23))
        self.pushb_reset.setFocusPolicy(Qt.NoFocus)
        self.pushb_wh_status_stop = QPushButton(wormhole_update_tool)
        self.pushb_wh_status_stop.setObjectName(u"pushb_wh_status_stop")
        self.pushb_wh_status_stop.setEnabled(False)
        self.pushb_wh_status_stop.setGeometry(QRect(560, 540, 141, 23))
        self.pushb_wh_status_stop.setFocusPolicy(Qt.NoFocus)
        self.pushb_wh_status_start = QPushButton(wormhole_update_tool)
        self.pushb_wh_status_start.setObjectName(u"pushb_wh_status_start")
        self.pushb_wh_status_start.setEnabled(False)
        self.pushb_wh_status_start.setGeometry(QRect(410, 540, 141, 23))
        self.pushb_wh_status_start.setFocusPolicy(Qt.NoFocus)

        self.retranslateUi(wormhole_update_tool)

        QMetaObject.connectSlotsByName(wormhole_update_tool)
    # setupUi

    def retranslateUi(self, wormhole_update_tool):
        wormhole_update_tool.setWindowTitle(QCoreApplication.translate("wormhole_update_tool", u"Form", None))
        self.Wormhole_update_tool_label.setText(QCoreApplication.translate("wormhole_update_tool", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">WORMHOLE UPDATE TOOL</span></p></body></html>", None))
        self.label_port.setText(QCoreApplication.translate("wormhole_update_tool", u"ssh port", None))
        self.label_id.setText(QCoreApplication.translate("wormhole_update_tool", u"Server ID", None))
        self.label_pw.setText(QCoreApplication.translate("wormhole_update_tool", u"Server PW", None))
        self.pushb_server_login.setText(QCoreApplication.translate("wormhole_update_tool", u"Server Log-in", None))
        self.label_ssh_connect_info.setText(QCoreApplication.translate("wormhole_update_tool", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">SSH Connect</span></p></body></html>", None))
        self.pushb_wh_update.setText(QCoreApplication.translate("wormhole_update_tool", u"wormhole_update", None))
        self.label_wh_update.setText(QCoreApplication.translate("wormhole_update_tool", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Wormhole_Update</span></p></body></html>", None))
        self.label_update_file.setText(QCoreApplication.translate("wormhole_update_tool", u"Update_file", None))
        self.toolb_find_file.setText(QCoreApplication.translate("wormhole_update_tool", u"...", None))
        self.label_host.setText(QCoreApplication.translate("wormhole_update_tool", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Server Host/IP</span></p></body></html>", None))
        self.label_http_connect_info.setText(QCoreApplication.translate("wormhole_update_tool", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Wormhole Homepage</span></p></body></html>", None))
        self.label_http_port.setText(QCoreApplication.translate("wormhole_update_tool", u"Http port", None))
        self.label_http_id.setText(QCoreApplication.translate("wormhole_update_tool", u"Admin ID", None))
        self.label_http_pw.setText(QCoreApplication.translate("wormhole_update_tool", u"Admin PW", None))
        self.pushb_http_login.setText(QCoreApplication.translate("wormhole_update_tool", u"sign_in", None))
        self.wh_version.setText(QCoreApplication.translate("wormhole_update_tool", u"Before connecting to the Wormhole", None))
        self.pushb_wormhole_hompage.setText(QCoreApplication.translate("wormhole_update_tool", u"Wormhole Homepage", None))
        self.pushb_reset.setText(QCoreApplication.translate("wormhole_update_tool", u"Reset", None))
        self.pushb_wh_status_stop.setText(QCoreApplication.translate("wormhole_update_tool", u"Wormhole Server Stop", None))
        self.pushb_wh_status_start.setText(QCoreApplication.translate("wormhole_update_tool", u"Wormhole Server Start", None))
    # retranslateUi

