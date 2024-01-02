import pandas as pd
import os

class Stack:
    def __init__(self, file_path = "sales.csv"):
        self.transactions = pd.DataFrame()
        self.file_path = file_path

    def is_empty(self):
        return self.transactions.empty

    def push(self, new_transaction):
        self.load_from_csv()  
        self.transactions = pd.concat([self.transactions, new_transaction], ignore_index=True)
        self.save_to_csv()

    def pop(self, count=1):
        if not self.is_empty():
            undone_transactions = self.transactions.tail(count)
            self.transactions = self.transactions.iloc[:-count]
            self.save_to_csv()
            return undone_transactions
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.transactions.tail(1)
        else:
            return None

    def load_from_csv(self):
        try:
            self.transactions = pd.read_csv(self.file_path)
        except FileNotFoundError:
            pass

    def save_to_csv(self):
        self.transactions.to_csv(self.file_path, index=False)

class Product:
    def __init__(self, product_id, name, quantity, limit, file_path):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.limit = limit
        self.file_path = file_path
        self.notifications = []

    def add_notification(self, notification):
        i=0
        self.notifications.append(notification)
        print(self.notifications[i])
        i+=1
    def remove_notification(self, notification):
        self.notifications.remove(notification)
    def decrease_quantity(self, quantity_sold,transaction_stack):
        self.quantity -= quantity_sold
        self.save_to_csv()

        if self.quantity < self.limit:
            notification_ = f"Low stock: {self.quantity} units"
            notification_message=f"Notification: {self.name} (Order ID: {self.product_id}) is {notification_}."
            self.add_notification(notification_message)

        print(f"Successfully sold {quantity_sold} units of {self.name}.")


    def increase_quantity(self, quantity_inc,transaction_stack):
        self.quantity += quantity_inc
        self.save_to_csv()

        for notification in self.notifications.copy():
            if "Low stock" in notification and self.quantity > self.limit:
                self.remove_notification(notification)
                print(f"Notification removed for {self.name} (Order ID: {self.product_id}): Stock is back to normal.")

        print(f"Product quantity increased to {self.quantity}.")

    def load_from_csv(self):
        try:
            transactions_df = pd.read_csv(self.file_path)
            product_data = transactions_df[transactions_df['Product'] == self.name]
            if not product_data.empty:
                self.quantity = int(product_data['Quantity Ordered'])
        except FileNotFoundError:
            pass

    def save_to_csv(self):
        transactions_df = pd.read_csv(self.file_path)
        product_index = transactions_df[transactions_df['Product'] == self.name].index
        transactions_df.loc[product_index, 'Quantity Ordered'] = self.quantity
        transactions_df.to_csv(self.file_path, index=False)


def read_products_from_csv(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return []

    products_df = pd.read_csv(file_path, usecols=['Order ID', 'Product', 'Quantity Ordered'])

    products = []

    for _, row in products_df.iterrows():
        product_id = row['Order ID']
        name = row['Product']
        quantity = row['Quantity Ordered']
        limit = 1
        product = Product(product_id=product_id, name=name, quantity=quantity, limit=limit, file_path=file_path)
        products.append(product)
    return products
def process_low_stock_notifications(products):
    for product in products:
        if product.quantity < product.limit:
            notification_ = f"Low stock: {product.quantity} units"
            notification_message=f"Notification: {product.name} (Order ID: {product.product_id}) is {notification_}."
            product.add_notification(notification_message)
def print_low_stock_notifications(products):
    for product in products:
        product.print_notification()

# def main():
#     csv_file_path = r'Sales_December_2019.csv'
#     while True:
#         transaction_stack = Stack(csv_file_path)
#         products = read_products_from_csv(csv_file_path)
#         transaction_stack.load_from_csv()
#         print("\nOptions:")
#         print("1. Add transaction")
#         print("2. Undo last transaction(s)")
#         print("3. View current transactions")
#         print("4. Show low-stock products")
#         print("5. Buy product")
#         print("6. Increase product quantity (Admin)")
#         print("7. exit")

#         user_choice = input("Enter your choice : ")

#         if user_choice == '1':
#             new_transaction_data = {}
#             for column in transaction_stack.transactions.columns:
#                 new_value = input(f"Enter the {column}: ")
#                 new_transaction_data[column] = [new_value]

#             new_transaction = pd.DataFrame(new_transaction_data)
#             transaction_stack.push(new_transaction)
#             print("Transaction added successfully!")

#         elif user_choice == '2':
#             count_to_undo = int(input("Enter the number of transactions to undo: "))
#             undone_transactions = transaction_stack.pop(count_to_undo)
#             if undone_transactions is not None:
#                 print("Undone Transactions:\n", undone_transactions)
#             else:
#                 print("No transactions to undo.")
#         elif user_choice == '3':
#             print("Current Transactions:\n")
#             print(transaction_stack.transactions)

#         elif user_choice == '4':
#             process_low_stock_notifications(products)

#         elif user_choice == '5':
#             product_id_to_buy = input("Enter the Product ID to buy: ")
#             quantity_to_buy = int(input("Enter the quantity to buy: "))
#             for product in products:
#                 if product.product_id == int(product_id_to_buy):
#                     if product.quantity >= quantity_to_buy and quantity_to_buy <= product.limit:
#                         product.decrease_quantity(quantity_to_buy,transaction_stack) 
#                     elif quantity_to_buy > product.limit:
#                         print(f"Quantity exceeds the product limit of {product.limit}.")
#                     else:
#                         print("Insufficient quantity in stock.")
#                     break
#             else:
#                 print("Product not found.")



#         elif user_choice == '6':

#             admin_product_id = input("Enter the Product ID to increase quantity: ")
#             admin_quantity_increase = int(input("Enter the quantity to increase: "))
#             for product in products:
#                 if product.product_id == int(admin_product_id):
#                     product.increase_quantity(admin_quantity_increase,transaction_stack)
#                     product.save_to_csv()
#                     break
#             else:
#                 print("Product not found.")

#         elif user_choice == '7':
#             transaction_stack.save_to_csv()
#             print("Transactions saved. Exiting...")
#             break

# if __name__ == "__main__":
#     main()
