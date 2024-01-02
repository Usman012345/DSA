from Node_ import Node_
class linklist(object):
    def __init__(self):
        self.head = None
    def insert_first(self,data):
       node=Node_(data)
       if self.head==None:
           self.head=node
       else:
           node.next=self.head
           self.head=node
           node.previous=self.head
    def insert_last(self,data):
        node=Node_(data)
        if self.head is None:
            self.head=node
        else:
            current_node=self.head
            while(current_node.next):
                current_node=current_node.next
            current_node.next=node
            current_node.next.previous=current_node
    def insert_index(self,data,index):
        node=Node_(data)
        current_node=self.head
        p=0
        if p==index:
            self.insert_first(data)
        else:
            current_node=self.head
            while current_node.next!=None and p<index-1:
                p+=1
                current_node=current_node.next
            if current_node !=None:
                node.next=current_node.next
                node.previous=current_node
                current_node.next=node
            else:
                print("doesn't exist")
    def update_node(self,data,index):
        current_node=self.head
        p=0
        if p==index:
            current_node.data=data
        else:
            while current_node.next!=None and p<index:
                p+=1
                current_node=current_node.next
            if current_node !=None:
                current_node.data=data
            else:
                print("doesn't exist")
    def remove_first(self):
        if self.head==None:
            return
        else:
            self.head=self.head.next
    def remove_last(self):
        if self.head==None:
            return
        else:
            current_node=self.head
            while current_node.next!=None:
                current_node=current_node.next
            current_node.next=None
    def remove_index(self,index):
        if self.head==None:
            return
        else:
            current_node=self.head
            p=0
            if p==index:
                self.head=self.head.next
            else:
                while current_node.next!=None and p<index-1:
                    p+=1
                    current_node=current_node.next
                if current_node != None:
                    current_node.next = current_node.next.next
                    current_node.next.next.previous=current_node
                else:
                    print("doesn't exist")
    def get_index(self,index):
        if self.head==None:
            return
        else:
            current_node=self.head
            p=0
            if p==index:
                self.head=self.head.next
            else:
                while current_node.next!=None and p<index-1:
                    p+=1
                    current_node=current_node.next
                if current_node != None:
                    return current_node.next
                else:
                    print("doesn't exist")
    def remove_node(self, data):
        current_node = self.head
        while(current_node != None and current_node.next!=None):
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                current_node.next.next.previous=current_node
                return
            else: 
                current_node=current_node.next
        print("Not found")
    def get_node(self, data):
        current_node = self.head
        while(current_node != None and current_node.next!=None):
            if current_node.next.data == data:
                return current_node.next
            else: 
                current_node=current_node.next
        print("Not Found")      
        
    def print_(self):
         current_node=self.head
         while current_node:
             print(current_node.data)
             current_node=current_node.next
    def size_(self):
        count=0
        if self.head!=None:
            current_node=self.head
            while current_node:
                current_node=current_node.next
                count+=1
            return count
        else:
            return 0
    def reverse_list(self):
        prev = None
        current_node = self.head 
        while(current_node != None): 
            next = current_node.next
            current_node.next = prev 
            prev = current_node 
            current_node = next
        self.head = prev 
    def sortlist(self):
        temp=Node_
        current_node=self.head
        while current_node and current_node.next:
            if current_node.next.data:
                if current_node.data>current_node.next.data:
                    temp.data=current_node.data
                    current_node.data=current_node.next.data
                    current_node.next.data=temp.data
            else: 
                return 
            current_node=current_node.next
            self.print_()
    def remove_duplicate(self):
        current_node = self.head
        iter=self.head
        temp=None
        while(current_node != None):
            data=current_node.data
            temp=current_node
            while current_node.next!=None:
                if current_node.next.data==data and current_node.next.next!=None:
                    current_node.next=current_node.next.next
                elif current_node.next.next==None and current_node.next.data==data:
                    current_node.next=None
                else:
                    current_node=current_node.next
            current_node=temp
            current_node = current_node.next
    def merge_list(self,list2):
        current_node1=self.head
        current_node2=list2.head
        while current_node1 and current_node2:
            if current_node1.next:
                current_node1=current_node1.next
            else:
                current_node1.next=current_node2
                return
    def intersection(self,list2):
        current_node1=self.head
        current_node2=list2.head
        result= linklist()
        result.print_()
        if current_node1 and current_node2:
            while current_node1:
                temp=current_node2
                print(current_node1.data)
                while current_node2:
                    print(current_node2.data)
                    if current_node1.data==current_node2.data:
                        result.insert_first(current_node1.data) 
                        break
                    current_node2=current_node2.next
                current_node2=temp
                current_node1=current_node1.next
        return result