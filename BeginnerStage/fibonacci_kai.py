n = int(input())
memo = [i * 0 for i in range(n + 1)]


def fib(k):
    if k <= 1:
        return k
    elif memo[k] != 0:
        return memo[k]
    else:
        memo[k] = fib(k - 1) + fib(k - 2)
        return memo[k]


print(fib(n))
