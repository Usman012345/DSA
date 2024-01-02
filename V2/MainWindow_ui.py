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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 682)
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

        self.dataBtn = QPushButton(self.frame_2)
        self.dataBtn.setObjectName(u"dataBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dataBtn.setIcon(icon1)
        self.dataBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.dataBtn)

        self.searchBtn = QPushButton(self.frame_2)
        self.searchBtn.setObjectName(u"searchBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.searchBtn.setIcon(icon2)
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
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingBtn.setIcon(icon3)
        self.settingBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.settingBtn)

        self.infoBtn = QPushButton(self.frame_3)
        self.infoBtn.setObjectName(u"infoBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon4)
        self.infoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon5)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.homeBtn_2.sizePolicy().hasHeightForWidth())
        self.homeBtn_2.setSizePolicy(sizePolicy1)
        self.homeBtn_2.setStyleSheet(u"")
        self.homeBtn_2.setIcon(icon)
        self.homeBtn_2.setIconSize(QSize(24, 24))
        self.homeBtn_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.homeBtn_2)

        self.dataBtn_2 = QPushButton(self.frame_4)
        self.dataBtn_2.setObjectName(u"dataBtn_2")
        sizePolicy1.setHeightForWidth(self.dataBtn_2.sizePolicy().hasHeightForWidth())
        self.dataBtn_2.setSizePolicy(sizePolicy1)
        self.dataBtn_2.setIcon(icon1)
        self.dataBtn_2.setIconSize(QSize(24, 24))
        self.dataBtn_2.setFlat(False)

        self.verticalLayout_5.addWidget(self.dataBtn_2)

        self.searchBtn_2 = QPushButton(self.frame_4)
        self.searchBtn_2.setObjectName(u"searchBtn_2")
        sizePolicy1.setHeightForWidth(self.searchBtn_2.sizePolicy().hasHeightForWidth())
        self.searchBtn_2.setSizePolicy(sizePolicy1)
        self.searchBtn_2.setIcon(icon2)
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
        self.settingBtn_2.setIcon(icon3)
        self.settingBtn_2.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.settingBtn_2)

        self.infoBtn_2 = QPushButton(self.frame_5)
        self.infoBtn_2.setObjectName(u"infoBtn_2")
        sizePolicy1.setHeightForWidth(self.infoBtn_2.sizePolicy().hasHeightForWidth())
        self.infoBtn_2.setSizePolicy(sizePolicy1)
        self.infoBtn_2.setLayoutDirection(Qt.LeftToRight)
        self.infoBtn_2.setIcon(icon4)
        self.infoBtn_2.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.infoBtn_2)

        self.helpBtn_2 = QPushButton(self.frame_5)
        self.helpBtn_2.setObjectName(u"helpBtn_2")
        sizePolicy1.setHeightForWidth(self.helpBtn_2.sizePolicy().hasHeightForWidth())
        self.helpBtn_2.setSizePolicy(sizePolicy1)
        self.helpBtn_2.setIcon(icon5)
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
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon6)
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
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon7)
        self.pushButton_6.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.frame_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon8)
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
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon9)
        self.minimizeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.minimizeBtn, 0, Qt.AlignHCenter)

        self.restoreBtn = QPushButton(self.frame_8)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon10)
        self.restoreBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.restoreBtn, 0, Qt.AlignHCenter)

        self.closeBtn = QPushButton(self.frame_8)
        self.closeBtn.setObjectName(u"closeBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon11)
        self.closeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.closeBtn, 0, Qt.AlignHCenter)


        self.horizontalLayout_5.addWidget(self.frame_8, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.mainBodyContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
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
        self.graphBtn = QPushButton(self.graphFrame)
        self.graphBtn.setObjectName(u"graphBtn")
        self.graphBtn.setGeometry(QRect(20, 10, 121, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.graphBtn.setFont(font)
        self.graphBtn.setStyleSheet(u"QPushButton{\n"
"background-color:transparent;\n"
"	background:transparent;\n"
"}")

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
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy3)
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.searchBar = QTextEdit(self.frame_11)
        self.searchBar.setObjectName(u"searchBar")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.searchBar.sizePolicy().hasHeightForWidth())
        self.searchBar.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.searchBar, 0, Qt.AlignTop)

        self.pushButton = QPushButton(self.frame_11)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.pushButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_17.addWidget(self.frame_11, 0, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_10 = QFrame(self.searchFrame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.searchResult = QComboBox(self.frame_10)
        self.searchResult.setObjectName(u"searchResult")

        self.verticalLayout_18.addWidget(self.searchResult)


        self.verticalLayout_16.addWidget(self.frame_10)


        self.verticalLayout_10.addWidget(self.searchFrame, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.searchPage)

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
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon12)
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
        font1 = QFont()
        font1.setPointSize(13)
        self.label_7.setFont(font1)
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
        self.label_8.setFont(font1)
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

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.dataBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
#endif // QT_CONFIG(tooltip)
        self.dataBtn.setText("")
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
        self.dataBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
#endif // QT_CONFIG(tooltip)
        self.dataBtn_2.setText(QCoreApplication.translate("MainWindow", u"Graph", None))
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
        self.graphBtn.setText(QCoreApplication.translate("MainWindow", u"Create Graph", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
        self.pushButton_2.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"More...", None))
    # retranslateUi

