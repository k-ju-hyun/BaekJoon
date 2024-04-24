A, B = map(str, input().split())
A_list = list(A)
A_list.reverse()
B_list = list(B)
B_list.reverse()

print(type(A_list[0]))
if A_list > B_list:
    print("".join(A_list))
else:
    print("".join(B_list))