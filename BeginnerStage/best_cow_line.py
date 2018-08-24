N = int(input())
S = input()
result = ""

# Start index for Advance and Backward
a, b = 0, N-1

# Main Logic
while a <= b:
    left = False
    # Tie Break
    for i in range(b - a + 1):
        if S[a + i] < S[b - i]:
            left = True
            break
        elif S[a + i] > S[b - i]:
            left = False
            break
    if left:
        result += S[a]
        a += 1
    else:
        result += S[b]
        b -= 1

print(result)
