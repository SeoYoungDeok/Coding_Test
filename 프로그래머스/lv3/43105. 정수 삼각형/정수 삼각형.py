def solution(triangle):
    
    for i in range(1, len(triangle)+1):
        for j , (left_num, right_num) in enumerate(zip(triangle[-i][0:-1], triangle[-i][1:])):
            triangle[-i-1][j] = max(triangle[-i-1][j] + left_num, triangle[-i-1][j] + right_num)
            
    return triangle[0][0]