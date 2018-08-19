from collections import deque
n = int(input())
queue = deque([i for i in range(n)])
print(queue)
print(queue.append(n))
print(queue)
for i in range(n + 1):
    print(queue.popleft())
print(queue)