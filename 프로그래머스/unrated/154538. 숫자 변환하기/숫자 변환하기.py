def solution(x, y, n):
    answer = [999] * (1_000_000 + 1)
    answer[x] = 0
    for i in range(x, y):
        if answer[y] != 999:
            break
            
        for num in [i+n, i*2, i*3]:
            if num > 1_000_000:
                continue
            answer[num] = min(answer[num], answer[i]+1)
    
    return -1 if answer[y] == 999 else answer[y]