# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableView, QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1007, 682)
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background-color:transparent;\n"
"	background:transparent;\n"
"	padding:0;\n"
"	margin:0;\n"
"	color:#fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	\n"
"	\n"
"	background-color: rgb(154, 208, 194);\n"
"\n"
"}\n"
"\n"
"#leftMenuSubContainer, #rightMenuSubContainer, #centerMenuSubContainer{\n"
"	\n"
"	background-color: rgb(38, 80, 115);\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"	text-align:left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"#centertMenuSubContainer QPushButton{\n"
"	text-align:left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"#centerMenuContainer{\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"#frame_9 {\n"
"	\n"
"	background-color: rgb(126, 126, 126);\n"
"	\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#headerContainer{\n"
"	\n"
"	background-color: rgb(44, 49, 60);\n"
"	border-color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"#graphBtn{\n"
"	\n"
"	color: rgb"
                        "(170, 0, 0);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QSize(24, 24))
        self.homeBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.homeBtn)

        self.addProductBtn = QPushButton(self.frame_2)
        self.addProductBtn.setObjectName(u"addProductBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.addProductBtn.sizePolicy().hasHeightForWidth())
        self.addProductBtn.setSizePolicy(sizePolicy1)
        self.addProductBtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addProductBtn.setIcon(icon1)
        self.addProductBtn.setIconSize(QSize(24, 24))
        self.addProductBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.addProductBtn)

        self.deleteProductBtn = QPushButton(self.frame_2)
        self.deleteProductBtn.setObjectName(u"deleteProductBtn")
        sizePolicy1.setHeightForWidth(self.deleteProductBtn.sizePolicy().hasHeightForWidth())
        self.deleteProductBtn.setSizePolicy(sizePolicy1)
        self.deleteProductBtn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/minus-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteProductBtn.setIcon(icon2)
        self.deleteProductBtn.setIconSize(QSize(24, 24))
        self.deleteProductBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.deleteProductBtn)

        self.updateProductBtn = QPushButton(self.frame_2)
        self.updateProductBtn.setObjectName(u"updateProductBtn")
        sizePolicy1.setHeightForWidth(self.updateProductBtn.sizePolicy().hasHeightForWidth())
        self.updateProductBtn.setSizePolicy(sizePolicy1)
        self.updateProductBtn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.updateProductBtn.setIcon(icon3)
        self.updateProductBtn.setIconSize(QSize(24, 24))
        self.updateProductBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.updateProductBtn)

        self.viewProductsBtn = QPushButton(self.frame_2)
        self.viewProductsBtn.setObjectName(u"viewProductsBtn")
        sizePolicy1.setHeightForWidth(self.viewProductsBtn.sizePolicy().hasHeightForWidth())
        self.viewProductsBtn.setSizePolicy(sizePolicy1)
        self.viewProductsBtn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/package.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.viewProductsBtn.setIcon(icon4)
        self.viewProductsBtn.setIconSize(QSize(24, 24))
        self.viewProductsBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.viewProductsBtn)

        self.dataBtn = QPushButton(self.frame_2)
        self.dataBtn.setObjectName(u"dataBtn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dataBtn.setIcon(icon5)
        self.dataBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.dataBtn)

        self.graphBtn = QPushButton(self.frame_2)
        self.graphBtn.setObjectName(u"graphBtn")
        sizePolicy1.setHeightForWidth(self.graphBtn.sizePolicy().hasHeightForWidth())
        self.graphBtn.setSizePolicy(sizePolicy1)
        self.graphBtn.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/slack.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.graphBtn.setIcon(icon6)
        self.graphBtn.setIconSize(QSize(24, 24))
        self.graphBtn.setCheckable(True)

        self.verticalLayout_4.addWidget(self.graphBtn)

        self.searchBtn = QPushButton(self.frame_2)
        self.searchBtn.setObjectName(u"searchBtn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.searchBtn.setIcon(icon7)
        self.searchBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.searchBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.settingBtn = QPushButton(self.frame_3)
        self.settingBtn.setObjectName(u"settingBtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingBtn.setIcon(icon8)
        self.settingBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.settingBtn)

        self.infoBtn = QPushButton(self.frame_3)
        self.infoBtn.setObjectName(u"infoBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon9)
        self.infoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon10)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer)

        self.centerMenuContainer = QWidget(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setMinimumSize(QSize(90, 0))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(90, 0))
        self.verticalLayout_9 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 0, 0, 0)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 16, 0, -1)
        self.homeBtn_2 = QPushButton(self.frame_4)
        self.homeBtn_2.setObjectName(u"homeBtn_2")
        sizePolicy1.setHeightForWidth(self.homeBtn_2.sizePolicy().hasHeightForWidth())
        self.homeBtn_2.setSizePolicy(sizePolicy1)
        self.homeBtn_2.setStyleSheet(u"")
        self.homeBtn_2.setIcon(icon)
        self.homeBtn_2.setIconSize(QSize(24, 24))
        self.homeBtn_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.homeBtn_2)

        self.addProductBtn_2 = QPushButton(self.frame_4)
        self.addProductBtn_2.setObjectName(u"addProductBtn_2")
        sizePolicy1.setHeightForWidth(self.addProductBtn_2.sizePolicy().hasHeightForWidth())
        self.addProductBtn_2.setSizePolicy(sizePolicy1)
        self.addProductBtn_2.setStyleSheet(u"")
        self.addProductBtn_2.setIcon(icon1)
        self.addProductBtn_2.setIconSize(QSize(24, 24))
        self.addProductBtn_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.addProductBtn_2)

        self.deleteProductBtn_2 = QPushButton(self.frame_4)
        self.deleteProductBtn_2.setObjectName(u"deleteProductBtn_2")
        sizePolicy1.setHeightForWidth(self.deleteProductBtn_2.sizePolicy().hasHeightForWidth())
        self.deleteProductBtn_2.setSizePolicy(sizePolicy1)
        self.deleteProductBtn_2.setStyleSheet(u"")
        self.deleteProductBtn_2.setIcon(icon2)
        self.deleteProductBtn_2.setIconSize(QSize(24, 24))
        self.deleteProductBtn_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.deleteProductBtn_2)

        self.updateProductBtn_2 = QPushButton(self.frame_4)
        self.updateProductBtn_2.setObjectName(u"updateProductBtn_2")
        sizePolicy1.setHeightForWidth(self.updateProductBtn_2.sizePolicy().hasHeightForWidth())
        self.updateProductBtn_2.setSizePolicy(sizePolicy1)
        self.updateProductBtn_2.setStyleSheet(u"")
        self.updateProductBtn_2.setIcon(icon3)
        self.updateProductBtn_2.setIconSize(QSize(24, 24))
        self.updateProductBtn_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.updateProductBtn_2)

        self.viewProductsBtn_2 = QPushButton(self.frame_4)
        self.viewProductsBtn_2.setObjectName(u"viewProductsBtn_2")
        sizePolicy1.setHeightForWidth(self.viewProductsBtn_2.sizePolicy().hasHeightForWidth())
        self.viewProductsBtn_2.setSizePolicy(sizePolicy1)
        self.viewProductsBtn_2.setStyleSheet(u"")
        self.viewProductsBtn_2.setIcon(icon4)
        self.viewProductsBtn_2.setIconSize(QSize(24, 24))
        self.viewProductsBtn_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.viewProductsBtn_2)

        self.dataBtn_2 = QPushButton(self.frame_4)
        self.dataBtn_2.setObjectName(u"dataBtn_2")
        sizePolicy1.setHeightForWidth(self.dataBtn_2.sizePolicy().hasHeightForWidth())
        self.dataBtn_2.setSizePolicy(sizePolicy1)
        self.dataBtn_2.setIcon(icon5)
        self.dataBtn_2.setIconSize(QSize(24, 24))
        self.dataBtn_2.setFlat(False)

        self.verticalLayout_5.addWidget(self.dataBtn_2)

        self.graphBtn_2 = QPushButton(self.frame_4)
        self.graphBtn_2.setObjectName(u"graphBtn_2")
        sizePolicy1.setHeightForWidth(self.graphBtn_2.sizePolicy().hasHeightForWidth())
        self.graphBtn_2.setSizePolicy(sizePolicy1)
        self.graphBtn_2.setStyleSheet(u"")
        self.graphBtn_2.setIcon(icon6)
        self.graphBtn_2.setIconSize(QSize(24, 24))
        self.graphBtn_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.graphBtn_2)

        self.searchBtn_2 = QPushButton(self.frame_4)
        self.searchBtn_2.setObjectName(u"searchBtn_2")
        sizePolicy1.setHeightForWidth(self.searchBtn_2.sizePolicy().hasHeightForWidth())
        self.searchBtn_2.setSizePolicy(sizePolicy1)
        self.searchBtn_2.setIcon(icon7)
        self.searchBtn_2.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.searchBtn_2)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.frame_5 = QFrame(self.centerMenuSubContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 14)
        self.settingBtn_2 = QPushButton(self.frame_5)
        self.settingBtn_2.setObjectName(u"settingBtn_2")
        sizePolicy1.setHeightForWidth(self.settingBtn_2.sizePolicy().hasHeightForWidth())
        self.settingBtn_2.setSizePolicy(sizePolicy1)
        self.settingBtn_2.setIcon(icon8)
        self.settingBtn_2.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.settingBtn_2)

        self.infoBtn_2 = QPushButton(self.frame_5)
        self.infoBtn_2.setObjectName(u"infoBtn_2")
        sizePolicy1.setHeightForWidth(self.infoBtn_2.sizePolicy().hasHeightForWidth())
        self.infoBtn_2.setSizePolicy(sizePolicy1)
        self.infoBtn_2.setLayoutDirection(Qt.LeftToRight)
        self.infoBtn_2.setIcon(icon9)
        self.infoBtn_2.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.infoBtn_2)

        self.helpBtn_2 = QPushButton(self.frame_5)
        self.helpBtn_2.setObjectName(u"helpBtn_2")
        sizePolicy1.setHeightForWidth(self.helpBtn_2.sizePolicy().hasHeightForWidth())
        self.helpBtn_2.setSizePolicy(sizePolicy1)
        self.helpBtn_2.setIcon(icon10)
        self.helpBtn_2.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.helpBtn_2)


        self.verticalLayout_9.addWidget(self.frame_5)


        self.verticalLayout_6.addWidget(self.centerMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy2)
        self.mainBodyContainer.setStyleSheet(u"background-color: rgb(219, 255, 215);")
        self.verticalLayout_11 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setStyleSheet(u"background-color: rgb(154, 208, 194);")
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.menuButton = QPushButton(self.frame_6)
        self.menuButton.setObjectName(u"menuButton")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon11)
        self.menuButton.setIconSize(QSize(24, 24))
        self.menuButton.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.menuButton)


        self.horizontalLayout_5.addWidget(self.frame_6, 0, Qt.AlignLeft)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.frame_7)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon12)
        self.pushButton_6.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.frame_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon13)
        self.pushButton_5.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.pushButton_5)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignHCenter)

        self.frame_8 = QFrame(self.headerContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_8)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon14)
        self.minimizeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.minimizeBtn, 0, Qt.AlignHCenter)

        self.restoreBtn = QPushButton(self.frame_8)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon15)
        self.restoreBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.restoreBtn, 0, Qt.AlignHCenter)

        self.closeBtn = QPushButton(self.frame_8)
        self.closeBtn.setObjectName(u"closeBtn")
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon16)
        self.closeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.closeBtn, 0, Qt.AlignHCenter)


        self.horizontalLayout_5.addWidget(self.frame_8, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.mainBodyContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.addProductPage = QWidget()
        self.addProductPage.setObjectName(u"addProductPage")
        self.verticalLayout_21 = QVBoxLayout(self.addProductPage)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.dataTimeWidget = QWidget(self.addProductPage)
        self.dataTimeWidget.setObjectName(u"dataTimeWidget")
        sizePolicy1.setHeightForWidth(self.dataTimeWidget.sizePolicy().hasHeightForWidth())
        self.dataTimeWidget.setSizePolicy(sizePolicy1)
        self.dataTimeWidget.setMinimumSize(QSize(100, 25))
        self.horizontalLayout_10 = QHBoxLayout(self.dataTimeWidget)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.dataTimeWidget)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_9)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(170, 0, 0);")

        self.horizontalLayout_16.addWidget(self.label_5)

        self.displayDate = QLabel(self.widget_9)
        self.displayDate.setObjectName(u"displayDate")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.displayDate.sizePolicy().hasHeightForWidth())
        self.displayDate.setSizePolicy(sizePolicy4)
        self.displayDate.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_16.addWidget(self.displayDate)


        self.horizontalLayout_10.addWidget(self.widget_9, 0, Qt.AlignHCenter)

        self.widget_8 = QWidget(self.dataTimeWidget)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_15.setSpacing(2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget_8)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        self.label_11.setMinimumSize(QSize(0, 0))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: rgb(170, 0, 0);")

        self.horizontalLayout_15.addWidget(self.label_11)

        self.displayTime = QLabel(self.widget_8)
        self.displayTime.setObjectName(u"displayTime")
        sizePolicy4.setHeightForWidth(self.displayTime.sizePolicy().hasHeightForWidth())
        self.displayTime.setSizePolicy(sizePolicy4)
        self.displayTime.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_15.addWidget(self.displayTime)


        self.horizontalLayout_10.addWidget(self.widget_8, 0, Qt.AlignHCenter)


        self.verticalLayout_21.addWidget(self.dataTimeWidget, 0, Qt.AlignRight|Qt.AlignTop)

        self.widget = QWidget(self.addProductPage)
        self.widget.setObjectName(u"widget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy5)
        self.widget.setStyleSheet(u"")
        self.verticalLayout_22 = QVBoxLayout(self.widget)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy6)
        self.widget_6.setStyleSheet(u"QWidget{\n"
"border-radius: 5px;\n"
"}\n"
"#inputProductName, #inputProductPrice, #inputProductQuantity, #inputProductCompany{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	border-bottom: 2px solid rgba(85, 170, 255);\n"
"	border-radius: 10px;\n"
"	padding-bottom: 7px;\n"
"    padding-left: 20px;\n"
"	padding-right: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 3px solid rgb(85, 170, 255);\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.verticalLayout_23 = QVBoxLayout(self.widget_6)
        self.verticalLayout_23.setSpacing(30)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget_6)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
        self.horizontalLayout_11 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(130, 25))
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel{\n"
"background-color: rgb(1, 163, 164);\n"
"text-align: center;\n"
"}#")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label)

        self.inputProductName = QLineEdit(self.widget_2)
        self.inputProductName.setObjectName(u"inputProductName")
        sizePolicy1.setHeightForWidth(self.inputProductName.sizePolicy().hasHeightForWidth())
        self.inputProductName.setSizePolicy(sizePolicy1)
        self.inputProductName.setMinimumSize(QSize(232, 30))
        self.inputProductName.setMaximumSize(QSize(250, 30))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.inputProductName.setFont(font2)
        self.inputProductName.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.inputProductName)


        self.verticalLayout_23.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget_6)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy3.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy3)
        self.horizontalLayout_12 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(130, 25))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgb(1, 163, 164);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_2)

        self.inputProductPrice = QLineEdit(self.widget_3)
        self.inputProductPrice.setObjectName(u"inputProductPrice")
        sizePolicy1.setHeightForWidth(self.inputProductPrice.sizePolicy().hasHeightForWidth())
        self.inputProductPrice.setSizePolicy(sizePolicy1)
        self.inputProductPrice.setMinimumSize(QSize(232, 30))
        self.inputProductPrice.setMaximumSize(QSize(250, 30))
        self.inputProductPrice.setFont(font1)
        self.inputProductPrice.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.inputProductPrice)


        self.verticalLayout_23.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_6)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy3.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy3)
        self.horizontalLayout_13 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy7)
        self.label_3.setMinimumSize(QSize(130, 25))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: rgb(1, 163, 164);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_3)

        self.inputProductQuantity = QLineEdit(self.widget_4)
        self.inputProductQuantity.setObjectName(u"inputProductQuantity")
        sizePolicy1.setHeightForWidth(self.inputProductQuantity.sizePolicy().hasHeightForWidth())
        self.inputProductQuantity.setSizePolicy(sizePolicy1)
        self.inputProductQuantity.setMinimumSize(QSize(232, 30))
        self.inputProductQuantity.setMaximumSize(QSize(250, 30))
        self.inputProductQuantity.setFont(font1)
        self.inputProductQuantity.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.inputProductQuantity)


        self.verticalLayout_23.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_6)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy3.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy3)
        self.horizontalLayout_14 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMinimumSize(QSize(130, 25))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color: rgb(1, 163, 164);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_4)

        self.inputProductCompany = QLineEdit(self.widget_5)
        self.inputProductCompany.setObjectName(u"inputProductCompany")
        sizePolicy1.setHeightForWidth(self.inputProductCompany.sizePolicy().hasHeightForWidth())
        self.inputProductCompany.setSizePolicy(sizePolicy1)
        self.inputProductCompany.setMinimumSize(QSize(232, 30))
        self.inputProductCompany.setMaximumSize(QSize(250, 30))
        self.inputProductCompany.setFont(font1)
        self.inputProductCompany.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.inputProductCompany)


        self.verticalLayout_23.addWidget(self.widget_5)

        self.widget_10 = QWidget(self.widget_6)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(50, 0))
        self.verticalLayout_25 = QVBoxLayout(self.widget_10)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.addProductBtn_3 = QPushButton(self.widget_10)
        self.addProductBtn_3.setObjectName(u"addProductBtn_3")
        sizePolicy.setHeightForWidth(self.addProductBtn_3.sizePolicy().hasHeightForWidth())
        self.addProductBtn_3.setSizePolicy(sizePolicy)
        self.addProductBtn_3.setMinimumSize(QSize(130, 25))
        self.addProductBtn_3.setMaximumSize(QSize(130, 25))
        self.addProductBtn_3.setFont(font)
        self.addProductBtn_3.setStyleSheet(u"background-color: rgb(170, 0, 0);")

        self.verticalLayout_25.addWidget(self.addProductBtn_3)


        self.verticalLayout_23.addWidget(self.widget_10, 0, Qt.AlignRight)


        self.verticalLayout_22.addWidget(self.widget_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.widget_7 = QWidget(self.widget)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy3.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy3)
        self.widget_7.setMinimumSize(QSize(130, 25))
        self.widget_7.setMaximumSize(QSize(130, 16777215))
        self.verticalLayout_24 = QVBoxLayout(self.widget_7)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_22.addWidget(self.widget_7, 0, Qt.AlignRight)


        self.verticalLayout_21.addWidget(self.widget)

        self.stackedWidget.addWidget(self.addProductPage)
        self.graphPage = QWidget()
        self.graphPage.setObjectName(u"graphPage")
        self.verticalLayout_8 = QVBoxLayout(self.graphPage)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.graphFrame = QFrame(self.graphPage)
        self.graphFrame.setObjectName(u"graphFrame")
        self.graphFrame.setFrameShape(QFrame.StyledPanel)
        self.graphFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.graphFrame)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 9, 0, 0)
        self.graphNavBar = QWidget(self.graphFrame)
        self.graphNavBar.setObjectName(u"graphNavBar")
        self.horizontalLayout_3 = QHBoxLayout(self.graphNavBar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.createPieGraphBtn = QPushButton(self.graphNavBar)
        self.createPieGraphBtn.setObjectName(u"createPieGraphBtn")
        self.createPieGraphBtn.setMinimumSize(QSize(0, 25))
        self.createPieGraphBtn.setMaximumSize(QSize(120, 40))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.createPieGraphBtn.setFont(font3)
        self.createPieGraphBtn.setStyleSheet(u"background-color: rgb(170, 0, 0);")

        self.horizontalLayout_3.addWidget(self.createPieGraphBtn)

        self.createGraphBtn = QPushButton(self.graphNavBar)
        self.createGraphBtn.setObjectName(u"createGraphBtn")
        self.createGraphBtn.setMinimumSize(QSize(0, 25))
        self.createGraphBtn.setMaximumSize(QSize(120, 16777215))
        self.createGraphBtn.setFont(font3)
        self.createGraphBtn.setStyleSheet(u"background-color: rgb(170, 0, 0);")

        self.horizontalLayout_3.addWidget(self.createGraphBtn)

        self.pushButton_7 = QPushButton(self.graphNavBar)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 25))
        self.pushButton_7.setMaximumSize(QSize(120, 16777215))
        self.pushButton_7.setFont(font3)
        self.pushButton_7.setStyleSheet(u"background-color: rgb(170, 0, 0);")

        self.horizontalLayout_3.addWidget(self.pushButton_7)


        self.verticalLayout_19.addWidget(self.graphNavBar, 0, Qt.AlignTop)

        self.graphPlotWin = QWidget(self.graphFrame)
        self.graphPlotWin.setObjectName(u"graphPlotWin")
        sizePolicy5.setHeightForWidth(self.graphPlotWin.sizePolicy().hasHeightForWidth())
        self.graphPlotWin.setSizePolicy(sizePolicy5)
        self.verticalLayout_20 = QVBoxLayout(self.graphPlotWin)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.graphFrame_2 = QFrame(self.graphPlotWin)
        self.graphFrame_2.setObjectName(u"graphFrame_2")
        self.graphFrame_2.setFrameShape(QFrame.StyledPanel)
        self.graphFrame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_20.addWidget(self.graphFrame_2)


        self.verticalLayout_19.addWidget(self.graphPlotWin)


        self.verticalLayout_8.addWidget(self.graphFrame)

        self.stackedWidget.addWidget(self.graphPage)
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.stackedWidget.addWidget(self.homePage)
        self.searchPage = QWidget()
        self.searchPage.setObjectName(u"searchPage")
        self.verticalLayout_10 = QVBoxLayout(self.searchPage)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.searchFrame = QFrame(self.searchPage)
        self.searchFrame.setObjectName(u"searchFrame")
        self.searchFrame.setStyleSheet(u"#frame_11{\n"
"	background-color: transparent;\n"
"}\n"
"#searchBar{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.searchFrame.setFrameShape(QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.searchFrame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.searchFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy4.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy4)
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.searchBar = QTextEdit(self.frame_11)
        self.searchBar.setObjectName(u"searchBar")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.searchBar.sizePolicy().hasHeightForWidth())
        self.searchBar.setSizePolicy(sizePolicy8)

        self.horizontalLayout_2.addWidget(self.searchBar, 0, Qt.AlignTop)

        self.pushButton = QPushButton(self.frame_11)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.pushButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_17.addWidget(self.frame_11, 0, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.searchFrame, 0, Qt.AlignTop)

        self.widget_25 = QWidget(self.searchPage)
        self.widget_25.setObjectName(u"widget_25")
        sizePolicy5.setHeightForWidth(self.widget_25.sizePolicy().hasHeightForWidth())
        self.widget_25.setSizePolicy(sizePolicy5)
        self.verticalLayout_18 = QVBoxLayout(self.widget_25)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.tableView_4 = QTableView(self.widget_25)
        self.tableView_4.setObjectName(u"tableView_4")
        self.tableView_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_18.addWidget(self.tableView_4)


        self.verticalLayout_10.addWidget(self.widget_25)

        self.stackedWidget.addWidget(self.searchPage)
        self.deleteProductPage = QWidget()
        self.deleteProductPage.setObjectName(u"deleteProductPage")
        self.horizontalLayout_19 = QHBoxLayout(self.deleteProductPage)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.deleteProductPage)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_29 = QVBoxLayout(self.widget_12)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.searchFrame_2 = QFrame(self.widget_12)
        self.searchFrame_2.setObjectName(u"searchFrame_2")
        self.searchFrame_2.setStyleSheet(u"#frame_10{\n"
"	background-color: transparent;\n"
"}\n"
"#searchBar_2{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.searchFrame_2.setFrameShape(QFrame.StyledPanel)
        self.searchFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.searchFrame_2)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.searchFrame_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy4.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy4)
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.searchBar_2 = QTextEdit(self.frame_12)
        self.searchBar_2.setObjectName(u"searchBar_2")
        sizePolicy8.setHeightForWidth(self.searchBar_2.sizePolicy().hasHeightForWidth())
        self.searchBar_2.setSizePolicy(sizePolicy8)

        self.horizontalLayout_20.addWidget(self.searchBar_2, 0, Qt.AlignTop)

        self.pushButton_3 = QPushButton(self.frame_12)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setIcon(icon7)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.pushButton_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_22.addWidget(self.frame_12)

        self.deleteRowBtn = QPushButton(self.frame_10)
        self.deleteRowBtn.setObjectName(u"deleteRowBtn")
        sizePolicy1.setHeightForWidth(self.deleteRowBtn.sizePolicy().hasHeightForWidth())
        self.deleteRowBtn.setSizePolicy(sizePolicy1)
        self.deleteRowBtn.setMinimumSize(QSize(120, 25))
        self.deleteRowBtn.setMaximumSize(QSize(120, 16777215))
        self.deleteRowBtn.setFont(font3)
        self.deleteRowBtn.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(170, 0, 0);}")
        self.deleteRowBtn.setCheckable(True)

        self.horizontalLayout_22.addWidget(self.deleteRowBtn)


        self.horizontalLayout_21.addWidget(self.frame_10, 0, Qt.AlignHCenter)


        self.verticalLayout_29.addWidget(self.searchFrame_2, 0, Qt.AlignTop)

        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy5.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy5)
        self.verticalLayout_26 = QVBoxLayout(self.widget_13)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.tableView_2 = QTableView(self.widget_13)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_26.addWidget(self.tableView_2)


        self.verticalLayout_29.addWidget(self.widget_13)


        self.horizontalLayout_19.addWidget(self.widget_12)

        self.stackedWidget.addWidget(self.deleteProductPage)
        self.transactionPage = QWidget()
        self.transactionPage.setObjectName(u"transactionPage")
        self.verticalLayout_27 = QVBoxLayout(self.transactionPage)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.transactionPage)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_37 = QVBoxLayout(self.widget_14)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.widget_26 = QWidget(self.widget_14)
        self.widget_26.setObjectName(u"widget_26")
        sizePolicy5.setHeightForWidth(self.widget_26.sizePolicy().hasHeightForWidth())
        self.widget_26.setSizePolicy(sizePolicy5)
        self.horizontalLayout_31 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.widget_27 = QWidget(self.widget_26)
        self.widget_27.setObjectName(u"widget_27")
        self.verticalLayout_34 = QVBoxLayout(self.widget_27)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.tableView_5 = QTableView(self.widget_27)
        self.tableView_5.setObjectName(u"tableView_5")
        self.tableView_5.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_34.addWidget(self.tableView_5, 0, Qt.AlignVCenter)


        self.horizontalLayout_31.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.widget_26)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMinimumSize(QSize(411, 470))
        self.horizontalLayout_37 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.widget_29 = QWidget(self.widget_28)
        self.widget_29.setObjectName(u"widget_29")
        sizePolicy6.setHeightForWidth(self.widget_29.sizePolicy().hasHeightForWidth())
        self.widget_29.setSizePolicy(sizePolicy6)
        self.widget_29.setMinimumSize(QSize(372, 283))
        self.widget_29.setStyleSheet(u"QWidget{\n"
"border-radius: 5px;\n"
"}\n"
"#inputProductName_3, #inputProductPrice_3, #inputProductQuantity_3, #inputProductCompany_3{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	border-bottom: 2px solid rgba(85, 170, 255);\n"
"	border-radius: 10px;\n"
"	padding-bottom: 7px;\n"
"    padding-left: 20px;\n"
"	padding-right: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 3px solid rgb(85, 170, 255);\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.verticalLayout_35 = QVBoxLayout(self.widget_29)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.widget_30 = QWidget(self.widget_29)
        self.widget_30.setObjectName(u"widget_30")
        sizePolicy3.setHeightForWidth(self.widget_30.sizePolicy().hasHeightForWidth())
        self.widget_30.setSizePolicy(sizePolicy3)
        self.horizontalLayout_32 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_32.setSpacing(10)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.widget_30)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setMinimumSize(QSize(130, 25))
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"QLabel{\n"
"background-color: rgb(1, 163, 164);\n"
"text-align: center;\n"
"}#")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_14)

        self.inputProductName_3 = QLineEdit(self.widget_30)
        self.inputProductName_3.setObjectName(u"inputProductName_3")
        sizePolicy1.setHeightForWidth(self.inputProductName_3.sizePolicy().hasHeightForWidth())
        self.inputProductName_3.setSizePolicy(sizePolicy1)
        self.inputProductName_3.setMinimumSize(QSize(232, 30))
        self.inputProductName_3.setMaximumSize(QSize(250, 30))
        self.inputProductName_3.setFont(font2)
        self.inputProductName_3.setStyleSheet(u"")

        self.horizontalLayout_32.addWidget(self.inputProductName_3)


        self.verticalLayout_35.addWidget(self.widget_30)

        self.widget_31 = QWidget(self.widget_29)
        self.widget_31.setObjectName(u"widget_31")
        sizePolicy3.setHeightForWidth(self.widget_31.sizePolicy().hasHeightForWidth())
        self.widget_31.setSizePolicy(sizePolicy3)
        self.horizontalLayout_33 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_33.setSpacing(10)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_35.addWidget(self.widget_31)

        self.widget_32 = QWidget(self.widget_29)
        self.widget_32.setObjectName(u"widget_32")
        sizePolicy3.setHeightForWidth(self.widget_32.sizePolicy().hasHeightForWidth())
        self.widget_32.setSizePolicy(sizePolicy3)
        self.horizontalLayout_34 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_34.setSpacing(10)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 12, 0, 0)
        self.label_16 = QLabel(self.widget_32)
        self.label_16.setObjectName(u"label_16")
        sizePolicy7.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy7)
        self.label_16.setMinimumSize(QSize(130, 25))
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"background-color: rgb(1, 163, 164);")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_16)

        self.inputProductQuantity_3 = QLineEdit(self.widget_32)
        self.inputProductQuantity_3.setObjectName(u"inputProductQuantity_3")
        sizePolicy1.setHeightForWidth(self.inputProductQuantity_3.sizePolicy().hasHeightForWidth())
        self.inputProductQuantity_3.setSizePolicy(sizePolicy1)
        self.inputProductQuantity_3.setMinimumSize(QSize(232, 30))
        self.inputProductQuantity_3.setMaximumSize(QSize(250, 30))
        self.inputProductQuantity_3.setFont(font1)
        self.inputProductQuantity_3.setStyleSheet(u"")

        self.horizontalLayout_34.addWidget(self.inputProductQuantity_3)


        self.verticalLayout_35.addWidget(self.widget_32)

        self.widget_33 = QWidget(self.widget_29)
        self.widget_33.setObjectName(u"widget_33")
        sizePolicy3.setHeightForWidth(self.widget_33.sizePolicy().hasHeightForWidth())
        self.widget_33.setSizePolicy(sizePolicy3)
        self.horizontalLayout_35 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_35.setSpacing(10)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 17, 0, 0)
        self.label_17 = QLabel(self.widget_33)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)
        self.label_17.setMinimumSize(QSize(130, 25))
        self.label_17.setFont(font1)
        self.label_17.setStyleSheet(u"background-color: rgb(1, 163, 164);")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_17)

        self.inputProductCompany_3 = QLineEdit(self.widget_33)
        self.inputProductCompany_3.setObjectName(u"inputProductCompany_3")
        sizePolicy1.setHeightForWidth(self.inputProductCompany_3.sizePolicy().hasHeightForWidth())
        self.inputProductCompany_3.setSizePolicy(sizePolicy1)
        self.inputProductCompany_3.setMinimumSize(QSize(232, 30))
        self.inputProductCompany_3.setMaximumSize(QSize(250, 30))
        self.inputProductCompany_3.setFont(font1)
        self.inputProductCompany_3.setStyleSheet(u"")

        self.horizontalLayout_35.addWidget(self.inputProductCompany_3)


        self.verticalLayout_35.addWidget(self.widget_33)

        self.widget_34 = QWidget(self.widget_29)
        self.widget_34.setObjectName(u"widget_34")
        self.widget_34.setMinimumSize(QSize(70, 0))
        self.horizontalLayout_36 = QHBoxLayout(self.widget_34)
        self.horizontalLayout_36.setSpacing(30)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.updateProductBtn_4 = QPushButton(self.widget_34)
        self.updateProductBtn_4.setObjectName(u"updateProductBtn_4")
        sizePolicy.setHeightForWidth(self.updateProductBtn_4.sizePolicy().hasHeightForWidth())
        self.updateProductBtn_4.setSizePolicy(sizePolicy)
        self.updateProductBtn_4.setMinimumSize(QSize(130, 25))
        self.updateProductBtn_4.setMaximumSize(QSize(130, 25))
        self.updateProductBtn_4.setFont(font)
        self.updateProductBtn_4.setStyleSheet(u"background-color: rgb(170, 0, 0);")

        self.horizontalLayout_36.addWidget(self.updateProductBtn_4)

        self.updateProductBtn_5 = QPushButton(self.widget_34)
        self.updateProductBtn_5.setObjectName(u"updateProductBtn_5")
        sizePolicy.setHeightForWidth(self.updateProductBtn_5.sizePolicy().hasHeightForWidth())
        self.updateProductBtn_5.setSizePolicy(sizePolicy)
        self.updateProductBtn_5.setMinimumSize(QSize(130, 25))
        self.updateProductBtn_5.setMaximumSize(QSize(130, 25))
        self.updateProductBtn_5.setFont(font)
        self.updateProductBtn_5.setStyleSheet(u"background-color: rgb(170, 0, 0);")

        self.horizontalLayout_36.addWidget(self.updateProductBtn_5)


        self.verticalLayout_35.addWidget(self.widget_34, 0, Qt.AlignVCenter)


        self.horizontalLayout_37.addWidget(self.widget_29, 0, Qt.AlignVCenter)


        self.horizontalLayout_31.addWidget(self.widget_28, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_37.addWidget(self.widget_26)


        self.verticalLayout_27.addWidget(self.widget_14)

        self.stackedWidget.addWidget(self.transactionPage)
        self.viewProductsPage = QWidget()
        self.viewProductsPage.setObjectName(u"viewProductsPage")
        self.horizontalLayout_17 = QHBoxLayout(self.viewProductsPage)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.viewProductsPage)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.tableView = QTableView(self.widget_11)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_18.addWidget(self.tableView)


        self.horizontalLayout_17.addWidget(self.widget_11)

        self.stackedWidget.addWidget(self.viewProductsPage)
        self.updateProductPage = QWidget()
        self.updateProductPage.setObjectName(u"updateProductPage")
        self.verticalLayout_28 = QVBoxLayout(self.updateProductPage)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.widget_15 = QWidget(self.updateProductPage)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_30 = QVBoxLayout(self.widget_15)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.searchFrame_3 = QFrame(self.widget_15)
        self.searchFrame_3.setObjectName(u"searchFrame_3")
        self.searchFrame_3.setStyleSheet(u"#frame_14{\n"
"	background-color: transparent;\n"
"}\n"
"#searchBar_3{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.searchFrame_3.setFrameShape(QFrame.StyledPanel)
        self.searchFrame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.searchFrame_3)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.searchFrame_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy4.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy4)
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.searchBar_3 = QTextEdit(self.frame_14)
        self.searchBar_3.setObjectName(u"searchBar_3")
        sizePolicy8.setHeightForWidth(self.searchBar_3.sizePolicy().hasHeightForWidth())
        self.searchBar_3.setSizePolicy(sizePolicy8)

        self.horizontalLayout_25.addWidget(self.searchBar_3, 0, Qt.AlignTop)

        self.pushButton_4 = QPushButton(self.frame_14)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setIcon(icon7)
        self.pushButton_4.setIconSize(QSize(24, 24))

        self.horizontalLayout_25.addWidget(self.pushButton_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_24.addWidget(self.frame_14)

        self.deleteRowBtn_2 = QPushButton(self.frame_13)
        self.deleteRowBtn_2.setObjectName(u"deleteRowBtn_2")
        sizePolicy1.setHeightForWidth(self.deleteRowBtn_2.sizePolicy().hasHeightForWidth())
        self.deleteRowBtn_2.setSizePolicy(sizePolicy1)
        self.deleteRowBtn_2.setMinimumSize(QSize(120, 25))
        self.deleteRowBtn_2.setMaximumSize(QSize(120, 16777215))
        self.deleteRowBtn_2.setFont(font3)
        self.deleteRowBtn_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(170, 0, 0);}")
        self.deleteRowBtn_2.setCheckable(True)

        self.horizontalLayout_24.addWidget(self.deleteRowBtn_2)


        self.horizontalLayout_23.addWidget(self.frame_13, 0, Qt.AlignHCenter)


        self.verticalLayout_30.addWidget(self.searchFrame_3)

        self.widget_16 = QWidget(self.widget_15)
        self.widget_16.setObjectName(u"widget_16")
        sizePolicy5.setHeightForWidth(self.widget_16.sizePolicy().hasHeightForWidth())
        self.widget_16.setSizePolicy(sizePolicy5)
        self.horizontalLayout_26 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.widget_18 = QWidget(self.widget_16)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_33 = QVBoxLayout(self.widget_18)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.tableView_3 = QTableView(self.widget_18)
        self.tableView_3.setObjectName(u"tableView_3")
        self.tableView_3.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_33.addWidget(self.tableView_3, 0, Qt.AlignVCenter)


        self.horizontalLayout_26.addWidget(self.widget_18)

        self.widget_17 = QWidget(self.widget_16)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(411, 470))
        self.widget_19 = QWidget(self.widget_17)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setGeometry(QRect(30, 90, 372, 283))
        sizePolicy6.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy6)
        self.widget_19.setMinimumSize(QSize(372, 283))
        self.widget_19.setStyleSheet(u"QWidget{\n"
"border-radius: 5px;\n"
"}\n"
"#inputProductName_2, #inputProductPrice_2, #inputProductQuantity_2, #inputProductCompany_2{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	border-bottom: 2px solid rgba(85, 170, 255);\n"
"	border-radius: 10px;\n"
"	padding-bottom: 7px;\n"
"    padding-left: 20px;\n"
"	padding-right: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 3px solid rgb(85, 170, 255);\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.verticalLayout_31 = QVBoxLayout(self.widget_19)
        self.verticalLayout_31.setSpacing(30)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.widget_20 = QWidget(self.widget_19)
        self.widget_20.setObjectName(u"widget_20")
        sizePolicy3.setHeightForWidth(self.widget_20.sizePolicy().hasHeightForWidth())
        self.widget_20.setSizePolicy(sizePolicy3)
        self.horizontalLayout_27 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_27.setSpacing(10)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_20)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setMinimumSize(QSize(130, 25))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"QLabel{\n"
"background-color: rgb(1, 163, 164);\n"
"text-align: center;\n"
"}#")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_9)

        self.inputProductName_2 = QLineEdit(self.widget_20)
        self.inputProductName_2.setObjectName(u"inputProductName_2")
        sizePolicy1.setHeightForWidth(self.inputProductName_2.sizePolicy().hasHeightForWidth())
        self.inputProductName_2.setSizePolicy(sizePolicy1)
        self.inputProductName_2.setMinimumSize(QSize(232, 30))
        self.inputProductName_2.setMaximumSize(QSize(250, 30))
        self.inputProductName_2.setFont(font2)
        self.inputProductName_2.setStyleSheet(u"")

        self.horizontalLayout_27.addWidget(self.inputProductName_2)


        self.verticalLayout_31.addWidget(self.widget_20)

        self.widget_21 = QWidget(self.widget_19)
        self.widget_21.setObjectName(u"widget_21")
        sizePolicy3.setHeightForWidth(self.widget_21.sizePolicy().hasHeightForWidth())
        self.widget_21.setSizePolicy(sizePolicy3)
        self.horizontalLayout_28 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_28.setSpacing(10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_21)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setMinimumSize(QSize(130, 25))
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"background-color: rgb(1, 163, 164);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_10)

        self.inputProductPrice_2 = QLineEdit(self.widget_21)
        self.inputProductPrice_2.setObjectName(u"inputProductPrice_2")
        sizePolicy1.setHeightForWidth(self.inputProductPrice_2.sizePolicy().hasHeightForWidth())
        self.inputProductPrice_2.setSizePolicy(sizePolicy1)
        self.inputProductPrice_2.setMinimumSize(QSize(232, 30))
        self.inputProductPrice_2.setMaximumSize(QSize(250, 30))
        self.inputProductPrice_2.setFont(font1)
        self.inputProductPrice_2.setStyleSheet(u"")

        self.horizontalLayout_28.addWidget(self.inputProductPrice_2)


        self.verticalLayout_31.addWidget(self.widget_21)

        self.widget_22 = QWidget(self.widget_19)
        self.widget_22.setObjectName(u"widget_22")
        sizePolicy3.setHeightForWidth(self.widget_22.sizePolicy().hasHeightForWidth())
        self.widget_22.setSizePolicy(sizePolicy3)
        self.horizontalLayout_29 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_29.setSpacing(10)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.widget_22)
        self.label_12.setObjectName(u"label_12")
        sizePolicy7.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy7)
        self.label_12.setMinimumSize(QSize(130, 25))
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"background-color: rgb(1, 163, 164);")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_12)

        self.inputProductQuantity_2 = QLineEdit(self.widget_22)
        self.inputProductQuantity_2.setObjectName(u"inputProductQuantity_2")
        sizePolicy1.setHeightForWidth(self.inputProductQuantity_2.sizePolicy().hasHeightForWidth())
        self.inputProductQuantity_2.setSizePolicy(sizePolicy1)
        self.inputProductQuantity_2.setMinimumSize(QSize(232, 30))
        self.inputProductQuantity_2.setMaximumSize(QSize(250, 30))
        self.inputProductQuantity_2.setFont(font1)
        self.inputProductQuantity_2.setStyleSheet(u"")

        self.horizontalLayout_29.addWidget(self.inputProductQuantity_2)


        self.verticalLayout_31.addWidget(self.widget_22)

        self.widget_23 = QWidget(self.widget_19)
        self.widget_23.setObjectName(u"widget_23")
        sizePolicy3.setHeightForWidth(self.widget_23.sizePolicy().hasHeightForWidth())
        self.widget_23.setSizePolicy(sizePolicy3)
        self.horizontalLayout_30 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_30.setSpacing(10)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.widget_23)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setMinimumSize(QSize(130, 25))
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"background-color: rgb(1, 163, 164);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_13)

        self.inputProductCompany_2 = QLineEdit(self.widget_23)
        self.inputProductCompany_2.setObjectName(u"inputProductCompany_2")
        sizePolicy1.setHeightForWidth(self.inputProductCompany_2.sizePolicy().hasHeightForWidth())
        self.inputProductCompany_2.setSizePolicy(sizePolicy1)
        self.inputProductCompany_2.setMinimumSize(QSize(232, 30))
        self.inputProductCompany_2.setMaximumSize(QSize(250, 30))
        self.inputProductCompany_2.setFont(font1)
        self.inputProductCompany_2.setStyleSheet(u"")

        self.horizontalLayout_30.addWidget(self.inputProductCompany_2)


        self.verticalLayout_31.addWidget(self.widget_23)

        self.widget_24 = QWidget(self.widget_19)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setMinimumSize(QSize(50, 0))
        self.verticalLayout_32 = QVBoxLayout(self.widget_24)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.updateProductBtn_3 = QPushButton(self.widget_24)
        self.updateProductBtn_3.setObjectName(u"updateProductBtn_3")
        sizePolicy.setHeightForWidth(self.updateProductBtn_3.sizePolicy().hasHeightForWidth())
        self.updateProductBtn_3.setSizePolicy(sizePolicy)
        self.updateProductBtn_3.setMinimumSize(QSize(130, 25))
        self.updateProductBtn_3.setMaximumSize(QSize(130, 25))
        self.updateProductBtn_3.setFont(font)
        self.updateProductBtn_3.setStyleSheet(u"background-color: rgb(170, 0, 0);")

        self.verticalLayout_32.addWidget(self.updateProductBtn_3)


        self.verticalLayout_31.addWidget(self.widget_24, 0, Qt.AlignRight)


        self.horizontalLayout_26.addWidget(self.widget_17, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_30.addWidget(self.widget_16)


        self.verticalLayout_28.addWidget(self.widget_15)

        self.stackedWidget.addWidget(self.updateProductPage)

        self.verticalLayout_11.addWidget(self.stackedWidget)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")

        self.horizontalLayout_8.addWidget(self.mainContentsContainer)

        self.rightMenuContainer = QWidget(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(200, 0))
        self.rightMenuContainer.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background-color:transparent;\n"
"	background:transparent;\n"
"	padding:0;\n"
"	margin:0;\n"
"	color:#fff;\n"
"}\n"
"QWidget{background-color: rgb(44, 49, 60)}\n"
"")
        self.verticalLayout_12 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.rightMenuSubContainer.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.frame_9 = QFrame(self.rightMenuSubContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"#frame_9{\n"
"	background-color: rgb(126, 126, 126);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"\n"
"background-color: rgb(126, 126, 126);\n"
"color: rgb(0, 0, 0);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_6)

        self.pushButton_2 = QPushButton(self.frame_9)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"\n"
"background-color: rgb(126, 126, 126);\n"
"")
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon17)
        self.pushButton_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.verticalLayout_13.addWidget(self.frame_9, 0, Qt.AlignBottom)

        self.stackedWidget_2 = QStackedWidget(self.rightMenuSubContainer)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_14 = QVBoxLayout(self.page)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        font4 = QFont()
        font4.setPointSize(13)
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_7)

        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_15 = QVBoxLayout(self.page_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"background-color: rgb(123, 176, 255);")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_8)

        self.stackedWidget_2.addWidget(self.page_2)

        self.verticalLayout_13.addWidget(self.stackedWidget_2)


        self.verticalLayout_12.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_8.addWidget(self.rightMenuContainer)


        self.verticalLayout_11.addWidget(self.mainBodyContent, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.addProductBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.addProductBtn.setText("")
#if QT_CONFIG(tooltip)
        self.deleteProductBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.deleteProductBtn.setText("")
#if QT_CONFIG(tooltip)
        self.updateProductBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.updateProductBtn.setText("")
#if QT_CONFIG(tooltip)
        self.viewProductsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.viewProductsBtn.setText("")
#if QT_CONFIG(tooltip)
        self.dataBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
#endif // QT_CONFIG(tooltip)
        self.dataBtn.setText("")
#if QT_CONFIG(tooltip)
        self.graphBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.graphBtn.setText("")
#if QT_CONFIG(tooltip)
        self.searchBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Reports", None))
#endif // QT_CONFIG(tooltip)
        self.searchBtn.setText("")
#if QT_CONFIG(tooltip)
        self.settingBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingBtn.setText("")
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Information about the App", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText("")
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Get more help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.addProductBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.addProductBtn_2.setText(QCoreApplication.translate("MainWindow", u"Add Product", None))
#if QT_CONFIG(tooltip)
        self.deleteProductBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.deleteProductBtn_2.setText(QCoreApplication.translate("MainWindow", u"Delete Product", None))
#if QT_CONFIG(tooltip)
        self.updateProductBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.updateProductBtn_2.setText(QCoreApplication.translate("MainWindow", u"Update Product", None))
#if QT_CONFIG(tooltip)
        self.viewProductsBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.viewProductsBtn_2.setText(QCoreApplication.translate("MainWindow", u"View Products", None))
#if QT_CONFIG(tooltip)
        self.dataBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
#endif // QT_CONFIG(tooltip)
        self.dataBtn_2.setText(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
#if QT_CONFIG(tooltip)
        self.graphBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.graphBtn_2.setText(QCoreApplication.translate("MainWindow", u"Transaction", None))
#if QT_CONFIG(tooltip)
        self.searchBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Reports", None))
#endif // QT_CONFIG(tooltip)
        self.searchBtn_2.setText(QCoreApplication.translate("MainWindow", u"Search", None))
#if QT_CONFIG(tooltip)
        self.settingBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Go to Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingBtn_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.infoBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Information about the App", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn_2.setText(QCoreApplication.translate("MainWindow", u"Info", None))
#if QT_CONFIG(tooltip)
        self.helpBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Get more help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn_2.setText(QCoreApplication.translate("MainWindow", u"Help", None))
#if QT_CONFIG(tooltip)
        self.menuButton.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuButton.setText("")
        self.pushButton_6.setText("")
        self.pushButton_5.setText("")
        self.minimizeBtn.setText("")
        self.restoreBtn.setText("")
        self.closeBtn.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.displayDate.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.displayTime.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
#if QT_CONFIG(whatsthis)
        self.inputProductName.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>adsasa</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.inputProductName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Product Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Product Price", None))
        self.inputProductPrice.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Product Price", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Product Quantity", None))
        self.inputProductQuantity.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Product Quantity", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Product Company", None))
        self.inputProductCompany.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Product Company", None))
        self.addProductBtn_3.setText(QCoreApplication.translate("MainWindow", u"Add Product", None))
        self.createPieGraphBtn.setText(QCoreApplication.translate("MainWindow", u"Create Pie Chart", None))
        self.createGraphBtn.setText(QCoreApplication.translate("MainWindow", u"Create Graph", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton.setText("")
        self.searchBar_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton_3.setText("")
        self.deleteRowBtn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
#if QT_CONFIG(whatsthis)
        self.inputProductName_3.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>adsasa</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.inputProductName_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Product Name", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Product Quantity", None))
        self.inputProductQuantity_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Product Quantity", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Product Company", None))
        self.inputProductCompany_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Product Company", None))
        self.updateProductBtn_4.setText(QCoreApplication.translate("MainWindow", u"Add to Cart", None))
        self.updateProductBtn_5.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.searchBar_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton_4.setText("")
        self.deleteRowBtn_2.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
#if QT_CONFIG(whatsthis)
        self.inputProductName_2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>adsasa</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.inputProductName_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Product Name", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Product Price", None))
        self.inputProductPrice_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Product Price", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Product Quantity", None))
        self.inputProductQuantity_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Product Quantity", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Product Company", None))
        self.inputProductCompany_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Product Company", None))
        self.updateProductBtn_3.setText(QCoreApplication.translate("MainWindow", u"Update Product", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
        self.pushButton_2.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"More...", None))
    # retranslateUi

