import sys

N = int(sys.stdin.readline().strip())
X = list(map(int, sys.stdin.readline().split()))
max = X[0]
min = X[0]

for i in range(1, N):
    if X[i] < min:
        min = X[i]
    elif X[i] > max:
        max = X[i]

print(min, max, end = ' ')
