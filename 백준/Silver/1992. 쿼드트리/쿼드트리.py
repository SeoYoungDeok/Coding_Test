import sys

input = sys.stdin.readline

N = int(input())

img = list()
for _ in range(N):
    tmp = input()
    tmp = ' '.join(tmp)
    img.append(list(map(int, tmp.split())))
    

def division(array, n):
    global answer
    
    if n >= 0:        
        s = 0
        
        for row in array:
            s += sum(row)
        
        if s == n*n:
            answer += '1'
            return
        elif s == 0:
            answer += '0'
            return
        else:
            slice1 = list()
            slice2 = list()
            slice3 = list()
            slice4 = list()

            for i in range(n):
                if i < n//2:
                    slice1.append(array[i][:n//2])
                    slice2.append(array[i][n//2:])
                else:
                    slice3.append(array[i][:n//2])
                    slice4.append(array[i][n//2:])
            answer += '('
            division(slice1, n//2)
            division(slice2, n//2)
            division(slice3, n//2)
            division(slice4, n//2)
            answer += ')'
    else:
        return
    
answer = ''
division(img, N)

print(answer)