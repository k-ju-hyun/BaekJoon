import sys

T = int(sys.stdin.readline())

for i in range(T) :
    A, B = map(int, sys.stdin.readline().strip().split())
    print(A + B)