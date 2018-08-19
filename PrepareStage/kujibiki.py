n = int(input())                        # Number of cards
m = int(input())                        # Sum
k = [int(input()) for i in range(n)]    # Cards

# Judgement
judge_result = False
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                if m == k[a] + k[b] + k[c] + k[d]:
                    judge_result = True

# Print Result
print("Yes" if judge_result else "No")
