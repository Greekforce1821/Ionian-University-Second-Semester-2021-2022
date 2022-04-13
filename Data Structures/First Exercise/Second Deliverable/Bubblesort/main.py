from gettext import npgettext
import numpy


def bubbleSort(arr):
    n = len(arr)
 
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def generate_matrix(low, high, shape):
    x, y = shape
    values = npgettext.random.randint(low+1, high-1, size=(x, y-2))
    predefined = npgettext.tile([low, high], (x, 1))
    values = npgettext.hstack([values, predefined])
    for row in values:
        npgettext.random.shuffle(row)
    return values
 
bubbleSort(arr)
 
print ("Ο ταξινομημένος πίνακας είναι ως εξής:")
for i in range(len(arr)):
    print ("% d" % arr[i],end=" ")