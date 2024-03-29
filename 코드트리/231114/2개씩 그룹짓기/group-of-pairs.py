n = int(input())
arr = list(map(int, input().split()))
arr.sort()

max = 0
for i in range(n):
    sum = arr[i] + arr[2*n-i-1]
    if sum > max: max = sum

print(max)