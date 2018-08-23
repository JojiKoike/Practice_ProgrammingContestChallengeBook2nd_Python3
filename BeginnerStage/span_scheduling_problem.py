# Inputs

# Number of works
n = int(input())

# Start Time
s = [int(input()) for i in range(n)]


# Stop Time
t = [int(input()) for j in range(n)]


# Work Dictionary
works = {}
for k in range(n):
    works[t[k]] = s[k]
sorted_works = sorted(works.items())
print(sorted_works)

# Solve
ans = 0
current_time = 0
for work in sorted_works:
    termination, start = work
    print("start: {0}, termination: {1}, current_time: {2}".format(start, termination, current_time))
    if current_time < start:
        print(current_time)
        ans += 1
        current_time = termination

# Show Results
print("{0} {1}".format(ans, current_time))
