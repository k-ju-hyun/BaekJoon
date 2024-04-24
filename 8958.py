from re import L
import sys

ox = []

N = int(sys.stdin.readline().strip())

for i in range(N) :
    ox = list(map(str, sys.stdin.readline().strip()))
    sum = 0
    cnt = 0
    for i in range(len(ox)) :
        if ox[i] == 'O':
            cnt += 1
            sum += cnt
        else :
            cnt = 0
    print(sum)