n, W = map(int, input().split())
weight_value = [input().split() for i in range(n)]
dp = [[-1 for k in range(10000 + 1)] for j in range(100 + 1)]

for i in range(n - 1, -1, -1):
    for j in range(0, W + 1):
        if j < int(weight_value[i][0]):
            dp[i][j] = dp[i + 1][j]
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - int(weight_value[i][0])] + int(weight_value[i][1]))
        print(dp[i][j])

print(dp[0][W])