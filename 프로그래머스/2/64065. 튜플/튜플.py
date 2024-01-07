from collections import defaultdict

def solution(s):
    s = list(map(int, s.replace('{', '').replace('}', '').split(',')))
    num_dict = defaultdict(int)
    for i in s:
        num_dict[i] += 1
    
    answer = list()
    for k, v in sorted(num_dict.items(), key = lambda x:-x[1]):
        answer.append(k)
    
    return answer