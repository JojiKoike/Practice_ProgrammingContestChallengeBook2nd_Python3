# Get Number of items and Limit Weight
n, W = map(int, input().split())

# Get Items info and build value and weight list
items = [map(int, input().split()) for i in range(n)]
values = []
weights = []
for item in items:
    v, w = item
    values.append(v)
    weights.append(w)

print(values)
print(weights)

# Initialize Dynamic Table
dp = [[0 for j in range(W + 1)] for i in range(n + 1)]

# Solve
for i in range(n - 1, -1, -1):
    for j in range(W + 1):
        if j < weights[i]:
            dp[i][j] = dp[i + 1][j]
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - weights[i]] + values[i])

# Show Result
print("Result : {0}".format(dp[0][W]))
