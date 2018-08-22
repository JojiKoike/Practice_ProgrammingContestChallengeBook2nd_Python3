from collections import deque
import random

# Input
m, n = map(int, input().split())


# Define State Class
class Pair:
    def __init__(self, nx, ny):
        self.x = nx
        self.y = ny


# Constants Definition
INF = 100000000


# Variables
sx, sy = 0, 1
gx, gy = m - 1, n - 2
d = [[ INF for j in range(n)] for i in range(m)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# Generate Maze Data
maze = [['#' if random.randint(0, 1) == 1 else '.' for j in range(n)] for i in range(m)]
maze[sx][sy] = "S"
maze[gx][gy] = "G"
print(maze)


# Breadth-First Search
def bfs() -> int:
    queue = deque()
    queue.append(Pair(sx, sy))
    d[sx][sy] = 0

    # Loop until queue become empty
    while len(queue) > 0:
        pair = queue.popleft()
        if pair.x == gx and pair.y == gy:
            break
        for i in range(4):
            nx, ny = pair.x + dx[i], pair.y + dy[i]
            if 0 <= nx < m and 0 <= ny < m and maze[nx][ny] != '#' and d[nx][ny] == INF:
                queue.append(Pair(nx, ny))
                d[nx][ny] = d[pair.x][pair.y] + 1

    return d[gx][gy]


print("{0}".format(bfs()))

