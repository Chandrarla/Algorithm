from copy import deepcopy
from collections import deque
from itertools import combinations

def attack(archor):
    board = deepcopy(grid)
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N-1, -1, -1):
        die = []
        for m in archor: # 한명의 궁수가 공격할 적 탐색
            queue = deque() # (i,m)에 있는 적, 사거리 1
            queue.append([i, m, 1])
            while queue:
                x, y, d = queue.popleft()
                if board[x][y]:
                    die.append([x, y])
                    if not visited[x][y]:
                        visited[x][y] = 1
                        cnt += 1
                    break
                if d < D:
                    for dx, dy in zip(dxs, dys):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < M:
                            queue.append([nx, ny, d + 1])
        for x, y in die:
            board[x][y] = 0
    return cnt

N, M, D = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(N)]
dxs, dys = [0, -1, 0], [-1, 0, 1]
result = 0
for archor in combinations([i for i in range(M)], 3):
    result = max(result, attack(archor))

print(result)