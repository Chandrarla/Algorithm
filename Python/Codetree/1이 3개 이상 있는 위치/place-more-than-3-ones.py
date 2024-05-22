n = int(input())
arr = [list(map(int, input().split()))
       for _ in range(n)]
def in_range(x, y):
    return 0<=x<n and 0<=y<n

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

ans = 0

for i in range(n):
    for j in range(n):
        cnt = 0
        for dir in range(4):
            nx, ny = i + dx[dir], j + dy[dir]
            if in_range(nx, ny) and arr[nx][ny] == 1:
                cnt += 1
        if cnt >=3:
            ans += 1

print(ans)