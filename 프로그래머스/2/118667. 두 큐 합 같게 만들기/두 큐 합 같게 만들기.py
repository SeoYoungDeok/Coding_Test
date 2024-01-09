from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    
    if (sum_queue1 + sum_queue2) % 2 == 1:
        return -1
    
    count = 0
    limit = (len(queue1) + len(queue2)) * 2
    while True:
        if count > limit:
            return -1
        
        if sum_queue1 > sum_queue2:
            pop = queue1.popleft()
            sum_queue1 -= pop
            sum_queue2 += pop
            queue2.append(pop)
            count += 1
        elif sum_queue1 < sum_queue2:
            pop = queue2.popleft()
            sum_queue2 -= pop
            sum_queue1 += pop
            queue1.append(pop)
            count += 1
        elif sum_queue1 == sum_queue2:
            return count
