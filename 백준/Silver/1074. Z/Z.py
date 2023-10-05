n, r, c = map(int, input().split())
num = 0

def func(row, col):
    #print("------- func 시작 -------")
    
    global num
    global n
    
    #print("n : ", n)
    #print("r, c : {}, {}".format(row, col))
    if n <= 0:
        #print("return")
        return
    
    
    if row < 2**(n-1) and col < 2**(n-1): #왼쪽 위
        #print("왼쪽 위")
        num += 0
        n -= 1
        row = row % (2**n)
        col = col % (2**n)
        #print(num)
        func(row, col)
        
    elif row >= 2**(n-1) and col < 2**(n-1): #왼쪽 아래
        #print("왼쪽 아래")
        num += (4**(n-1)) * 2
        n -= 1
        row = row % (2**n)
        col = col % (2**n)
        #print(num)
        func(row, col)
    elif row < 2**(n-1) and col >= 2**(n-1): #오른쪽 위
        #print("오른쪽 위")
        num += 4**(n-1)
        n -= 1
        row = row % (2**n)
        col = col % (2**n)
        #print(num)
        func(row, col)
    elif row >= 2**(n-1) and col >= 2**(n-1): #오른쪽 아래
        #print("오른쪽 아래")
        num += (4**(n-1)) * 3
        n -= 1
        row = row % (2**n)
        col = col % (2**n)
        #print(num)
        func(row, col)
        
    #print("------- func 종료 -------")

func(r, c)
print(num)