Remainder = []

for i in range(10) :
    A = int(input())
    Remainder.append(A%42)
Remainder = set(Remainder)
print(len(Remainder))
