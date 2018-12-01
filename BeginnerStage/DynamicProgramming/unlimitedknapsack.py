n, W = map(int, input().split())
items = [map(int, input().split()) for i in range(n)]
weights = []
values = []
for item in items:
    w, v = item
    weights.append(w)
    values.append(v)

dp = [[0 for j in range(W + 1)] for i in range(n + 1)]


for i in range(n):
    for j in range(W + 1):
        if weights[i] > j:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i+1][j-weights[i]] + values[i])

print("Result : {0}".format(dp[n][W]))