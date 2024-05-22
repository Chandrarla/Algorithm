n, t = tuple(map(int, input().split()))
r, c, d = tuple(input().split())
r, c = int(r), int(c)

dict = {
    'U': 0,
    'R': 1,
    'D': 2,
    'L': 3
}


def is_range(x, y):
    return 1 <= x <= n and 1 <= y <= n


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir_num = dict[d]

for _ in range(t):
    nr = r + dx[dir_num]
    nc = c + dy[dir_num]
    if is_range(nr, nc):
        r, c = nr, nc
    else:
        dir_num = (dir_num + 2) % 4

print(r, c)