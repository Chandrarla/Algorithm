n = int(input())
offset = 100
arr = [0] * 200
segments = [tuple(map(int, input().split()))
       for _ in range(n)]
for a, b in segments:
    a += offset
    b += offset
    for i in range(a, b):
        arr[i] += 1
max_index = max(arr)
print(max_index)