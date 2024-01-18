def rotate(array, query):
    
    temp = 999999
    minimum = 999999
    
    for c in range(query[1] - 1, query[3]):
        array[query[0] - 1][c], temp = temp, array[query[0] - 1][c]
        if minimum > temp:
            minimum = temp
    
    for r in range(query[0], query[2]):
        array[r][query[3] - 1], temp = temp, array[r][query[3] - 1]
        if minimum > temp:
            minimum = temp
    
    for c in range(query[3] - 2, query[1] - 2, -1):
        array[query[2] - 1][c], temp = temp, array[query[2] - 1][c]
        if minimum > temp:
            minimum = temp
    
    for r in range(query[2] - 2, query[0] - 2, -1):
        array[r][query[1] - 1], temp = temp, array[r][query[1] - 1]
        if minimum > temp:
            minimum = temp
    
    return minimum

def solution(rows, columns, queries):
    answer = []
    
    array = [[(row * columns) + col + 1 for col in range(columns)] for row in range(rows)]

    for query in queries:
        answer.append(rotate(array, query))
        
    return answer