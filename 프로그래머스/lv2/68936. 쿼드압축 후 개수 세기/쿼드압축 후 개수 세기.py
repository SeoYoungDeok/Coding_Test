def go(arr, n, answer):
    s = 0
    for row in arr:
        s += sum(row)
        
    if s == n*n:
        answer.append(1)
        return
    elif s == 0:
        answer.append(0)
        return
    
    slice1 = list()
    slice2 = list()
    slice3 = list()
    slice4 = list()

    for i in range(n):
        if i < n//2:
            slice1.append(arr[i][:n//2])
            slice2.append(arr[i][n//2:])
        else:
            slice3.append(arr[i][:n//2])
            slice4.append(arr[i][n//2:])
    
    go(slice1, len(slice1), answer)
    go(slice2, len(slice2), answer)
    go(slice3, len(slice3), answer)
    go(slice4, len(slice4), answer)

def solution(arr):
    answer = []
    go(arr, len(arr), answer)
    
    
    return [(len(answer)-sum(answer)), sum(answer)]