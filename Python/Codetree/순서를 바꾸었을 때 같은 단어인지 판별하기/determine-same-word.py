A = list(input())
B = list(input())

A.sort()
B.sort()
sorted_A = "".join(A)
sorted_B = "".join(B)

if sorted_A == sorted_B:
    print("Yes")
else: print("No")