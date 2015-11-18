def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
    return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print sequentialSearch(testlist, 3)
print sequentialSearch(testlist, 13)

def binarySearch(alist, item):
        first = 0
        last = len(alist)-1
        found = False
  
        while first<=last and not found:
            midpoint = (first + last)//2
            if alist[midpoint] == item:
                found = True
            else:
                if item < alist[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1

        return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print binarySearch(testlist, 4) 
print binarySearch(testlist, 19)

def binarySearchRecursive(alist, item):
        if len(alist) == 0:
            return False
        else:
            midpoint = (first + last)//2
            if alist[midpoint] == item:
                return True
            else:
                if item < alist[midpoint]:
                    return binarySearchRecursive(alist[:midpoint], item)
                else:
                    return binarySearchRecursive(alist[midpoint+1:], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print binarySearch(testlist, 1) 
print binarySearch(testlist, 33)
