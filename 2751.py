import sys
n = int(sys.stdin.readline().strip())
m = []

for i in range(n):
    m.append(int(sys.stdin.readline().strip()))

m = sorted(m)
print(*m, sep = '\n')