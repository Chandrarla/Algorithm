N, M = map(int, input().split())
lst = []

for i in range(1, N + 1):
    lst.append(i)

for _ in range(M):
    i, k, j = map(int, input().split())
    lst = lst[:i-1] + lst[j-1:k] + lst[i-1:j-1] + lst[k:]

print(*lst)
