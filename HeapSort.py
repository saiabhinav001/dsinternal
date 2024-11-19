def heapify(A, n, k):
    max = k
    l = 2 * k + 1
    r = 2 * k + 2
    if l < n and A[k] < A[l]:
        max = l
    if r < n and A[max] < A[r]:
        max = r
    # if root is not max,swap with max and continue heapify
    if max != k:
        A[k], A[max] = A[max], A[k]
        heapify(A, n, max)


def heapsort(A):
    n = len(A)

    # build max heap
    for k in range((n // 2) - 1, -1, -1):
        heapify(A, n, k)
    for k in range(n - 1, 0, -1):
        # swap
        A[k], A[0] = A[0], A[k]
        # Heapify root element
        heapify(A, k, 0)


A = [12, 1, 9, 6, 7, 10, 4]
heapsort(A)
n = len(A)
print("Sorted array is")
for k in range(n):
    print("%d" % A[k], end=" ")
