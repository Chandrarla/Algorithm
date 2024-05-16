N, M = list(map(int, input().split()))
graph = [[0 for _ in range(N)] for _ in range(N)]
visited = [False for _ in range(N)]
cnt = 0

for _ in range(M):
    x, y = list(map(int, input().split()))
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

def DFS(vertex):
    global cnt
    for curr_v in range(1, M):
        if graph[vertex][curr_v] and not visited[curr_v]:
            cnt += 1
            visited[curr_v] = True
            DFS(curr_v)

DFS(1)
print(cnt)