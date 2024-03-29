n = int(input())
ans, visited = [], [0] * (n+1)

def choose(curr_n):
    # 탈출 조건, cnt == n+1일 때 출력
    if curr_n == n+1:
        for elem in ans:
            print(elem, end = " ")
        print()

    # 1~n까지 돌면서 ans 배열에 append, visited된 수는 continue
    for i in range(1, n+1):
        if visited[i]:
            continue

        visited[i] = 1
        ans.append(i)

        choose(curr_n+1)

        ans.pop()
        visited[i] = 0

choose(1)