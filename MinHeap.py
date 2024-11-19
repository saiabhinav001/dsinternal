def min_heapify(A, k):
    # Get indices of left and right children
    l = left(k)
    r = right(k)

    # Find smallest among root, left child and right child
    if l < len(A) and A[l] < A[k]:
        smallest = l
    else:
        smallest = k

    if r < len(A) and A[r] < A[smallest]:
        smallest = r

    # If root is not smallest, swap with smallest and continue heapifying
    if smallest != k:
        A[k], A[smallest] = A[smallest], A[k]
        min_heapify(A, smallest)

def left(k):
    # Return left child index
    return 2 * k + 1

def right(k):
    # Return right child index
    return 2 * k + 2

def build_min_heap(A):
    # Find index of last non-leaf node
    n = int((len(A) // 2) - 1)

    # Build min heap by calling min_heapify on all non-leaf nodes
    for k in range(n, -1, -1):
        min_heapify(A, k)

A = [3, 9, 2, 1, 4, 5]
print("Original array:", A)
build_min_heap(A)
print("Min heap:", A)
