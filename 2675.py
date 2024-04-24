T = int(input())

for i in range(T):
    R, S = map(str, input().split())
    w = ''
    for j in range(len(S)):
        w += int(R) * S[j]
    print(w)