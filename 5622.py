word = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0
S = input()

for i in range(len(S)):
    for j in word:
        if S[i] in j:
            time += word.index(j) + 3
        else:
            continue

print(time)