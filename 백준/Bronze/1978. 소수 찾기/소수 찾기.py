import sys
import math

input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
answer = 0
for i in N_list:
    if i <= 1:
        pass
    else:
        target = int(math.sqrt(i)) + 1
        cnt = 0
        for j in range(2, target):
            if i % j == 0:
                cnt += 1
        if cnt == 0:
            answer += 1

print(answer)