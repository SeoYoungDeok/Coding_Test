import math

def dist(d1, d2):
    return math.sqrt(d1**2 + d2**2)

def solution(k, d):
    answer = 0
    
    x = d - (d % k)
    y = 0
    while x >= 0:
        if dist(x, y) <= d:
            answer += x // k + 1
            y += k
        else:
            x -= k
    
    return answer