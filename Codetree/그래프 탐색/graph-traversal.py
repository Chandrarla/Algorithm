N, M = list(map(int, input().split()))
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
cnt = 0

for _ in range(M):
    x, y = list(map(int, input().split()))
    graph[x][y] = 1
    graph[y][x] = 1

def DFS(vertex):
    global cnt
    visited[vertex] = True
    for curr_v in range(1, N+1):
        if graph[vertex][curr_v] and not visited[curr_v]:
            cnt += 1
            DFS(curr_v)

DFS(1)
print(cnt)