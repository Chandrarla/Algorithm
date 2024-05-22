from collections import deque

n, m = map(int, input().split())

# 지도 입력
a = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)] # 각 정점 방문했는지 여부
dist = [[-1 for _ in range(m)] for _ in range(n)] #dist[i][j] (i, j) 도달하는 데에 필요한 최소 거리

def bfs():
    # q를 가지고 너비 우선 탐색
    while q:
        r, c = q.popleft() # 현재 위치가 r행 c열 탐색 중
        for dr, dc in ((1,0), (0,1), (-1,0), (0,-1)):
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < m and a[nr][nc] == 1 and not visited[nr][nc]: # 격자를 벗어나지 않는지, 뱀이 없는지, 방문한 적이 없는지
                visited[nr][nc] = 1
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

q = deque() # 새로운 queue를 생성
visited[0][0] = 1
dist[0][0] = 0
q.append((0, 0))

bfs()
print(dist[n-1][m-1])