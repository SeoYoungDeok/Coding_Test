from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    s = 0
    while truck_weights:
        answer += 1
        s -= bridge.popleft()
        if s + truck_weights[0] <= weight:
            pop = truck_weights.popleft()
            s += pop
            bridge.append(pop)
        else:
            bridge.append(0)
    
    answer += bridge_length
    
    return answer