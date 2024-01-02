import pandas as pd
import matplotlib.pyplot as plt
import csv
import sys
from PyQt5.QtCore import Qt,pyqtSlot, QEvent,QRect, QPropertyAnimation,QParallelAnimationGroup, QEasingCurve
from PyQt5.QtGui import QIcon,QPainter, QPen
from PyQt5.QtWidgets import QListView,QCompleter,QApplication,QLineEdit, QMainWindow,QComboBox, QPushButton, QLabel,QStackedWidget, QVBoxLayout, QWidget, QHBoxLayout, QSizePolicy, QSpacerItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.uic import loadUi
import resources
import Hashing_Password

class MainWindow_2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.showPassIcon = QIcon("://icons//icons//eye.svg")
        self.hidePassIcon = QIcon("://icons//icons//eye-off.svg")
        loadUi("Credentials.ui",self)

        self.password_2.setEchoMode(QLineEdit.Password)
        self.password_3.setEchoMode(QLineEdit.Password)

        self.hidePassword = True
        self.hidePassword2 = True
        self.showPassBtn.clicked.connect(self.show_password)
        self.showPassBtn_2.clicked.connect(self.show_password)


        self.LoginBtn2_2.clicked.connect(self.switch_to_login_page)
        self.SignUpBtn.clicked.connect(self.switch_to_signup_page)    
        
        
        self.SignUpBtn2_2.clicked.connect(self.signUp)
        self.LoginBtn.clicked.connect(self.signIn)

    def checkPasswordVisibility(self):
        if self.hidePassword or self.hidePassword2:
            self.showPassBtn.setIcon(self.hidePassIcon)
            self.showPassBtn_2.setIcon(self.hidePassIcon)
        else:
            self.showPassBtn.setIcon(self.showPassIcon)
            self.showPassBtn_2.setIcon(self.showPassIcon)


    def show_password(self):
        if self.hidePassword :
            self.password_2.setEchoMode(QLineEdit.Normal)
            self.hidePassword = False
            self.checkPasswordVisibility()
        else:
            self.password_2.setEchoMode(QLineEdit.Password)
            self.hidePassword = True
            self.checkPasswordVisibility()    

        if self.hidePassword2 :
            self.password_3.setEchoMode(QLineEdit.Normal)
            self.hidePassword2 = False
            self.checkPasswordVisibility()
        else:
            self.password_3.setEchoMode(QLineEdit.Password)
            self.hidePassword2 = True
            self.checkPasswordVisibility()     

    def clearSignUpInput(self):
        self.username_3.clear()
        self.password_3.clear()

    def clearLoginInput(self):
        self.username_2.clear()
        self.password_2.clear()    

    def switch_to_login_page(self):
        self.stackedWidget.setCurrentIndex(0)
        self.clearSignUpInput()

    def switch_to_signup_page(self):
        self.stackedWidget.setCurrentIndex(1) 
        self.clearLoginInput()

    def signIn(self):
        name = self.username_2.text()
        password = self.password_2.text()
        check = Hashing_Password.signIn(name, password)
        if check:
            self.mainWindow = MainWindow()  
            self.mainWindow.show()
            self.hide()


    def signUp(self):
        try:
            name = self.username_3.text()
            password = self.password_3.text()
            Hashing_Password.signUp(name, password)
        except Exception as e:
            print(e)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("MainWindow.ui",self)  # Load your UI file here
        self.restoreIcon = QIcon(":/icons/icons/square.svg")
        self.maximizedIcon = QIcon("://icons//icons//copy.svg")
        # Remove default title bar and set window flags
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground) 

        self.titleBar = QWidget(self)
        
        self.restoreBtn.setIcon(self.restoreIcon)
        self.restoreBtn.clicked.connect(self.toggle_maximize)
        self.minimizeBtn.clicked.connect(self.minimize_window)
        self.closeBtn.clicked.connect(self.close_window)
        self.dataBtn.clicked.connect(self.switch_to_graph_page)
        self.dataBtn_2.clicked.connect(self.switch_to_graph_page)
        self.switch_to_home_page()
        self.homeBtn.clicked.connect(self.switch_to_home_page)
        self.homeBtn_2.clicked.connect(self.switch_to_home_page)
        self.searchBtn.clicked.connect(self.switch_to_search_page)
        self.searchBtn_2.clicked.connect(self.switch_to_search_page)

        # # Some initial items in the QComboBox
        # # Some initial items in the QComboBox
        # search_results = ["Apple", "Banana", "Orange", "Pineapple", "Grapes", "Watermelon", "Peach", "Pear"]
        # self.searchResult.addItems(search_results)
        # #self.searchResult.setEditable(False)
        # # Store the textChanged signal of QLineEdit in a variable
        # text_changed_signal = self.searchBar.textChanged

        # # Connect the stored signal to the handle_text_changed slot
        # text_changed_signal.connect(self.handle_text_changed)
        # # Create a completer and set it to the QComboBox
        # completer = QCompleter(search_results)
        # completer.setCaseSensitivity(0)  # Case insensitive matching
        # self.searchResult.setCompleter(completer)
        # Create a completer and set it to the QListView within QComboBox
        completer = QCompleter()
        completer.setPopup(QListView())  # Set QListView for showing suggestions
        self.searchResult.setCompleter(completer)

        # Some initial items in the QComboBox
        search_results = ["Apple", "Banana", "Orange", "Pineapple", "Grapes", "Watermelon", "Peach", "Pear"]
        completer.setModel(completer.model())  # Set QCompleter model with search results
        # Connect the textChanged signal of QTextEdit to handle_text_changed method
        self.searchBar.textChanged.connect(self.handle_text_changed)

        self.centerMenuContainer.hide()
        self.mainBodyContent.hide()

        self.menuButton.clicked.connect(self.toggle_visibility)
        
        self.graph_widget = GraphWidget([])  # Empty data initially

        # Check if layout is already set for graphFrame
        if self.graphFrame_2.layout() is None:
            graph_frame_layout = QVBoxLayout()
            self.graphFrame_2.setLayout(graph_frame_layout)
        self.graphFrame_2.layout().addWidget(self.graph_widget)

        self.createGraphBtn.raise_()
        self.createGraphBtn.clicked.connect(self.create_graph)
        self.createPieGraphBtn.clicked.connect(self.create_pie_chart)

    # Create a QComboBox for displaying suggestions
        self.searchResult.setPlaceholderText("Suggestions")
        self.searchResult.setMaxVisibleItems(5)

    def handle_text_changed(self):
        # # Clear the previous suggestions
        # self.searchResult.clear()
        # text = self.searchBar.toPlainText().lower()

        # search_results = ["Apple", "Banana", "Orange", "Pineapple", "Grapes", "Watermelon", "Peach", "Pear"]

        # if text:
        #     matching_results = [result for result in search_results if text.lower() in result.lower()]
        #     self.searchResult.addItems(matching_results)# Filter items in QComboBox based on entered text
        # matching_results = [result for result in search_results if text in result.lower()]
        # self.searchResult.addItems(matching_results)
        # text = self.searchBar.toPlainText().lower()
        # if text:
        #     self.searchResult.showPopup()  # Show the popup
        # else:
        #     self.searchResult.hidePopup()  # Hide the popup
        text = self.searchBar.toPlainText().lower()
        self.searchResult.lineEdit().setText(text)  # Set text in QComboBox to update QCompleter suggestions

    def switch_to_graph_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_home_page(self):
        self.stackedWidget.setCurrentIndex(1)    

    def switch_to_search_page(self):
        self.stackedWidget.setCurrentIndex(2)    

    def create_graph(self):
        data = [10, 20, 30, 40, 50]  # Sample data for the graph - replace with your data
        self.graph_widget.draw_graph(data, 'line')

    def create_pie_chart(self):
        data = [10, 20, 30, 40, 50]  # Sample data for the pie chart - replace with your data
        self.graph_widget.draw_graph(data, 'pie')

    def toggle_visibility(self):
        # Toggle visibility of the QWidget
        if self.leftMenuContainer.isVisible():
            self.leftMenuContainer.hide()
            self.centerMenuContainer.show()
        else:
            self.leftMenuContainer.show()
            self.centerMenuContainer.hide()

    def event(self, event):
        if event.type() == QEvent.WindowStateChange:
            if self.isMaximized():
                self.restoreBtn.setIcon(self.maximizedIcon)
            else:
                self.restoreBtn.setIcon(self.restoreIcon)
        return super().event(event)

    def toggle_maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def minimize_window(self):
        self.showMinimized()

    def close_window(self):
        self.close()

class GraphWidget(QWidget):
    def __init__(self, data):
        super().__init__()

        self.data = data
        self.figure, self.ax = plt.subplots(figsize=(2, 2))
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        #self.raise_()  # Bring the GraphWidget to the front

    def draw_graph(self, data, graph_type):
        self.ax.clear()
        if graph_type == 'line':
            self.ax.plot(data, marker='o', linestyle='-')
            self.ax.set_title('Graph of Data')
            self.ax.set_xlabel('X-axis Label')
            self.ax.set_ylabel('Y-axis Label')
        elif graph_type == 'pie':
            self.ax.pie(data, labels=[f'Data {i}' for i in range(len(data))],
                        autopct='%1.1f%%', startangle=140)
            self.ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow_2()
    window.show()
    sys.exit(app.exec_())


