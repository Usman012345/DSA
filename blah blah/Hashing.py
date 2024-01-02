import pandas as pd
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        hash_value = 0
        key = str(key)
        for c in key:
            hash_value = (hash_value * 31) + ord(c)
        return hash_value % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = Node(key, value)

    def get(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(f"Key not found: {key}")
    
    def search(self, query):
        foundData = [] 
        if query is not None:
            query = str(query).lower()
            
            for i in self.table:
                while i:
                    # Check if any part of the item matches the query
                    if (
                        query in i.value.name.lower()
                        or query in i.value.company.lower()
                        or query in str(i.value.price)
                        or query in str(i.value.quantity)
                    ):
                        foundData.append([i.value.name, i.value.company, i.value.price, i.value.quantity])
                    i = i.next
        return foundData
    
    def isExist(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key and current.value.company == value.company:
                return True
            current = current.next
        return False

    def update(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next
        raise KeyError(f"Key not found: {key}")

    def delete(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        previous = None
        while current:
            if current.key == key and current.value.company == value.company:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                return
            previous = current
            current = current.next
        raise KeyError(f"Key not found: {key}")
    
    def save_to_csv(self, filename = "products.csv"):
        data = []
        for node in self.table:
            while node:
                data.append([
                    node.key,
                    node.value.company,
                    node.value.price,
                    node.value.quantity,
                    node.value.threshold])
                node = node.next

        df = pd.DataFrame(data, columns=["Name", "Company", "Price(RS)", "Quantity", "Threshold"])
        df.to_csv(filename, index=False)

