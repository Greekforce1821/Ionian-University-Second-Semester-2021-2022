import os
from array import array
a = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0],	
     [1, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
     [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
     [0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
     [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

Mark = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
N = len(a)
QSIZE = N*N
queue = array('i', QSIZE*[0])
front = -1
rear = -1

def enqueue(k):
    global front
    global rear
    f = 0

    if front == -1:
        front = 0
    if rear < QSIZE - 1:
        rear = rear + 1
        queue[rear] = k
        f = 1
    return f

def dequeue():
    global front
    global rear
    f = 0
    k = 0
    if front != -1:
        k = queue[front]
        front = front + 1
        f = 1
    if front > rear:
        rear = -1
        front = -1
    return k, f

def bfs(k):
    flag = 0
    i = 0
    flag = enqueue(k)
    Mark[k] = 1
    while flag == 1:
        i, flag = dequeue()
        if flag == 1:
            print("Now in %d" % (i+1))
            for j in range(N):
                if a[i][j] == 1 and Mark[j] == 0:
                    flag = enqueue(j)
                    Mark[j] = 1
    
p = input("Give start node (1-%d) or out of range to exit: " % (N))
i = int(p)
while i >= 1 and i <= N:
    for m in range(N):
        Mark[m] = 0
    bfs(i-1)
    p = input("Give start node (1-%d) or out of range to exit: " % (N))
    i = int(p)