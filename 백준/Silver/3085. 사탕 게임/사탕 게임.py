import sys

input = sys.stdin.readline

def check(arr, N):
    row_max = 0
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            temp = arr[i][j]
            if temp == arr[i][j+1]:
                cnt += 1
            else:
                if row_max < cnt:
                    row_max = cnt
                cnt = 1
            if row_max < cnt:
                row_max = cnt
    
    col_max = 0
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            temp = arr[j][i]
            if temp == arr[j+1][i]:
                cnt += 1
            else:
                if col_max < cnt:
                    col_max = cnt
                cnt = 1
            if row_max < cnt:
                row_max = cnt
    
    return max(row_max, col_max)

arr = []
N = int(input().rstrip())

for i in range(N):
    arr.append(list(input().rstrip()))

answer = []
for i in range(N):
    for j in range(N):
        if i-1 >= 0 and arr[i][j] != arr[i-1][j]:
            arr[i][j], arr[i-1][j] = arr[i-1][j], arr[i][j]
            answer.append(check(arr, N))
            arr[i][j], arr[i-1][j] = arr[i-1][j], arr[i][j]
            
        if i+1 <= N-1 and arr[i][j] != arr[i+1][j]:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            answer.append(check(arr, N))
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            
        if j-1 >= 0 and arr[i][j] != arr[i][j-1]:
            arr[i][j], arr[i][j-1] = arr[i][j-1], arr[i][j]
            answer.append(check(arr, N))
            arr[i][j], arr[i][j-1] = arr[i][j-1], arr[i][j]
            
        if j+1 <= N-1 and arr[i][j] != arr[i-1][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            answer.append(check(arr, N))
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        
print(max(answer))