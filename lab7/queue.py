class Queue_(object):
    def __init__(self):
        self.arr=[]
    def add(self,data):
        if len(self.arr)<10:
            self.arr.append(data)
        else:
            print("Overflow")
    def remove(self):
        if self.arr:
           temp= self.arr[-1]
           del self.arr[-1]
           return temp
        else:
           print("Underflow")
    def peek(self):
        if self.arr:
            return self.arr[-1]
        else:
            print("Underflow")
    def isfull(self):
        if self.arr:
            if len(self.arr)==10:
                print("yes")
            else:
                print("no")
    def isempty(self):
        if self.arr:
            print("no")
        else:
            print("yes")
    def print_(self):
        print(self.arr)
        
obj=Queue_()
obj.add(1)
obj.add(3)
obj.print_()
obj.remove()
obj.isfull()
obj.isempty()
obj.print_()
obj.peek()





