def solution(numbers):
    answer = []
    
    for n in numbers:
        if n % 2 == 0:
            answer.append(n+1)
        else:
            right_zero = (~n & (n+1))
            answer.append((n + right_zero) - (right_zero // 2))
        
    return answer