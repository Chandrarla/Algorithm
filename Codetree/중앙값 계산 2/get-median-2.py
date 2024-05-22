n = int(input())
arr = list(map(int, input().split()))

read = []

for i in range(len(arr)):
    read.append(arr[i])
    if (i+1)%2 == 1 :
        read.sort()
        print(read[i//2], end = " ")