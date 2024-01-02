import sys
class Hashtable(object):
    def __init__(self,size):
        self.arr=[0]*size
        self.size=0
        self.count=0
    def constructor(self,hsize):
         arr=[0]*hsize
         return arr
    def hash_size(self):
        return self.size
    def GetNumberOfKeys():
        return self.count
    def HashFunction(self,key):
        x=128
        sum=0
        for i in key:
            sum+=ord(i)
        return sum %x 
    def SearchKey(self,key):
       val= self.HashFunction(key)
       for i in range(0,len(self.arr)):
           if val==i:
               return self.arr[i]
       return 0
    def UpdateKey(self,node):
       added=False
       obj=  self.SearchKey(node.key)
       if obj==0:
          self.size+=1
          x= self.HashFunction(node.key)
          if self.arr[x]==0:
            self.arr[x]=node
          else:
            for i in range(x,len(self.arr)):
                if self.arr[i]==0:
                    self.arr[i]=node
                    added=True
       else:
           obj.data+=1
           added=True
       if added==True:
           return added
       else:
           rehash()
           self.UpdateKey(node)
    def rehash():
        return self.arr % len(self.arr)*2