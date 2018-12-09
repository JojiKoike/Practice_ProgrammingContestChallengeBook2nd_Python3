# Get Inputs
n = int(input())
a_input = map(int, input().split())
m_input = map(int, input().split())
K = int(input())
a = []
m = []
for a_i in a_input:
    a.append(a_i)
for m_i in m_input:
    m.append(m_i)

# Initialize DP Table
dp = [-1 for i in range(K + 1)]
dp[0] = 0

# Solve
for i in range(n):
    for j in range(K + 1):
        if dp[j] >= 0:
            dp[j] = m[i]
        elif j < a[i] or dp[j - a[i]] <= 0:
            dp[j] = -1
        else:
            dp[j] = dp[j - a[i]] - 1

# Show Result
print("Yes" if dp[K] > 0 else "No")

