def solution(n):
    answer = [1, 1]
    
    for i in range(n-1):
        answer.append(answer[i] + answer[i+1])
    
    return answer[-1] % 1234567