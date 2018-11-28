n, k = map(int, input().split())
ainputs = input().split()
a = []
for ainput in ainputs:
    a.append(int(ainput))

lb = -1
ub = n

while ub - lb > 1:
    mid = int((ub + lb) / 2)
    if a[mid] >= k:
        ub = mid
    else:
        lb = mid

print("Result : {0}".format(ub))
