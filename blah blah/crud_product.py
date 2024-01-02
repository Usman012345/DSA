import validations
import pandas as pd
import Hashing

hash_table = Hashing.HashTable(size=10)
class product:
    def __init__(self, name, company, price, quantity, threshold):
        self.name = name
        self.company = company
        self.price = price
        self.quantity = quantity
        self.threshold = threshold

def add_product(name, company, price, quantity, threshold):
    isName = validations.string_validation(name)
    isCompany = validations.string_validation(company)
    isQuantity = validations.int_validation(quantity)
    isPrice = validations.int_validation(price)
    isThreshold = validations.int_validation(threshold)

    if isName and isCompany and isQuantity and isPrice and isThreshold:
        p = product(name, company, price, quantity, threshold)

        if not hash_table.isExist(name, p):

            hash_table.insert(p.name, p)
            hash_table.save_to_csv()
            return ("Product has been added")
        else:
            return ("Product same Name and company already present")    
    else:
        # Handle validation errors
        if not isName:
            return("Product name should not have Digits or be empty")
        elif not isCompany:
            return("Company name should not have Digits or be empty")
        elif not isQuantity:
            return("Quantity cannot have character or empty space")
        elif not isPrice:
            return("Price cannot have character or empty space")

def update_product(name, company, price, quantity, threshold):
    isName = validations.string_validation(name)
    isCompany = validations.string_validation(company)
    isQuantity = validations.int_validation(quantity)
    isPrice = validations.int_validation(price)
    isThreshold = validations.int_validation(threshold)

    if isName and isCompany and isQuantity and isPrice and isThreshold:
        p = product(name, company, price, quantity, threshold)

        # Call the update_key method on the instance
        hash_table.update(p.name, p)
        hash_table.save_to_csv()
        return ("Product has been updated")
    else:
        # Handle validation errors
        if not isName:
            return("Product name should not have Digits or be empty")
        elif not isCompany:
            return("Company name should not have Digits or be empty")
        elif not isQuantity:
            return("Quantity cannot have character or empty space")
        elif not isPrice:
            return("Price cannot have character or empty space")
        elif not isThreshold:
            return("Thresholf cannot have characters or empty space")


def delete_product(name, company, price, quantity,threshold):
    p = product(name, company, price,quantity, threshold)
    hash_table.delete(name, p)
    hash_table.save_to_csv()

def search_product(query):
    data = hash_table.search(query)
    if data:
        save_search_file(data)
        return True
    else:
        return False

def search_product_transaction(query):
    data = hash_table.search(query)
    if data:
        save_search_file(data)
        return data
    else:
        return data
    

def save_search_file(data,filename = "searchedData.csv"):
    df = pd.DataFrame(data, columns=["Name", "Company", "Price(RS)", "Quantity", "Threshold"])
    df.to_csv(filename, index=False)

def load_from_csv(filename = "products.csv"):
        df = pd.read_csv(filename)
        for _, row in df.iterrows():
            name, company, price, quantity, threshold = row["Name"], row["Company"], row["Price(RS)"], row["Quantity"], row["Threshold"]
            p = product(name, company, price, quantity, threshold)
            hash_table.insert(name, p)

load_from_csv()