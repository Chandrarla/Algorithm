n, m = tuple(map(int, input().split()))

arr = [[0] * (n+2) for _ in range(n+2)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

for _ in range(m):
    x, y = tuple(map(int, input().split()))
    arr[x][y] = 1
    cnt = 0
    for i in range(4):
        nx, ny = x + dxs[i], y + dys[i]
        if arr[nx][ny] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)