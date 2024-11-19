import heapq
H=[21,3,45,23,78,6,5]
heapq.heapify(H)
print(H)
heapq.heappush(H,8)
print(H)
heapq.heappop(H)
print(H)
heapq.heapreplace(H,6)
print(H)
heapq.heappushpop(H,4)
print(H)
H.append(1)
print(H)