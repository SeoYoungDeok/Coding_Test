from collections import deque

def check(answer, i, j, l):
    if answer[0] > i or answer[2] > l:
        answer[0] = i
        answer[1] = j
        answer[2] = l
    return answer

def solution(sequence, k):
    answer = [1_000_000, 1_000_000, 1_000_000]
    
    queue = deque([sequence[0]])
    
    s, i, j = sequence[0], 0, 0
    while True:
        if s == k:
                answer = check(answer, i, j, len(queue))
                
        if s < k and j < len(sequence)-1:
            j += 1
            s += sequence[j]
            queue.append(sequence[j])
        elif queue:
            s -= queue.popleft()
            i += 1
        else:
            break
                    
    return answer[:2]