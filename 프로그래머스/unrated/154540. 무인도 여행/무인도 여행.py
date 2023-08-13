import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)

def go(maps, row, col):
    if maps[row][col] != "X":
        s = int(maps[row][col])
        maps[row][col] = "X"
    else:
        return 0
    
    if row+1 < len(maps) and maps[row+1][col] != "X":
        s += int(go(maps, row+1, col))
    if row-1 >= 0 and maps[row-1][col] != "X":
        s += int(go(maps, row-1, col))
    if col+1 < len(maps[0]) and maps[row][col+1] != "X":
        s += int(go(maps, row, col+1))
    if col-1 >= 0 and maps[row][col-1] != "X":
        s += int(go(maps, row, col-1))
    
    return s

def solution(maps):
    answer = []
    maps = [list(map(str, line)) for line in maps]
    
    for row in range(len(maps)):
        for col in range(len(maps[0])):
            if maps[row][col] != "X":
                answer.append(go(maps, row, col))

    if answer:
        return sorted(answer)
    else:
        return [-1]