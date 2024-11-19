def max_heapify(A, k):
    l = left(k)
    r = right(k)

    if l < len(A) and A[l] > A[k]:
        largest = l
    else:
        largest = k

    if r < len(A) and A[r] > A[largest]:
        largest = r

    # If largest is not root
    if largest != k:
        # Swap root with largest
        A[k], A[largest] = A[largest], A[k]
        # Recursively heapify the affected subtree
        max_heapify(A, largest)


def left(k):
    # Return left child index
    return 2 * k + 1


def right(k):
    # Return right child index
    return 2 * k + 2


def build_max_heap(A):
    # Find index of last non-leaf node
    n = int(len(A) // 2) - 1

    # Build max heap by calling max_heapify on all non-leaf nodes
    for k in range(n, -1, -1):
        max_heapify(A, k)


# Test the implementation
A = [3, 9, 2, 1, 4, 5]
print("Original array:", A)
build_max_heap(A)
print("Max heap:", A)
