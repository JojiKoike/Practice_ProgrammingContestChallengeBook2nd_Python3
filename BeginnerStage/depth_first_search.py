n = int(input())
k = int(input())
a = [int(input()) for i in range(n)]


def dfs(i, summation):
    if i == n:
        return summation == k

    if dfs(i + 1, summation):
        return True

    if dfs(i + 1, summation + a[i]):
        return True

    return False


print("Yes" if dfs(0, 0) else "No")
