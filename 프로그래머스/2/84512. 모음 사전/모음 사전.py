from itertools import product

def solution(word):
    answer = list()
    
    for i in range(1, 6):
        answer.extend(list(product(['A', 'E', 'I', 'O', 'U'], repeat=i)))
        
    answer.sort()
    
    for i, w in enumerate(answer):
        if word == ''.join(w):
            return i + 1