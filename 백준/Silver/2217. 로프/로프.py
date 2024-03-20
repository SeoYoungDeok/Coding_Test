n = int(input())

ropes = []

for _ in range(n):
    ropes.append(int(input()))

ropes.sort()

max_weight = 0
for i, rope in enumerate(ropes):
    weight = rope * (n - i)
    if weight > max_weight:
        max_weight = weight

print(max_weight)