def solution(n, k, cmd):
    answer = ["O"] * n
    
    k += 1
    up = [i for i in range(-1, n+1)]
    down = [i for i in range(1, n+3)]
    deleted = []
    
    for op in cmd:
        if op.startswith("C"):
            deleted.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            if down[k] > n :
                k = up[k]
            else:
                k = down[k]
        elif op.startswith("Z"):
            restore = deleted.pop()
            up[down[restore]] = restore
            down[up[restore]] = restore
        else:
            direction, num = op.split()
            if direction == "U":
                for i in range(int(num)):
                    k = up[k]
            else:
                for i in range(int(num)):
                    k = down[k]
                    
    for i in deleted:
        answer[i-1] = "X"
    
    return "".join(answer)