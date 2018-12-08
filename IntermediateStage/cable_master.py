
N = int(input())
K = int(input())
ls = map(float, input().split())
L = []
for l in ls:
    L.append(l)


def judge(x: float) -> bool:
    num = 0
    for li in L:
        num += int(li / x)
    return num >= K


INF = 1.0e10
ESP = 1.0e-10
ub = INF
lb = 0.0
while ub - lb > ESP:
    mid = (ub + lb) / 2.0
    if judge(mid):
        lb = mid
    else:
        ub = mid

print("{:.2f}".format(ub))

