import sys

input = sys.stdin.readline

N = int(input())
paper = list()

for _ in range(N):
    temp = list(map(int, input().split()))
    for i in range(len(temp)):
        if temp[i] == -1:
            temp[i] = 10
    paper.append(temp)

    
def division(array, n):
    global minus_one, zero, plus_one
    
    if n >= 0:        
        s = 0
        for row in array:
            s += sum(row)
        
        if s == n*n:
            plus_one += 1
            return
        elif s == 0:
            zero += 1
            return
        elif s == n*n*10:
            minus_one += 1
            return
        else:
            slice1 = list()
            slice2 = list()
            slice3 = list()
            slice4 = list()
            slice5 = list()
            slice6 = list()
            slice7 = list()
            slice8 = list()
            slice9 = list()

            for i in range(n):
                if i < n//3:
                    slice1.append(array[i][:n//3])
                    slice2.append(array[i][n//3:(n//3)*2])
                    slice3.append(array[i][(n//3)*2:])
                elif i < (n//3)*2:
                    slice4.append(array[i][:n//3])
                    slice5.append(array[i][n//3:(n//3)*2])
                    slice6.append(array[i][(n//3)*2:])
                else:
                    slice7.append(array[i][:n//3])
                    slice8.append(array[i][n//3:(n//3)*2])
                    slice9.append(array[i][(n//3)*2:])

            division(slice1, n//3)
            division(slice2, n//3)
            division(slice3, n//3)
            division(slice4, n//3)
            division(slice5, n//3)
            division(slice6, n//3)
            division(slice7, n//3)
            division(slice8, n//3)
            division(slice9, n//3)
    else:
        return
    
minus_one = 0
zero = 0
plus_one = 0
division(paper, N)

print(minus_one)
print(zero)
print(plus_one)