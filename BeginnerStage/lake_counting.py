import random
import sys

n = int(input())
m = int(input())


# Generate Field Data
field = [['W' if random.randint(0, 1) == 1 else '.' for j in range(m)] for i in range(n)]
print(field)


# Depth First Search
def dfs(x: int, y: int):
    field[x][y] = '.'

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 'W':
                dfs(nx, ny)


# Count Lakes
if __name__ == "__main__":
    res = 0
    # 一時的に最大再帰深度を拡張する
    rec_limit_default = sys.getrecursionlimit()
    sys.setrecursionlimit(rec_limit_default * 10)
    for i in range(n):
        for j in range(m):
            if field[i][j] == 'W':
                dfs(i, j)
                res += 1
    # 最大再帰深度を元に戻す
    sys.setrecursionlimit(rec_limit_default)

    print("Lake Count is {0}".format(res))
