import os
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

def dfs(k):
    Mark[k] = 1
    print("Now in %d" % (k+1))
    for j in range(N):
        if a[k][j] == 1 and Mark[j] == 0:
            dfs(j)

    return

p = input("Give start node (1-%d) or out of range to exit: " % (N))
i = int(p)
while i >= 1 and i <= N:
    for m in range(N):
        Mark[m] = 0
    dfs(i-1)
    p = input("Give start node (1-%d) or out of range to exit: " % (N))
    i = int(p)
