OFFSET = 1000
checked = [
    [0] * 2001
    for _ in range(2001)
]

for k in range(1, 4):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
    for i in range(x1, x2):
        for j in range(y1, y2):
            checked[i][j] += k

cnt = 0

for i in range(2001):
    for j in range(2001):
        if checked[i][j] == 1 or checked[i][j] == 2:
            cnt += 1

print(cnt)