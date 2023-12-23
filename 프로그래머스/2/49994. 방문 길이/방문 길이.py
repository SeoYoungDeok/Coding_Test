def solution(dirs):
    answer = set()
    
    x, y = 5, 5
    op = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)}
    
    for d in dirs:
        dx, dy = op[d]
        if not (0 <= x+dx and x+dx <=10 and 0<=y+dy and y+dy<=10):
            continue
        answer.add((x, y, x+dx, y+dy))
        answer.add((x+dx, y+dy, x, y))
        x += dx
        y += dy
        
    return len(answer) // 2