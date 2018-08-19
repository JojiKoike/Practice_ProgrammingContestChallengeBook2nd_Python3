L = int(input())
n = int(input())
x = [int(input()) for i in range(n)]
# Min
minimum = 0
for i in range(n):
    minimum = max(minimum, min(x[i], L - x[i]))
print("Minimum: {0}".format(minimum))

# Max
maximum = 0
for i in range(n):
    maximum = max(maximum, max(x[i], L - x[i]))
print("Maximum: {0}".format(maximum))