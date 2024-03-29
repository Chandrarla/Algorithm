n, m = tuple(map(int, input().split()))

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
ans = 0

for _ in range(m):
    a, b = tuple(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

def dfs(vertex):
    global ans
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            ans += 1
            dfs(curr_v)


visited[1] = True
dfs(1)
print(ans)