from sys import stdin as s

input_string = s.readline().strip()

answer = [0, 0]
temp = input_string[0]
answer[int(temp)] += 1
for s in input_string[1:]:
    if temp == s:
        pass
    else:
        answer[int(s)] += 1
        temp = s

print(min(answer))