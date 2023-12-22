from collections import deque

def solution(numbers):
    answer = [0] * len(numbers)
    queue = deque([])
    
    for i, n in enumerate(numbers):
        while queue and n > numbers[queue[-1]]:
            j = queue.pop()
            answer[j] = n
        queue.append(i)
    
    while len(queue) != 0:
        pop = queue.pop()
        answer[pop] = -1
    
    return answer


