n = int(input())                        # Number of cards
m = int(input())                        # Sum
k = [int(input()) for i in range(n)]    # Cards

# Judgement O(n) = n^4
judge_result = False
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                if m == k[a] + k[b] + k[c] + k[d]:
                    judge_result = True

# Print Result
print("Yes" if judge_result else "No")
