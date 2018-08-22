# Get Input Values
values = [int(input()) for i in range(6)]
A = int(input())

# Define Constant
V = [1, 5, 10, 50, 100, 500]

ans = 0
for i in range(5, -1, -1):
    t = int(min(A/V[i], values[i]))
    A -= t * V[i]
    ans += t

print("{0}".format(ans))
