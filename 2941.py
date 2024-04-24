alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
word = 0
S = input()

for i in alphabet:
    if i in S:
        cnt += S.count(i)
        S = S.replace(i, ".")
S = S.replace(".", "")

print(cnt + len(S)) 