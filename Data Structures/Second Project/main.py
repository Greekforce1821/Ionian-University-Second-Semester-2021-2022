from itertools import count
import os
import csv
from pprint import pprint
from re import X
import time
from tkinter import Y
from matplotlib import pyplot as plt
import sys


tm_spnd = 0.0                               #tm_spnd calculates the time which was spent while inserting the data to the Node
counter = 0                                 #The counter counts the successful tries of inserting data
counting_data = [100]                       #This specific array called counting_data counts the 100 inputs from the user in order to create a graphical block diagram
dataRecord = []                             #Creating an empty array called dataRecord

with open('MOCK_DATA.csv', newline='') as file:       #Opening the .csv file and transfer the data from it to the array
    reader = csv.reader(file)
    header = next(reader) 
        
    for row in reader:
        id = int(row[0])
        fn = str(row[1])
        ln = str(row[2])
        gr = float(row[3])
        dataRecord.append([id, fn, ln, gr])  

class node:
    def __init__(self):
        self.fID = int                      #self.fID corresponds to the ID
        self.fn = ""                        #self.fn corresponds to the First Name
        self.ln = ""                        #self.ln corresponds to the Last Name
        self.gr = 0.0                       #self.gr corresponds to the Grade                       
        self.left = None                    #self.left corresponds to the left part of the node
        self.right = None                   #selft.right corresponds to the right part of the node
 
 
                          
x = 0                                       #Creating a counter x for the dataRecord array
y = 0                                       #Creating a counter y for the dataRecord array
z = 0                                       #Creating a counter z for the dataRecord array
m = 0                                       #Creating a counter m for the dataRecord array
    
        
def Node():                                 #This function Node stores the data which was given by the user in a specific array called dataRecord.
    r = node()
    r.fID = dataRecord[x][0]                   #The variable r.fID corresponds to the first value of the dataRecord Array
    r.fn = dataRecord[y][1]                    #The variable r.fn corresponds to the second value of the dataRecord Array
    r.ln = dataRecord[z][2]                    #The variable r.ln corresponds to the third value of the dataRecord Array
    r.gr = float(dataRecord[m][3])             #The variable r.gr corresponds to the forth value of the dataRecord Array            
    return r

def addInOrder(root,new):                   #This function addInOrder sorts the data from the array in order.                    
    if new.fID <= root.fID:
        if root.left == None:
            root.left = new
        else:
            addInOrder(root.left,new) 
    else: 
        if root.right == None:
            root.right = new
        else:
            addInOrder(root.right,new) 
            
def showInOrder(root):                      #This function showInOrder sorts the data from the array in order.  
    if root != None:
        showInOrder(root.left)
        print(("%s %s %s %.2f %d") % (root.ID, root.fn, root.ln, root.gr,))
        showInOrder(root.right)

def countNodes(root):                       #This function countNodes counts the succesful results of finding the items that the user had entered earlier.
    result = 0
    
    if root  != None:
        result = countNodes(root.left)
        result = result + 1
        result += countNodes(root.right)
    return result            

def PreOrder(root):                         #The function PreOrder visits the root, traverses the left subtree and traverses again the right subtree.
    if root != None:
        print((root.ID, root.fn, root.ln, root.gr))
        PreOrder(root.left)
        PreOrder(root.right)


def PostOrder(root):                        #The function PostOrder traverses the right root, traverses again the left root and lastly visits the root.
    if root != None:
        PostOrder(root.left)
        PostOrder(root.right)
        print((root.ID, root.fn, root.ln, root.gr))
        
        
def InOrder(root):                          #The function InOrder traverses the left subtree, visits the root and last but not least traverses again the right subtree
    if root != None:
        InOrder(root.left)
        print((root.ID, root.fn, root.ln, root.gr))
        InOrder(root.right)
            

     
def findByID(root,fID):                      #This function findById runs a search of the entered ID by the user and tries to return it if there is inside the tree.
    result = None
    
    if root != None:
        if fID < root.ID:
            result = findByID(root.left,fID)
        elif fID == root.ID:
            result = root
        else:
            result = findByID(root.right, fID)
    return result

def maxID(root):                                             #The function maxID corresponds with the maximum grade of all the students from the .csv file
    if root.right == None:
        result = root
    else:
        result = maxID(root.right)
    return result

def maxGrade(root):                                           #The function maxGrade calculates the maximum grade of all the students from the .csv file
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

print("---------- Menu ----------")                            #This is the GUI of the program in order to interact with the user and offer him the options that he would like to run.
print("1. Add in Order")
print("2. Show in Order")
print("3. Find Student by Grade")
print ("4. Show Last Student by Grade")  
print("5. Show Maximum Grade")
print ("0. Exit")  
ch = input("Choice: ").strip()                                 #Here the program asks from the user to enter a number in order to choose a specific option.

while ch != "0":                                               #While the choice is different from the 0 the program starts.
    if ch == "1":                                              #While the choice is matching with the 1 the program starts the time and adding in order the options from the .csv file
        starting = time.time()
        temp = Node()
        if root == None:
            root = temp
            x = 1
            y = 1
            z = 1
            m = 1
        else:
                addInOrder(root, temp)
                x = x + 1
                y = y + 1
                z = z + 1
                m = m + 1
        counter = counter + 1
        end = time.time()
        spnd_time = end - starting
         
    elif ch == "2":
        print ("Choose which way you wish to order the data from the .csv file.")
        print (" ---------- Menu ----------")
        print (" 1. Using the PreOrder method. ")
        print (" 2. Using the PostOrder method.")
        print (" 3. Using the InOrder method. ")
        ch = input("Choice: ").strip() 
        if ch == 1:
            PreOrder(root)
        elif ch == 2:
            PostOrder(root)
        else:
            print(("Number of Nodes: %d") % (countNodes(root)))
            
    elif ch == "3":
        userID = input("Give us Your ID:")
        starting = time.time()
        temp = findByID(root,userID)
        end = time.time()
        if temp == None:
            print ("User with the specific ID was not found. Please enter another one!")
        else:
            print(("%s %s %s %.2f %d") % (temp.ID, temp.fn, temp.ln, temp.gr))
            
    elif ch == "4":
        if root == None:
            print("Sorry, Nobody was found.")
        else:
            temp = maxID(root)
            print(("%s %s %s %.2f %d") % (temp.ID, temp.fn, temp.ln, temp.gr))
    elif ch == "5":
        if root == None:
            print("There is no Max Grade for the moment!")
        else:
            print(("Max Grade: %.2f") % (maxGrade(root)))
    else:
        print("Try again.")
    
       
#Graphical Illustration
    
plt.plot(counting_data, tm_spnd, color="red", marker="o", linestyle="solid")
plt.grid(axis='x')
plt.grid(axis='y')
plt.xticks(counting_data)
plt.title("Time and Count of Data")
plt.ylabel("Time")
plt.xlabel("Counting Data")
plt.show()
plt.close()
            
