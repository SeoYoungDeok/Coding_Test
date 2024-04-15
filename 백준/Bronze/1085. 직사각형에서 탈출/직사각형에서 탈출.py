import sys

X, Y, W, H = map(int, sys.stdin.readline().split())

print(min(X, Y, W-X, H-Y))