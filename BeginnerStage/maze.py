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


# Generate Maze Data
maze = [['#' if random.randint(0, 1) == 1 else '.' for j in range(n)] for i in range(m)]
maze[sx][sy] = "S"
maze[gx][gy] = "G"


print(maze)