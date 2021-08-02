#Linear search in python

def linearSearch(array, n, x):


    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


array = ['athish', 'siddharth', 'haarvish', 'dennis']
x = 'danny'
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)
