N, M = map(int, input().split())
arr = []
blk = 0

for i in range(1, N+1):
    arr.append(i)

for _ in range(M):
    i, j = map(int, input().split())
    blk = arr[i-1]
    arr[i-1] = arr[j-1]
    arr[j-1] = blk

print(*arr)