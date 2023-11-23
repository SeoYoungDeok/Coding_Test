import sys
from collections import deque

input = sys.stdin.readline

while True:
    S = input().rstrip()
    
    if S == '.':
        break
        
    flag = 0
    queue = deque()
    
    for c in S:
        if c == '(' or c == '[':
            queue.append(c)
            
        if queue and c == ')':
            pop = queue.pop()
            if pop != '(':
                flag = 1
                break
        elif queue and c == ']':
            pop = queue.pop()
            if pop != '[':
                flag = 1
                break
        elif not queue and c == ']' or c == ')':
            flag = 1
            break
    
    if len(queue) >= 1:
        flag = 1
    
    if flag:
        print("no")
    else:
        print("yes")