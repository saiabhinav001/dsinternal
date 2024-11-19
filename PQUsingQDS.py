# Priority Queue using Queue Data Structure

import queue
q=queue.PriorityQueue()
q.put(2)
q.put(4)
q.put(1)
q.put(0)
q.put(2)
q.put(6)
q.put(9)
for i in range(q.qsize()):
    print(q.get(i), end=" ")
