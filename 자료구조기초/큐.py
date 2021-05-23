from collections import deque

#큐사용을 위해 collections에서 deque를 import를 해야함

queue = deque([12])

queue.append(7)
queue.append(5)
queue.append(3)
queue.append(1)

queue.popleft()

queue.append(4)
queue.append(8)

queue.popleft()
queue.popleft()

print(queue)
