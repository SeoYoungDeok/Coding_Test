def solution(n):
    temp = [[0] * i for i in range(1, n+1)]
    
    row, col, num = -1, 0, 0
    for i in range(n, 0, -3):
        for j in range(i):
            row += 1
            num += 1
            temp[row][col] = num
        for j in range(i-1):
            col += 1
            num += 1
            temp[row][col] = num
        for j in range(i-2):
            row -= 1
            col -= 1
            num += 1
            temp[row][col] = num
    
    answer = []
    for line in temp:
        answer += line
    
    return answer