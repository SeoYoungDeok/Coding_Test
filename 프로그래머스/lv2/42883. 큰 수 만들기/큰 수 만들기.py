from collections import deque

def solution(number, k):
    answer = deque(list())
    
    for n in number:
        while answer and answer[-1] < n and k > 0:
            answer.pop()
            k -= 1
        answer.append(n)

    if k != 0:
        return "".join(answer)[:-k]
    else:
        return "".join(answer)