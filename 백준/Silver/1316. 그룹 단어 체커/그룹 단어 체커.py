from sys import stdin as s

N = int(s.readline().strip())

count = 0
for i in range(N):
    word = s.readline().strip()
    stack = [word[0]]

    for c in word[1:]:
        if stack[-1] != c:
            stack.append(c)
        else:
            continue

    if len(stack) == len(set(stack)):
        count += 1

print(count)
