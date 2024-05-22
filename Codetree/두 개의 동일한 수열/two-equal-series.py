n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sorted_A, sorted_B = sorted(A), sorted(B)
if sorted_A == sorted_B:
    print("Yes")
else: print("No")