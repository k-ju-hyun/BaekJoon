import sys

score = []
sum = 0

N = int(sys.stdin.readline().strip())
score = list(map(int, sys.stdin.readline().strip().split()))

M = max(score)

for i in range(N):
    sum += score[i] / M * 100
    avg = sum / N
print(avg)
