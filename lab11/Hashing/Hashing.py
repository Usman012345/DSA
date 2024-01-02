import numpy as np
from Node import Node
import sys
from Hashtable import Hashtable
import pandas as pd
def read_file():
    df = pd.read_csv("Doc.txt")
    return df
def add_to_table(obj,Node):
    if obj.size==0:
      obj.size+=1
      x= obj.HashFunction(node.key)
      obj.arr[x]=Node
    else:
     obj.UpdateKey(Node)
strings=read_file()
x=128
obj=Hashtable(x)
for i in strings:  
    node=Node(i,1)
    add_to_table(obj,node)
key="Usman"
result_node=obj.SearchKey(key)
if result_node!=0:
    print(result_node.key,result_node.data)
else:
    print(result_node)

