from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    
    cnt = defaultdict(int)
    
    for i in tangerine:
        cnt[i] += 1
    
    cnt = sorted(cnt.items(), key = lambda x:x[1], reverse=True)
    
    for i, c in cnt:
        if k > 0:
            answer += 1
            k -= c
        else:
            break
    
    return answer