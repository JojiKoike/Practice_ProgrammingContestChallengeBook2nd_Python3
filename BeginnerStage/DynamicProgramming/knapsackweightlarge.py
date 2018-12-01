n, W = map(int, input().split())
items = [map(int, input().split()) for i in range(n)]
weights = []
values = []
for item in items:
    w, v = item
    weights.append(w)
    values.append(v)

max_value = max(values)

# Calc DP Table
dp = [[100000000 for j in range(n * max_value + 1)] for i in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    for j in range(n * max_value + 1):
        if j < values[i]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = min(dp[i][j], dp[i][j - values[i]] + weights[i])

# Show Result
res = 0
for i in range(n * max_value + 1):
    if dp[n][i] <= W:
        res = i
print("Result : {0}".format(res))
