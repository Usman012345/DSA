import pandas as pd

class KeyNode:
    def __init__(self, key, value):
        self.value = value
        self.key = key

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[]]*self.size

        self.key_occupied = 0

    def get_hash(self, key):
        hash_value = 0
        key = str(key)
        for c in key:
            hash_value = (hash_value * 31) + ord(c)
        return (hash_value %self.size)
    
    def update_key(self, key, value):
        index = self.get_hash(key.lower())
        
        #if the key is already present, update value
        for node in self.table[index]:
            if node.key == key:
                node.value = value
                return
        
        #else it will add new keyNode
        self.table[index].append(KeyNode(key, value))
        self.key_occupied += 1 


        if self.key_occupied > self.size * 0.7:
            self.rehash()


    def rehash(self):
        new_size = self.size * 2
        new_table = [[]] * new_size

        for bucket in self.table: #go to the chain on an index
            for node in bucket: #transverse chain of nodes on the table
                index = self.get_hash(node.key)
                new_table[index].append(node)

        self.table = new_table
        self.size = new_size

    def search_key(self, key):
        index = self.get_hash(key.lower())
        for node in self.table[index]:
            if node.key.lower() == key.lower():
                return node.value
        return -1  # Key not found



t = HashTable(10)
value = 0
t.update_key("Falfal", value)
value += 1
t.update_key("heheheheh", value)
value += 1
t.update_key("A",value)
value += 1
t.update_key("B", value)
value += 1
t.update_key("C", value)
value += 1
t.update_key("D", value)
value += 1

if t.search_key("a") != -1:
    print("Found it")
else:
    print("Sheeeeeet")
