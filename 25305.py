import sys

N, K = map(int, sys.stdin.readline().strip().split())
x = [] * N

x = list(map(int, sys.stdin.readline().strip().split()))

x.sort(reverse=True)
print(x[K-1])