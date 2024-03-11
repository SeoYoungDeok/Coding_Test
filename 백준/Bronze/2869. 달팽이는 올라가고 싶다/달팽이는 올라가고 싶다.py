import sys

input = sys.stdin.readline

A, B, V = map(int, input().split())

if ((V-B) / (A-B)).is_integer():
    print((V-B) // (A-B))
else:
    print(((V-B) // (A-B)) + 1)