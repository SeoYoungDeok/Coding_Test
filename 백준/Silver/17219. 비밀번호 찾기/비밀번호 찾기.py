import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

pass_dict = dict()

for i in range(N):
    email, pw = sys.stdin.readline().rstrip().split()
    pass_dict[email] = pw
    
for j in range(M):
    print(pass_dict[sys.stdin.readline().rstrip()])