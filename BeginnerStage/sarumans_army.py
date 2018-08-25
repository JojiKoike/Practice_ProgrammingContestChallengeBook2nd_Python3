N, R = map(int, input().split())
X = [int(input()) for i in range(N)]

j = 0
ans = 0
while j < N:
    print(j)
    s = X[j]
    j += 1
    while j < N and X[j] <= s + R:
        j += 1
    p = X[j - 1]
    while j < N and X[j] <= p + R:
        j += 1
    ans += 1

print(ans)
