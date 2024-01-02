class stack_(object):
    """description of class"""
    def __init__(self):
        self.arr=[]

    def push(self,data):
       if len(self.arr)<10:
           self.arr.append(None)
           for i in reversed(range(0,len(self.arr)-1)):
                    self.arr[i+1]=self.arr[i]
           self.arr[0]=data
       else:
           print("overflow")
    def pop(self):
       if self.arr:
        del self.arr[-1]
       else:
           print("Underflow")
    def top(self):
        if self.arr:
            return self.arr[0]
        else:
            print("underflow")
    def print_(self):
        print(self.arr)

obj= stack_()

obj.push(3)
obj.push(4)
obj.print_()
obj.pop()
obj.print_()
                    
                    





    

