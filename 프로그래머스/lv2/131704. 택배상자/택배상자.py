from collections import deque

def solution(order):
    answer = 0
    storage = deque([])
    
    for i in range(1, len(order)+1):
        storage.append(i)
        while storage and storage[-1] == order[answer]:
            answer += 1
            storage.pop()
            
    return answer