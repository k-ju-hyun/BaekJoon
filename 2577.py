import sys

A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())

mul = str(A * B * C) #문자열로 저장

for i in range(10) :
    print(mul.count(str(i)))
