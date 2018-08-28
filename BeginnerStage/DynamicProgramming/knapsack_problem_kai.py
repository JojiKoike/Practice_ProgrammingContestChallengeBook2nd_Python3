n, W = map(int, input().split())
weight_value = [input().split() for i in range(n)]
dp = [[-1 for k in range(10000 + 1)] for j in range(100 + 1)]


def rec(i: int, j: int) -> int:
    if dp[i][j] >= 0:
        return dp[i][j]
    if i == n:
        res = 0
    elif j < int(weight_value[i][0]):
        res = rec(i+1, j)
    else:
        res = rec(i + 1, j) if rec(i + 1, j) > rec(i + 1, j - int(weight_value[i][0])) + int(weight_value[i][1]) \
            else rec(i + 1, j - int(weight_value[i][0])) + int(weight_value[i][1])
    dp[i][j] = res
    return res


print("{0}".format(rec(0, W)))
