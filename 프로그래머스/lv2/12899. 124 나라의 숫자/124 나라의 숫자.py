def solution(n):
    mod = ["_", "1", "2", "4"]
    answer = ""
    
    while n > 0:
        m = n % 3
        if m == 0:
            answer += "4"
            n //= 3
            n -= 1
        else:
            answer += str(m)
            n //= 3
        
    
    return answer[::-1]
    
    
    
    