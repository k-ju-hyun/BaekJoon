import sys

while True:
    A, B = map(int, sys.stdin.readline().strip().split())
    if (A == 0) & (B == 0):
        break
    print(A + B)