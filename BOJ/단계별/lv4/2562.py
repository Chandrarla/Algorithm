arr = []
max = 0

for _ in range(9):
    n = int(input())
    arr.append(n)

for i in arr:
    if i > max:
        max = i

print(max)
print((arr.index(max))+1)