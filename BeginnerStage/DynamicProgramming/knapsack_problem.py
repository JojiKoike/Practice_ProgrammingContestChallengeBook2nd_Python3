n, W = map(int, input().split())
weight_value = [input().split() for i in range(n)]


def rec(i: int, j: int) -> int:
    res = 0
    if i == n:
        res = 0
    elif j < int(weight_value[i][0]):
        res = rec(i + 1, j)
    else:
        res = rec(i + 1, j) if rec(i + 1, j) > rec(i + 1, j - int(weight_value[i][0])) + int(weight_value[i][1]) \
            else rec(i + 1, j - int(weight_value[i][0])) + int(weight_value[i][1])
    return res


print("{0}".format(rec(0, W)))
