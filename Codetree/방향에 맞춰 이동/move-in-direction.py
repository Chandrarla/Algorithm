n = int(input())

x, y = 0, 0

dict = {
    'E': 0,
    'S': 1,
    'W': 2,
    'N': 3
}

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    dir, dist = tuple(input().split())
    dist = int(dist)

    x += dx[dict[dir]] * dist
    y += dy[dict[dir]] * dist

print(x, y)