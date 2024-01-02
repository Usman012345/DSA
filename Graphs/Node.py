
class Node_(object):
    def __init__(self, data):
        self.neighbours=[]
        self.data = data
        self.next = None
        self.previous=None
        self.status="Unvisited"
    #def __init__(self,data):
     #   self.neighbours=None
      #  self.data = data
       # self.next = None
        #self.previous=None
    