grid = [list(map(int, input().split())) for _ in range(10)]
visited = [[0] * 10 for _ in range(10)]
cnt = 0

def can_place(x, y, s):
    for i in range(x, x+s):
        for j in range(y, y+s):
            if not grid[i][j]:
                return False
            if visited[i][j]:
               return False

    return True

def in_range(x, y, s):
    return 0 <= x + s-1 < 10 and 0 <= y + s-1 < 10

def check_visited(x, y, s):
    for i in range(x, x+s):
        for j in range(y, y+s):
            visited[i][j] = 1


for s in range(5, 0, -1):
    paper = 0
    for x in range(10):
        for y in range(10):
            if paper <= 5 and in_range(x, y, s) and can_place(x, y, s):
                check_visited(x, y, s)
                paper += 1
                cnt += 1

if visited != grid:
    print(-1)
else: print(cnt)