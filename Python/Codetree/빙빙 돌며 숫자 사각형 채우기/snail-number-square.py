n, m = tuple(map(int, input().split()))
arr = [[0] * m for _ in range(n)]

x, y = 0, 0
arr[x][y] = 1


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir_num = 0

for i in range(2, n * m + 1):
    nx, ny = x + dx[dir_num], y + dy[dir_num]

    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4

    # x, y = nx, ny가 아님에 유의. 바뀐 dir_num을 사용해야 하기 때문.
    x, y = x + dx[dir_num], y + dy[dir_num]
    arr[x][y] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()