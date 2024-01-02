import pandas as pd

class KeyNode:
    def __init__(self, key, value):
        self.value = value
        self.key = key

class PasswordHashing:
    def __init__(self, size):
        self.size = size
        self.password_table = [[] for _ in range(self.size)]
        self.key_occupied = 0
        self.read_csv("passwords.csv")

    def get_hash(self, password):
        hash_value = 0
        password = str(password)
        for c in password:
            hash_value = (hash_value * 31) + ord(c)
        return hash_value % self.size
    
    def hash_password(self, password):
        result = ""
        for i in password:
            result += chr(ord(i) % 20 + 10)   #can be changed for stronger hashing
        return result
    
    def update_key(self, username, password):
        index = self.get_hash(username)

        # If the key (username) is already present, update value (hashed password)
        for node in self.password_table[index]:
            if node.key == username:
                node.value = self.hash_password(password)
                return

        # Otherwise, add a new KeyNode with the hashed password
        self.password_table[index].append(KeyNode(username, self.hash_password(password)))
        self.key_occupied += 1

        if self.key_occupied > self.size * 0.7:
            self.rehash()

    def rehash(self):
        new_size = self.size * 2
        new_table = [[] for _ in range(new_size)]

        for bucket in self.password_table:
            for node in bucket:
                index = self.get_hash(node.key)
                new_table[index].append(node)

        self.password_table = new_table
        self.size = new_size

    def username_exists(self, username):
        index = self.get_hash(username)

        # Check if the username already exists in the password table
        for node in self.password_table[index]:
            if node.key == username:
                return True  # Username exists

        return False  # Username does not exist

    def verify_password(self, username, password):
        index = self.get_hash(username)

        for node in self.password_table[index]:

            if node.key == username and node.value == self.hash_password(password):
                return True  # Password matched

        return False  # Username or password not found

    def save_to_csv(self, filename):
        data = []

        for bucket in self.password_table:
            for node in bucket:
                data.append({'username': node.key, 'password_hash': node.value})

        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)

    def read_csv(self, filename):
        df = pd.read_csv(filename)
        for _, row in df.iterrows():
            username = row['username']
            password_hash = row['password_hash']
            index = self.get_hash(username)
            self.password_table[index].append(KeyNode(username, password_hash))

def signUp(userName, password):
    if password_hashing.username_exists(userName):
        return False
    else:
        password_hashing.update_key(userName, password)
        password_hashing.save_to_csv("passwords.csv")
        return True

def signIn(userName, password):
    if password_hashing.verify_password(userName, password):
        return True
    
    return False

password_hashing = PasswordHashing(size=10)
