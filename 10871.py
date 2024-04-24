import sys

N, X = map(int, sys.stdin.readline().strip().split())
A = []
A = list(map(int, sys.stdin.readline().split()))

for i in range(N) :
    if A[i] < X:
        result = A[i]
        print(result, end = ' ')