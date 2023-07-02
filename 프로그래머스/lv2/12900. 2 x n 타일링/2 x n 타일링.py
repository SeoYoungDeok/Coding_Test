def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    answer = [0] * n
    answer[0] = 1
    answer[1] = 2
    
    for i in range(2, n):
        answer[i] = (answer[i-1] + answer[i-2]) % 1_000_000_007
        
    return answer[n-1]