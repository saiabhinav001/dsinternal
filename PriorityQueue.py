# Function to heapify the tree
def heapify(arr, n, i):
    # Find the largest among root, left child and right child
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Swap and continue heapify if root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Function to insert an element into the tree
def insert(array, newNum):
    n = len(array)
    if n == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((n // 2) - 1, -1, -1):
            heapify(array, n, i)


# Function to delete an element from the tree
def deleteNode(array, num):
    n = len(array)
    i = 0
    for i in range(0, n):
        if num == array[i]:
            break

    array[i], array[n - 1] = array[n - 1], array[i]

    array.remove(n - 1)

    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)


arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print ("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))


