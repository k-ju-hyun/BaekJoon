import sys

N = int(sys.stdin.readline().strip())

arr = []

for i in str(N):
    arr.append(int(i))

arr.sort(reverse=True)
for i in arr:
    print(i, end = '')