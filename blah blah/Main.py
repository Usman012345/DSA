
import pandas as pd
import matplotlib.pyplot as plt
import csv
import sys
from graph import graph
#import Graphs
from PyQt5.QtCore import Qt,QSize, QModelIndex,QAbstractTableModel, QItemSelectionModel,pyqtSlot, QEvent, QRect, QVariant, QPropertyAnimation,QAbstractTableModel,QParallelAnimationGroup, QEasingCurve
from PyQt5.QtGui import QIcon,QPainter,QStandardItemModel,QStandardItem
from PyQt5.QtWidgets import QListWidgetItem,QTableView,QListView,QCompleter,QApplication,QLineEdit,QHeaderView,QMessageBox, QMainWindow,QAction,QMenu,QComboBox, QPushButton, QLabel,QStackedWidget, QVBoxLayout, QWidget, QHBoxLayout, QSizePolicy, QSpacerItem, QAbstractItemView
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.uic import loadUi
from matplotlib.figure import Figure
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import resources
import Hashing_Password
import validations
import crud_product
import transaction___sales
from PyQt5.QtWidgets import QStyledItemDelegate
from PyQt5.QtGui import QColor

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
        try:

            name = self.username_2.text()
            password = self.password_2.text()
            check = Hashing_Password.signIn(name, password)
            if check:
                self.mainWindow = MainWindow()  
                self.mainWindow.show()
                self.hide()
            else:
                QMessageBox.information(self, "Login Failed", "Incorrect Username or password")
        except Exception as e:
            print(str(e))


    def signUp(self):
        try:
            name = self.username_3.text()
            password = self.password_3.text()
            
            isName = validations.name_validation(name)
            isPassword = validations.password_validation(password)

            if isName and isPassword:
                if Hashing_Password.signUp(name, password):
                    self.switch_to_login_page()
                else:
                    QMessageBox.information(self, 'SignUp', "Username already present", QMessageBox.Ok)
            else:
                if not isName:
                    QMessageBox.information(self, 'Error', "Username should not have symbols or empty space", QMessageBox.Ok)
                else:
                    QMessageBox.information(self, 'Error', "Password should have symbols and must have greater length than 5", QMessageBox.Ok)
        except Exception as e:
            print(e)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("MainWindow.ui",self)  # Load your UI file here
        self.load_table()
        self.load_table_transaction()
        #self.init_ui()
        #self.df = self.Read_CSV()
        #print(self.df.head())

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
        self.dataBtn.clicked.connect(self.switch_to_dataAnalysis_page)
        self.dataBtn_2.clicked.connect(self.switch_to_dataAnalysis_page)
        self.switch_to_home_page()
        self.homeBtn.clicked.connect(self.switch_to_home_page)
        self.homeBtn_2.clicked.connect(self.switch_to_home_page)
        self.searchBtn.clicked.connect(self.switch_to_search_page)
        self.searchBtn_2.clicked.connect(self.switch_to_search_page)
        self.addProductBtn.clicked.connect(self.switch_to_addProduct_page)
        self.addProductBtn_2.clicked.connect(self.switch_to_addProduct_page)
        self.deleteProductBtn.clicked.connect(self.switch_to_deleteProduct_page)
        self.deleteProductBtn_2.clicked.connect(self.switch_to_deleteProduct_page)
        self.viewProductsBtn.clicked.connect(self.switch_to_viewProducts_page)
        self.viewProductsBtn_2.clicked.connect(self.switch_to_viewProducts_page)
        self.graphBtn.clicked.connect(self.switch_to_transactionPage)
        self.graphBtn_2.clicked.connect(self.switch_to_transactionPage)
        self.addProductBtn_3.clicked.connect(self.add_product_ui)
        self.updateProductBtn.clicked.connect(self.switch_to_updateProduct_page)
        self.updateProductBtn_2.clicked.connect(self.switch_to_updateProduct_page)
        self.notificationBtn.clicked.connect(self.switch_to_notification_page)
        self.notificationBtn_2.clicked.connect(self.switch_to_notification_page)

        self.updateProductBtn_4.clicked.connect(self.transaction_ui)
        self.updateProductBtn_5.clicked.connect(self.undo_trasaction_ui)
        # Set selection mode to SingleSelection
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSelectionModel(QItemSelectionModel(self.tableView.model()))


        self.pushButton.clicked.connect(self.search_product_ui)
        self.pushButton_3.clicked.connect(self.delete_product_search_ui)
        self.deleteRowBtn.clicked.connect(self.delete_product_ui)
        self.pushButton_4.clicked.connect(self.update_product_search_ui)
        self.updateProductBtn_3.clicked.connect(self.update_product_ui)
        selection_model = self.tableView_3.selectionModel()
        selection_model.selectionChanged.connect(self.update_product_fillUp)


        # Set header text color
        header_stylesheet = "QHeaderView::section { background-color: #9AD0C2; }"
        self.tableView.horizontalHeader().setStyleSheet(header_stylesheet)
        self.tableView.verticalHeader().setStyleSheet(header_stylesheet)
        self.tableView_2.horizontalHeader().setStyleSheet(header_stylesheet)
        self.tableView_2.verticalHeader().setStyleSheet(header_stylesheet)
        self.tableView_3.horizontalHeader().setStyleSheet(header_stylesheet)
        self.tableView_3.verticalHeader().setStyleSheet(header_stylesheet)
        self.tableView_4.horizontalHeader().setStyleSheet(header_stylesheet)
        self.tableView_4.verticalHeader().setStyleSheet(header_stylesheet)
        self.tableView_6.horizontalHeader().setStyleSheet(header_stylesheet)
        self.tableView_6.verticalHeader().setStyleSheet(header_stylesheet)
        # Adjust column width based on window size
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setShowGrid(True)
        self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_2.horizontalHeader().setStretchLastSection(True)
        self.tableView_2.setShowGrid(True)
        self.tableView_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_3.horizontalHeader().setStretchLastSection(True)
        self.tableView_3.setShowGrid(True)
        self.tableView_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_4.horizontalHeader().setStretchLastSection(True)
        self.tableView_4.setShowGrid(True)
        self.tableView_6.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_6.horizontalHeader().setStretchLastSection(True)
        self.tableView_6.setShowGrid(True)


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
        self.pushButton_7.connect(self.Create_relational_graph)

        ####################################################################
        # Create a QStandardItemModel
        self.model_notification = QStandardItemModel()

        # Set the model to the QListView
        self.notificationView.setModel(self.model_notification)

        # Add sample notifications
        notification1 = QStandardItem("New message received")
        notification2 = QStandardItem("Reminder")
        self.model_notification.appendRow(notification1)
        self.model_notification.appendRow(notification2)

        # Set word wrap and style for the QListWidget
        self.notificationView.setWordWrap(True)
        # Set the delegate on the QListView
        self.notificationView.setItemDelegate(RoundedDelegate())
  #  def Create_relational_graph(self):

    def switch_to_dataAnalysis_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_home_page(self):
        self.stackedWidget.setCurrentIndex(2)    

    def switch_to_search_page(self):
        self.stackedWidget.setCurrentIndex(3)   

    def switch_to_addProduct_page(self):
        self.stackedWidget.setCurrentIndex(0)   

    def switch_to_deleteProduct_page(self):
        try:
            self.stackedWidget.setCurrentIndex(4)   
        except Exception as e:
            print(str(e))
    def switch_to_viewProducts_page(self):
        self.stackedWidget.setCurrentIndex(6)

    def switch_to_transactionPage(self):
        self.stackedWidget.setCurrentIndex(5)  

    def switch_to_updateProduct_page(self):
        self.stackedWidget.setCurrentIndex(7)        

    def switch_to_notification_page(self):
        self.stackedWidget.setCurrentIndex(8)

    def create_graph(self):
        data = [10, 20, 30, 40, 50]  # Sample data for the graph - replace with your data
        self.graph_widget.draw_graph(data, 'line')

    def create_pie_chart(self):
        data = [10, 20, 30, 40, 50]  # Sample data for the pie chart - replace with your data
        self.graph_widget.draw_graph(data, 'pie')

    def Read_CSV(self):
        self.df=pd.read_excel('sales_formatting_class.xlsx')
        return self.df
    
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

    #Add Product Functionality
    def add_product_ui(self):
        try:
            name = self.inputProductName.text()
            company = self.inputProductCompany.text()
            price = self.inputProductPrice.text()
            quantity = self.inputProductQuantity.text()
            threshold = self.inputProductThreshold_2.text()

            msg = crud_product.add_product(name, company, price, quantity, threshold)
            QMessageBox.information(self, "Message", msg)
            self.load_table()
        except Exception as e:
            print(str(e))    

    def search_product_ui(self):
        try:

            query = self.searchBar.toPlainText()
            if query is not None:
                isFound = crud_product.search_product(query)
                if isFound: 
                    self.load_searchResult()
                else:
                    QMessageBox.information(self, "Not Found", "No Such item is found")
        except Exception as e:
            print(str(e))

    def delete_product_search_ui(self):
        try:
            self.load_table()
            query = self.searchBar_2.toPlainText()
            if query is not None:
                self.clear_csv_file()
                isFound = crud_product.search_product(query)
                if isFound: 
                    self.load_searchResult()
                    
                else:
                    QMessageBox.information(self, "Not Found", "No Such item is found")
        except Exception as e:
            print(str(e))

    def delete_product_ui(self):
        try:
            table_view = self.tableView_2

            # Get the selected indexes
            selected_indexes = table_view.selectionModel().selectedRows()

            if not selected_indexes:
                return  # No selection

            # Get the selected row data from the model
            model = table_view.model()
            for index in selected_indexes:
                selected_row = index.row()
                selected_row_data = model.get_selected_row_data(selected_row)
            
            crud_product.delete_product(selected_row_data[0], selected_row_data[1], selected_row_data[2], selected_row_data[3],selected_row_data[4])
            self.load_table()
            # Notify the view that the data has changed
            model.layoutChanged.emit()

        except Exception as e:
            print(str(e))

    def update_product_ui(self):
        name = self.inputProductName_2.text() 
        company = self.inputProductCompany_2.text() 
        price = self.inputProductPrice_2.text() 
        quantity = self.inputProductQuantity_2.text()
        threshold = self.inputProductThreshold.text()

        try:

            crud_product.update_product(name, company, price, quantity, threshold)
            self.load_table()
            if quantity < threshold:
                self.add_notification(str(name) + " is below the threshold ","Its threshold is "+ str(threshold) +" but the quantity is " + str(quantity))
            elif threshold > quantity:
                self.remove_notification(self.add_notification(str(name) + " is below the threshold ","Its threshold is "+ str(threshold) +" but the quantity is " + str(quantity)))
        except Exception as e:
            QMessageBox.information(self, "Not Found ", str(e))
            
    def update_product_fillUp(self):
        try:
            table_view = self.tableView_3

            # Get the selected indexes
            selected_indexes = table_view.selectionModel().selectedRows()

            if not selected_indexes:
                return  # No selection

            # Get the selected row data from the model
            model = table_view.model()
            for index in selected_indexes:
                selected_row = index.row()
                selected_row_data = model.get_selected_row_data(selected_row)
            #Fill text boxes on bases of selected row
            self.inputProductName_2.setText(selected_row_data[0]) 
            self.inputProductCompany_2.setText(selected_row_data[1]) 
            self.inputProductPrice_2.setText(selected_row_data[2]) 
            self.inputProductQuantity_2.setText(selected_row_data[3])     
            self.inputProductThreshold.setText(selected_row_data[4])
            # Notify the view that the data has changed
            model.layoutChanged.emit()

        except Exception as e:
            print(str(e))

    def update_product_search_ui(self):
        try:
            query = self.searchBar_3.toPlainText()
            if query is not None:
                self.clear_csv_file()
                isFound = crud_product.search_product(query)
                if isFound: 
                    self.load_searchResult()
                    
                else:
                    QMessageBox.information(self, "Not Found", "No Such item is found")
        except Exception as e:
            print(str(e))

    def clear_csv_file(self,file_path = "searchedData.csv"):
    # Open the file in write mode, which clears its contents
        with open(file_path, 'w', newline='') as file:
            file.write("")

    def showContextMenu(self, position):
        menu = QMenu()
        delete_action = QAction('Delete Row', self)
        delete_action.triggered.connect(self.deleteRow)
        menu.addAction(delete_action)
        menu.exec_(self.tableView.viewport().mapToGlobal(position))   
    s = transaction___sales.Stack()
    
    def transaction_ui(self):
        try:
            new_transaction_data = {}
            name = self.inputProductName_3.text()
            quantity = self.inputProductQuantity_3.text()

            data = crud_product.search_product_transaction(name)
            
            if not data:
                QMessageBox.information(self, "Not Found", "This item is not present in the store")
            else:
                item = data[0]
                if int(quantity) > item[3]:
                    QMessageBox.information(self, "Not Enough Stock", "Store currently don't have that much" + " " + name)
                else:    
                    new_transaction_data['Name'] = item[0]
                    new_transaction_data['Company'] = item[1]
                    new_transaction_data['Price(RS)'] = item[2]
                    new_transaction_data['Quantity'] = quantity
                    new_transaction_data['Threshold'] = item[4]
                    item[3] -= int(quantity)
                    crud_product.update_product(item[0], item[1], item[2], item[3], item[4])
                    self.load_table() #Refresh data of all the tables
                    if item[3] < item[4]:
                        self.add_notification(str(item[0]) + " is below the threshold ","Its threshold is "+ str(item[4]) +" but the quantity is " + str(item[3]))
                    if 'new_transaction' not in locals():
                        new_transaction = []

                    new_transaction.append(new_transaction_data)

                    new_transaction_df = pd.DataFrame(new_transaction_data, index=[pd.Timestamp.now()])

                    self.s.push(new_transaction_df)
                    self.load_table_transaction()
        
        except Exception as e:
            print(e)


    def undo_trasaction_ui(self):
        try:
            count = 1  # You can adjust this count based on your requirements
            undone_transactions = self.s.pop(count)
            
            if undone_transactions is not None:
                for _, transaction_data in undone_transactions.iterrows():
                    # Access data in undone transaction_data DataFrame
                    name = transaction_data['Name']
                    company = transaction_data['Company']
                    price = transaction_data['Price(RS)']
                    quantity = transaction_data['Quantity']
                    threshold = transaction_data['Threshold']
                    
                self.load_table_transaction()
                data = crud_product.search_product_transaction(name)
                item = data[0]
                item[3] += int(quantity)
                if item[3] > item[4]:
                    self.remove_notification(str(item[0]) + " is below the threshold ","Its threshold is "+ str(item[4]) +" but the quantity is " + str(item[3]))
                crud_product.update_product(name, company, price, item[3], threshold)
                self.load_table()
        except Exception as e:
            print(e)

    def load_table(self):
        with open('products.csv', "r",encoding="utf-8") as fileInput:
            roww = 0
            data = list(csv.reader(fileInput))
            model = TableModel(data)
            self.tableView.setModel(model)
            self.tableView_2.setModel(model)  
            self.tableView_3.setModel(model)
        selection_model = self.tableView_3.selectionModel()
        selection_model.selectionChanged.connect(self.update_product_fillUp)

    def load_searchResult(self):
        with open('searchedData.csv', "r",encoding="utf-8") as fileInput:
            roww = 0
            data = list(csv.reader(fileInput))
            model = TableModel(data) 
            self.tableView_4.setModel(model)
            self.tableView_2.setModel(model) 
            self.tableView_3.setModel(model)  
        selection_model = self.tableView_3.selectionModel()
        selection_model.selectionChanged.connect(self.update_product_fillUp)
            
    ##########################################################################################3
            #######################################################################33
    # def load_table_transaction(self):
    #     try:
    #         with open('sales.csv', "r", encoding="utf-8") as fileInput:
    #             data = list(csv.reader(fileInput))
    #             if len(data) < 1:
    #                 headers = ["Name", "Company", "Price(RS)", "Quantity"]
    #                 self.empty_model = HeadersTableModel(headers)
    #                 self.tableView_6.setModel(self.empty_model)
    #             else:
    #                 model = TableModel(data)
    #                 self.tableView_6.setModel(model)
    #     except Exception as e:
    #         print(e)
            
        def load_table_transaction(self):
            with open('sales.csv', "r", encoding="utf-8") as fileInput:
                data = list(csv.reader(fileInput))
                model = TableModel(data)
                self.tableView_6.setModel(model)
        
    def add_data_to_headers_model(self, new_data):
        try:
            if isinstance(self.tableView_6.model(), TableModel):
                model = self.tableView_6.model()
                model.add_data(new_data)
                # Notify the view to update after adding data
                model.layoutChanged.emit()
        except Exception as e:
            print(e)

    #######################################################################
    # def add_notification(self, title, message, icon_path):
    #     item = QListWidgetItem()
    #     item.setText(f"{title}\n{message}")
    #     item.setIcon(QIcon(icon_path))
    #     item.setSizeHint(item.sizeHint() + QSize(10, 10))  # Adjust the size
    #     item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    #     self.notificationView.addItem(item)
    def add_notification(self, title, message):     
        if title in self.items:
            existing_item = self.items[title]
            existing_item.setText(f"{title}\n{message}")  # Update the message
        else:
            # Add a new notification if not present
            item = QStandardItem(f"{title}\n{message}")
            self.model.appendRow(item)
            self.items[title] = item 

    def remove_notification(self, title, message):
        # Search for the item with the specified title and message
        for item in self.items:
            if item.text() == f"{title}\n{message}":
                self.items.remove(item)
                self.model.removeRow(item.row())
                break 
    #######################################################################                

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
        names = ['Apple', 'Banana', 'Orange', 'Pineapple', 'Grapes','Pta Nai']
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
        # elif graph_type == 'pie':
        #     if labels is None:
        #         labels = [f'Data {i}' for i in range(len(data))]
        #     self.ax.pie(data, labels=names, startangle=140)
        #     self.ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

        self.canvas.draw()

class TableModel(QAbstractTableModel):
    def __init__(self, data=None):
        super().__init__()
        self._data = data if data is not None else []
        self._headers = ["Name", "Company", "Price(RS)", "Quantity","Threshold"]

    def set(self, data):
        self._data = data

    def rowCount(self, index):
        return max(1, len(self._data))  # Ensure at least one row for headers

    def columnCount(self, index):
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or role != Qt.DisplayRole:
            return QVariant()

        if len(self._data) == 0:
            return QVariant()  # No data, return empty QVariant for display

        return self._data[index.row()][index.column()]

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                if section < len(self._headers):
                    return self._headers[section]
            elif orientation == Qt.Vertical:
                return str(section + 1)  # Adding numbering starting from 1 for vertical header
        return QVariant()

    def get_selected_row_data(self, selected_row):
        if 0 <= selected_row < len(self._data):
            return self._data[selected_row]
        return None

    def add_data(self, new_data):
        if len(new_data) != len(self._headers):
            return False  # Ensure the length of new data matches the number of columns

        self.beginInsertRows(QModelIndex(), len(self._data), len(self._data))
        self._data.append(new_data)
        self.endInsertRows()
        return True
    
class RoundedDelegate(QStyledItemDelegate):
        def sizeHint(self, option, index):
            size = super().sizeHint(option, index)
            size.setHeight(size.height() + 20)  # Increase the height by 10 pixels
            return size

        def paint(self, painter, option, index):
            # Set the background color and round corners
            painter.save()
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor("#9AD0C2"))
            painter.drawRoundedRect(option.rect, 20, 20)

            # Draw the item text
            text = index.data(Qt.DisplayRole)
            painter.setPen(Qt.black)
            painter.drawText(option.rect, Qt.AlignCenter, text)

            painter.restore()
        
# class TableModel(QAbstractTableModel):
#     def __init__(self,data):
#         super().__init__()
#         self._data = data
#         self._headers = ["Name", "Company", "Price(RS)", "Quantity"]

#     def set(self, data):
#         self._data = data

#     def rowCount(self, index):
#         return len(self._data)

#     def columnCount(self, index):
#         return len(self._data[0])


#     def data(self, index, role=Qt.DisplayRole):
#         if not index.isValid() or role != Qt.DisplayRole:
#             return QVariant()
#         return self._data[index.row()][index.column()]

#     def headerData(self, section, orientation, role=Qt.DisplayRole):
#         if role == Qt.DisplayRole:
#             if orientation == Qt.Horizontal:
#                 if section < len(self._headers):
#                     return self._headers[section]
#             elif orientation == Qt.Vertical:
#                 return str(section + 1)  # Adding numbering starting from 1 for vertical header
#         return QVariant()    

#     def get_selected_row_data(self, selected_row):
#         if 0 <= selected_row < len(self._data):
#             return self._data[selected_row]
#         return None

# class HeadersTableModel(QAbstractTableModel):
#     def __init__(self, headers=None, data=None):
#         super().__init__()
#         self._headers = headers if headers else []
#         self._data = data if data else []

#     def rowCount(self, index):
#         return len(self._data)

#     def columnCount(self, index):
#         return len(self._headers)

#     def headerData(self, section, orientation, role=Qt.DisplayRole):
#         if role == Qt.DisplayRole:
#             if orientation == Qt.Horizontal:
#                 if section < len(self._headers):
#                     return self._headers[section]
#         return QVariant()

#     def add_data(self, new_data):
#         self.beginResetModel()
#         self._data.extend(new_data)
#         self.endResetModel()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow_2()
    window.show()
    sys.exit(app.exec_())


