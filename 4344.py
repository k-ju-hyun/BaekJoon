import sys

C = int(sys.stdin.readline().strip())

for i in range(C):
    score = list(map(int, sys.stdin.readline().split()))
    avg = sum(score[1:]) / score[0]

    cnt = 0
    for j in score[1:]:
        if j > avg:
            cnt += 1
        
    ratio = (cnt/score[0]) * 100
    print(f'{ratio:.3f}%')