import sys
N = int(sys.stdin.readline().strip())
num = [0] * 10001

for i in range(N):
    num[int(sys.stdin.readline().strip())] += 1

for i in range(len(num)):
    for j in range(num[i]):
        print(i)
