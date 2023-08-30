import collections

def solution(clothes):
    clothe_dict = collections.defaultdict(list)
    for v, k in clothes:
        clothe_dict[k].append(v)
    
    answer = 1
    for k in clothe_dict.keys():
        answer *= len(clothe_dict[k]) + 1
    answer -= 1
    
    return answer