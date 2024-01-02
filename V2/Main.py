import pandas as pd
import matplotlib.pyplot as plt
import csv
import sys
from PyQt5.QtCore import Qt, QEvent,QRect, QPropertyAnimation,QParallelAnimationGroup, QEasingCurve, pyqtSlot
from PyQt5.QtGui import QIcon,QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow,QComboBox, QPushButton, QLabel,QStackedWidget, QVBoxLayout, QWidget, QHBoxLayout, QSizePolicy, QSpacerItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.uic import loadUi
import resources
import Hashing_Password

class MainWindow_2(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Credentials.ui",self)
        self.LoginBtn2.clicked.connect(self.switch_to_login_page)
        self.SignUpBtn.clicked.connect(self.switch_to_signup_page)    
        
        
        self.SignUpBtn2.clicked.connect(self.signUp)
        self.LogInBtn.clicked.connect(self.signIn)

    def switch_to_login_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_signup_page(self):
        self.stackedWidget.setCurrentIndex(1) 

    def signIn(self):
        name = self.username.toPlainText()
        password = self.password.toPlainText()
        check = Hashing_Password.signIn(name, password)
        if check:
            self.mainWindow = MainWindow()  
            self.mainWindow.show()
            self.hide()


    def signUp(self):
        try:
            name = self.username_3.toPlainText()
            password = self.password_3.toPlainText()
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

        self.searchBar.textChanged.connect(self.handle_text_changed)

        self.centerMenuContainer.hide()
        self.mainBodyContent.hide()

        self.menuButton.clicked.connect(self.toggle_visibility)
        
        self.graph_widget = GraphWidget([])  # Empty data initially

        # Check if layout is already set for graphFrame
        if self.graphFrame.layout() is None:
            graph_frame_layout = QVBoxLayout()
            self.graphFrame.setLayout(graph_frame_layout)
        self.graphFrame.layout().addWidget(self.graph_widget)

        self.graphBtn.raise_()
        self.graphBtn.clicked.connect(self.create_graph)

    # Create a QComboBox for displaying suggestions
        self.searchResult.setPlaceholderText("Suggestions")
        self.searchResult.setMaxVisibleItems(5)

    def handle_text_changed(self, text):
        # Clear the previous suggestions
        self.searchResult.clear()

        # Perform search or filtering logic here based on 'text'
        # For example, you might have a list of suggestions to show
        # Here, we are displaying suggestions containing the entered text

        search_results = ["Apple", "Banana", "Orange", "Pineapple", "Grapes", "Watermelon", "Peach", "Pear"]

        if text:
            matching_results = [result for result in search_results if text.lower() in result.lower()]
            self.searchResult.addItems(matching_results)

    def switch_to_graph_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_home_page(self):
        self.stackedWidget.setCurrentIndex(1)    

    def switch_to_search_page(self):
        self.stackedWidget.setCurrentIndex(2)    

    def create_graph(self):
        data = [10, 20, 30, 40, 50]  # Sample data for the graph - replace with your data
        self.graph_widget.data = data
        self.graph_widget.draw_graph()
        #self.stackedWidget.setCurrentIndex(0)  # Show the graphPage

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

    def draw_graph(self):
        self.ax.clear()
        self.ax.plot(self.data, marker='o', linestyle='-')
        self.ax.set_title('Graph of Data')
        self.ax.set_xlabel('X-axis Label')
        self.ax.set_ylabel('Y-axis Label')
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow_2()
    window.show()
    sys.exit(app.exec_())


