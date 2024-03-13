import sys

N, M = map(int, input().split())
card_list = list(map(int, input().split()))

answer = 0
for i in range(len(card_list)-2):
    for j in range(i+1, len(card_list)-1):
        for k in range(j+1, len(card_list)):
            temp = card_list[i] + card_list[j] + card_list[k]
            if answer < temp and temp <= M:
                answer = temp
print(answer)