from sys import stdin as s

sequence1 = list(s.readline().strip())
sequence2 = list(s.readline().strip())
cache = [0] * len(sequence1)

for i in range(len(sequence2)):
    count = 0
    for j in range(len(sequence1)):
        if count < cache[j]:
            count = cache[j]
        elif sequence2[i] == sequence1[j]:
            cache[j] = count + 1

print(max(cache))
