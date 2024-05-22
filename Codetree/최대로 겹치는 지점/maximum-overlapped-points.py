n = int(input())
arr = [0] * 100
segments = [tuple(map(int, input().split()))
       for _ in range(n)]
for a, b in segments:
    for i in range(a, b):
        arr[i] += 1
max_index = max(arr)
cnt = 0
for elem in arr:
    if max_index == elem:
        cnt += 1
print(cnt)