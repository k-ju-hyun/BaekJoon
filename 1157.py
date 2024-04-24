W = input().upper()

word = list(set(W))
cntlist = []

for i in word:
    cnt = W.count(i)
    cntlist.append(cnt)

if cntlist.count(max(cntlist)) > 1:
    print("?")
else:
    print(word[cntlist.index(max(cntlist))])