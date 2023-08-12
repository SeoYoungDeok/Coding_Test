from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    combi = [[] for i in range(11)]
    for order in orders:
        for c in course:
            combi[c] += list(combinations(sorted(order), c))

    for c in course:
        counter = Counter(combi[c])
        counter = counter.most_common(len(counter))
        
        if counter:
            cnt = counter[0][1]
        else:
            break
            
        for k, v in counter:
            if cnt == v and v >= 2:
                answer.append("".join(k))
            else:
                break
        
    
    return sorted(answer)