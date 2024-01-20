import math
from itertools import permutations

def solution(n, k):
    answer = []
    n_list = list(range(1, n+1))
    
    fact = [0] * (n+1)
    fact[0] = 1
    for i in range(1, n+1):
        fact[i] = fact[i-1] * i
    
    while n > 0:
        div, mod = divmod(k, fact[n-1])
        
        if mod == 0:
            answer.append(n_list.pop(div-1))
            n_list = sorted(n_list, reverse=True)
            answer += n_list
            break
        elif mod == 1:
            answer.append(n_list.pop(div))
            answer += n_list
            break
        else:
            n -= 1
            k = mod
            answer.append(n_list.pop(div))
            
    return answer
