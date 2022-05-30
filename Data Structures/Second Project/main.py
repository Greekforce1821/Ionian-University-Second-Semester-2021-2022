from itertools import count
import os

class node:
    def init_(self):
        self.fID = ""                       #self.fID corresponds to the ID
        self.fn = ""                        #self.fn corresponds to the First Name
        self.ln = ""                        #self.ln corresponds to the Last Name
        self.gr = 0.0                       #self.gr corresponds to the Grade
        self.ap = 0                         #self.ap corresponds to the
        self.left = None                    #self.left corresponds to the left part of the node
        self.right = None                   #selft.right corresponds to the right part of the node
        
def Node():                                 #This function Node stores the data which was given by the user in a specific array called dataRecord
    r = node()
    textline = input("Give us some data:")
    dataRecord = textline.strip().split()
    r.fID = dataRecord[0]                   #The variable r.fID corresponds to the first value of the dataRecord Array
    r.fn = dataRecord[1]                    #The variable r.fn corresponds to the second value of the dataRecord Array
    r.ln = dataRecord[2]                    #The variable r.ln corresponds to the third value of the dataRecord Array
    r.gr = float(dataRecord[3])             #The variable r.gr corresponds to the forth value of the dataRecord Array
    r.ap = int(dataRecord[4])               #The variable r.ap corresponds to the fifth vavlue of the dataRecord Array
    return r

def addInOrder(root,new):                   #This function addInOrder sorts the data from the array in order                     
    if new.ID <= root.ID:
        if root.left == None:
            root.left = new
        else:
            addInOrder(root.left,new) 
    else: 
        if root.right == None:
            root.right = new
        else:
            addInOrder(root.right,new) 
            
def showInOrder(root):
    if root != None:
        showInOrder(root.left)
        print(("%s %s %s %.2f %d") % (root.ID, root.fn, root.ln, root.gr, root.ap))
        showInOrder(root.right)

def countNodes(root):
    result = 0
    
    if root  != None:
        result = countNodes(root.left)
        result = result + 1
        result += countNodes(root.right)
    return result            
     
def findByID(root,fID):
    result = None
    
    if root != None:
        if fID < root.ID:
            result = findByID(root.left,fID)
        elif fID == root.ID:
            result = root
        else:
            result = findByID(root.right, fID)
    return result

def maxID(root):
    if root.right == None:
        result = root
    else:
        result = maxID(root.right)
    return result

def maxGrade(root):
    result = -1
    
    if root != None:
        result = maxGrade(root.left)
        if result < root.gr:
            result = root.gr
        resultRight = maxGrade(root.right)
        if result < resultRight:
            result = resultRight
    return result

root = None

print("---------- Menu ----------")
print("1. Add in Order")
print("2. Show in Order")
print("3. Find Student by Grade")
print ("4. Show Last Student by Grade")  
print("5. Show Maximum Grade")
print ("0. Exit")  
ch = input("Choice: ").strip()

while ch != "0":
    if ch == "1":
        temp = createNode()
        if root == None:
            root = temp
        else:
            addInOrder(root, temp)

