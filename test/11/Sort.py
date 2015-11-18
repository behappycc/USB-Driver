alist = [54,26,93,17,77,31,44,55,21]
def bubbleSort(blist):
    for i in range(len(alist)-1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
              alist[j], alist[j+1] = alist[j+1], alist[j]

bubbleSort(alist)
print alist

def selectionSort(alist):
   for i in range(len(alist)-1,0,-1):
       positionOfMax=0
       for j in range(1,i+1):
           if alist[j]>alist[positionOfMax]:
               positionOfMax = j

       alist[i], alist[positionOfMax] = alist[positionOfMax], alist[i]

alist = [59,26,93,17,77,31,44,55,2,99]
selectionSort(alist)
print alist


def quickSort(alist, first, last):
    if first < last:
        splitpoint = partition(alist,first,last)

        quickSort(alist,first,splitpoint-1)
        quickSort(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark

alist = [54,26,93,17,77,31,44,55,21, 23]
quickSort(alist, 0, len(alist)-1)
print alist

'''
def qsort(array=[12,4,5,6,7,3,1,15,15]):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return qsort(less)+equal+qsort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

#print qsort()
'''