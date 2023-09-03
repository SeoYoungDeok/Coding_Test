def solution(s):
    temp = list()
    for c in s:
        temp.append(c)
        if len(temp) >= 2 and temp[-1] == temp[-2]:
            del temp[-2:]
    
    if len(temp) > 0:
        return 0
    else:
        return 1