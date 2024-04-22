from sys import stdin as s

K = int(s.readline().rstrip())
building_list = list(map(int, s.readline().rstrip().split()))

answer = [0] * len(building_list)

def preorder(l, idx, n):
    
    if idx < l:
        n = preorder(l, idx*2+1, n)
        answer[idx] = n
        n += 1
        n = preorder(l, idx*2+2, n)
        
    return n

preorder(len(building_list), 0, 1)

num = 0
for i in range(K):
    for _ in range(2**i):
        print(building_list[answer[num]-1], end=" ")
        num += 1
    print()