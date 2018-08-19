n = int(input())
stack = []

# Stacking
for i in range(n):
    stack.append(i)
    print(stack)

# Pop
for i in range(n):
    stack.pop()
    print(stack)