import sys
input = sys.stdin.readline

N, query = map(int, input().split())
array = list(map(int, input().split()))

cumsum = list()
sum = 0
for i in range(N):
    sum += array[i] 
    cumsum.append(sum)

for _ in range(query):
    left, right = map(int, input().split())
    
    if left != 1:
        print(cumsum[right-1] - cumsum[left-2])
    else:
        print(cumsum[right-1])