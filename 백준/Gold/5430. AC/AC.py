import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for i in range(T):
    p = input().rstrip()
    n = int(input())
    
    cnt = 0
    for c in p:
        if c == 'D':
            cnt += 1
    
    if cnt == n:
        print("[]")
        _ = input().rstrip()
    elif cnt > n:
        print("error")
        _ = input().rstrip()
    else:
        array = input().rstrip()
        array = deque(map(int, array[1:-1].split(',')))
        
        r_cnt = 0
        for c in p:
            if c == 'R':
                r_cnt += 1
            elif c == 'D':
                if r_cnt % 2 == 0:
                    array.popleft()
                else:
                    array.pop()
        
        if r_cnt % 2 != 0:
            array.reverse()
        
        answer = "["
        for j in array:
            answer += str(j) + ","

        answer = answer[:-1] + "]"

        print(answer)