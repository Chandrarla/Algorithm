OFFSET = 100
checked = [
    [0] * 201
    for _ in range(201)
]

n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
    for i in range(x1, x2):
        for j in range(y1, y2):
            checked[i][j] = 1

cnt = 0
for i in range(201):
    for j in range(201):
        if checked[i][j] == 1:
            cnt += 1

print(cnt)