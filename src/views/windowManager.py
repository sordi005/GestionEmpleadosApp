# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowManager.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget #centralwidget{\n"
"	background-color:#1E1E1E;\n"
"\n"
"}\n"
"\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widgetBarraMenu = QWidget(self.centralwidget)
        self.widgetBarraMenu.setObjectName(u"widgetBarraMenu")
        self.widgetBarraMenu.setStyleSheet(u"")
        self.verticalLayout_15 = QVBoxLayout(self.widgetBarraMenu)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frameBarraLefMenu = QFrame(self.widgetBarraMenu)
        self.frameBarraLefMenu.setObjectName(u"frameBarraLefMenu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameBarraLefMenu.sizePolicy().hasHeightForWidth())
        self.frameBarraLefMenu.setSizePolicy(sizePolicy)
        self.frameBarraLefMenu.setToolTipDuration(-1)
        self.frameBarraLefMenu.setStyleSheet(u"QFrame {\n"
"    /* Color de fondo del frame */\n"
"    background: #121212;\n"
"    \n"
"    /* Borde: ancho, estilo y color */\n"
"    border: 1px solid #333333;\n"
"    \n"
"    /* Esquinas redondeadas (radio en p\u00edxeles) */\n"
"    border-radius: 1px;\n"
"    \n"
"    /* Espacio interno entre el borde y el contenido */\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    /* Estilo de borde */\n"
"    border: 1px solid #a0a0a0;\n"
"    \n"
"    /* Radio de esquinas */\n"
"    border-radius: 3px;\n"
"    \n"
"    /* Margen superior para separar del t\u00edtulo */\n"
"    margin-top: 10px;\n"
"    \n"
"    /* Espacio interno arriba del contenido */\n"
"    padding-top: 15px;\n"
"    \n"
"    /* Fondo con gradiente lineal (de arriba a abajo) */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #f9f9f9, stop:1 #e0e0e0);\n"
"}\n"
"\n"
"/* Estilo espec\u00edfico para el T\u00cdTULO del GroupBox */\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin"
                        ";  /* Posici\u00f3n relativa al margen */\n"
"    left: 10px;                /* Desplazamiento horizontal */\n"
"    padding: 0 5px;            /* Espacio interno (arriba/abajo, izquierda/derecha) */\n"
"    color: #505050;            /* Color del texto */\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    /* Fondo con gradiente azul */\n"
"    background: #1A5BFF\n"
"    \n"
"    /* Color del texto */\n"
"    color: white;\n"
"    \n"
"    /* Borde del bot\u00f3n */\n"
"    border: 1px solid #2980b9;\n"
"    \n"
"    /* Esquinas redondeadas */\n"
"    border-radius: 4px;\n"
"    \n"
"    /* Espacio interno (arriba/abajo, izquierda/derecha) */\n"
"    padding: 1px 10px;\n"
"    \n"
"    /* Ancho m\u00ednimo */\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"\n"
"")
        self.frameBarraLefMenu.setFrameShape(QFrame.StyledPanel)
        self.frameBarraLefMenu.setFrameShadow(QFrame.Raised)
        self.frameBarraLefMenu.setLineWidth(1)
        self.verticalLayout_8 = QVBoxLayout(self.frameBarraLefMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.groupBoxBotones = QGroupBox(self.frameBarraLefMenu)
        self.groupBoxBotones.setObjectName(u"groupBoxBotones")
        sizePolicy.setHeightForWidth(self.groupBoxBotones.sizePolicy().hasHeightForWidth())
        self.groupBoxBotones.setSizePolicy(sizePolicy)
        self.verticalLayout_10 = QVBoxLayout(self.groupBoxBotones)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pushButton_6 = QPushButton(self.groupBoxBotones)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_10.addWidget(self.pushButton_6, 0, Qt.AlignLeft)

        self.pushButton_7 = QPushButton(self.groupBoxBotones)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_10.addWidget(self.pushButton_7, 0, Qt.AlignLeft|Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.pushButton_8 = QPushButton(self.groupBoxBotones)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_10.addWidget(self.pushButton_8, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.groupBoxBotones, 0, Qt.AlignLeft|Qt.AlignTop)

        self.pushButton = QPushButton(self.frameBarraLefMenu)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_8.addWidget(self.pushButton, 0, Qt.AlignRight)

        self.frameinferior = QFrame(self.frameBarraLefMenu)
        self.frameinferior.setObjectName(u"frameinferior")
        self.frameinferior.setFrameShape(QFrame.StyledPanel)
        self.frameinferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameinferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.subWidgetBarraMenu1_2 = QWidget(self.frameinferior)
        self.subWidgetBarraMenu1_2.setObjectName(u"subWidgetBarraMenu1_2")
        self.verticalLayout_2 = QVBoxLayout(self.subWidgetBarraMenu1_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 5, 0)
        self.label_4 = QLabel(self.subWidgetBarraMenu1_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_3 = QLabel(self.subWidgetBarraMenu1_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)


        self.horizontalLayout.addWidget(self.subWidgetBarraMenu1_2)

        self.subWidgetBarraMenu1 = QWidget(self.frameinferior)
        self.subWidgetBarraMenu1.setObjectName(u"subWidgetBarraMenu1")
        self.verticalLayout = QVBoxLayout(self.subWidgetBarraMenu1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 0, 0)
        self.label_2 = QLabel(self.subWidgetBarraMenu1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(self.subWidgetBarraMenu1)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout.addWidget(self.subWidgetBarraMenu1)


        self.verticalLayout_8.addWidget(self.frameinferior, 0, Qt.AlignBottom)


        self.verticalLayout_15.addWidget(self.frameBarraLefMenu, 0, Qt.AlignLeft)


        self.horizontalLayout_3.addWidget(self.widgetBarraMenu, 0, Qt.AlignLeft)

        self.LayoputRightMain = QVBoxLayout()
        self.LayoputRightMain.setObjectName(u"LayoputRightMain")

        self.horizontalLayout_3.addLayout(self.LayoputRightMain)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBoxBotones.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

