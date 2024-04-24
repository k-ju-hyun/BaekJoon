import sys

A, B, C = map(int, sys.stdin.readline().split())

if A == B == C :
    money = 10000 + A * 1000
elif (A == B) or (A == C) :
    money = 1000 + A * 100
elif (B == C) :
    money = 1000 + B * 100
else:
    maxnum = max(A, B, C)
    money = maxnum * 100
print(money)