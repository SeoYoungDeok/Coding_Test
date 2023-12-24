from collections import defaultdict

def solution(name, yearning, photo):
    
    yearning_score = defaultdict(int)
    
    for k, v in zip(name, yearning):
        yearning_score[k] = v
    
    answer = []
    for p in photo:
        answer.append(sum([yearning_score[k] for k in p]))
    
    return answer