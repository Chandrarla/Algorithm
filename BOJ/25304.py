total = int(input())
num = int(input())
sum = 0

for _ in range(num):
    price, n = map(int, input().split())
    sum += price * n

if total == sum:
    print("Yes")
else:
    print("No")
