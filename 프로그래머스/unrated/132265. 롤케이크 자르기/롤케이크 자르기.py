def solution(topping):
    temp = [0] * len(topping)
    ascent = []
    descent = []
    
    i = 0
    for n in topping:
        if temp[n-1]:
            ascent.append(i)
        else:
            i += 1
            temp[n-1] = 1
            ascent.append(i)
            
    temp = [0] * len(topping)
    i = 0
    for n in topping[::-1]:
        if temp[n-1]:
            descent.append(i)
        else:
            i += 1
            temp[n-1] = 1
            descent.append(i)
    descent.reverse()
    
    answer = 0
    for i, j in zip(ascent[:-2], descent[1:]):
        if i == j:
            answer += 1
            
    return answer