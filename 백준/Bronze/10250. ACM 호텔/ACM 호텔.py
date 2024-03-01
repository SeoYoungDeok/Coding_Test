import sys

T = int(sys.stdin.readline())

for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    
    if N == 1:
        print('101')
        continue
    
    floor = ((N-1) % H) + 1    
    host = ((N-1) // H) + 1
    if host < 10:
        host = '0' + str(host)
    
    print(str(floor) + str(host))