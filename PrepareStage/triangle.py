input()
input_lengths = input().split()
lengths = [int(input_lengths[i]) for i in range(len(input_lengths))]
result = 0
for i in range(len(lengths)):
    for j in range(i + 1, len(lengths)):
        for k in range(j + 1, len(lengths)):
            circumstance_length = lengths[i] + lengths[j] + lengths[k]
            max_length = max(lengths[i], max(lengths[j], lengths[k]))
            lest = circumstance_length - max_length
            if lest > max_length:
                result = circumstance_length
print(result)