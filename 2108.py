import sys
from collections import Counter

N = int(sys.stdin.readline().strip())
num = []
sum = 0

for i in range(N):
    num.append(int(sys.stdin.readline().strip()))
    sum += num[i]

# print(round(sum/N))

num.sort()
# print(num[N//2])

# cnt = []
# num_list = list(set(num))
# num_list.sort()

# for i in num_list:
#     cnt.append(num.count(i))

# if len(cnt) > 1:
#     if cnt.count(max(cnt)) >= 2:
#         idx = cnt.index(max(cnt)) + 1
#         print(num_list[idx])
#     else:
#         idx = cnt.index(max(cnt))
#         print(num_list[idx])
# else:
#     print(num[0])

count = 1


# print(abs(num[N-1] - num[0]))