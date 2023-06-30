from collections import deque

def solution(prices):
    
    answer = [0] * len(prices)
    queue = deque([])
    
    for i, price in enumerate(prices):
        while queue and price < prices[queue[-1]]:
            j = queue.pop()
            answer[j] = i - j
        queue.append(i)
    
    while len(queue) != 0:
        pop = queue.pop()
        answer[pop] = (len(prices) - 1) - pop
        
    return answer