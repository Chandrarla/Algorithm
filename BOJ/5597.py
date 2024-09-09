arr = []

for _ in range(30):
    arr.append(0)

for _ in range(28):
    sbmt = int(input())
    arr[sbmt - 1] = 1

for i in range(30):
    if arr[i] == 0:
        print(i+1)

