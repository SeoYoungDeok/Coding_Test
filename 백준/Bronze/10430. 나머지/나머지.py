import sys

input = sys.stdin.readline

A, B, C = map(int, input().rstrip().split())

a = (A+B)%C
b = (A*B)%C

print(a)
print(a)
print(b)
print(b)