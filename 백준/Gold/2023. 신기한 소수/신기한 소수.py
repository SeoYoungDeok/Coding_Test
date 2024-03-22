import sys
import math

N = int(sys.stdin.readline())
answer = [2,3,5,7] # 한자릿수 소수

for i in range(N-1): # 두자릿수 부터
    temp = list()
    for num in answer: 
        for j in range(1,10):
            target = num * 10 + j #이전 소수를 받아와서 한자릿수 늘림
            count = 0
            for k in range(1, round((math.sqrt(target))) + 1): # 소수판별
                if target % k == 0:
                    count += 1
            if count <= 1: # 소수이면 temp list에 추가
                temp.append(target)
    answer = temp
    temp = list()

for num in answer:
    print(num)