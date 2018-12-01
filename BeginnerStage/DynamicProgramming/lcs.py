# Get Input Values
n, m = map(int, input().split())
s, t = input().split()

# Initialize DP table
dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

# Solve
for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

# Show Result
print("Result : {0}".format(dp[n][m]))