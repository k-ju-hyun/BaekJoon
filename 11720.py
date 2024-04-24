N = int(input())

sum = 0

num = list(map(int, input()))

for i in range(N):
    sum += num[i]
print(sum)