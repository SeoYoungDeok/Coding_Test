from sys import stdin as s
from collections import deque

N = s.readline().rstrip()
line = deque(map(int, s.readline().rstrip().split()))
sub_line = deque([])

order = 1

while line or sub_line:
    if line and line[0] == order:
        line.popleft()
        order += 1
    elif sub_line and sub_line[-1] == order:
        sub_line.pop()
        order += 1
    elif line:
        sub_line.append(line.popleft())
    else:
        print("Sad")
        break
else:
    print("Nice")