import sys

num = []

for i in range(9):
    x = int(sys.stdin.readline().strip())
    num.append(x)

print(max(num), num.index(max(num)) + 1, sep = '\n')