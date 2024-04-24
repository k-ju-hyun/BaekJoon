N = int(input())
firstNum = N
sum = 0

while True:
    if (N % 10 + N // 10) < 10:
        N = (N % 10 + N // 10) + ((N % 10) * 10)
    else:
        N = (N % 10 + N // 10) % 10 + (( N % 10 ) * 10)
    sum += 1
    if firstNum == N:
        break
print(sum)