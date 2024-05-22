def solution(k, dungeons):
    global max_val  # 전역 변수 사용 선언
    max_val = 0  # 함수가 호출될 때마다 초기화
    visited = [False for _ in range(len(dungeons))]

    def dfs(k, cnt):
        global max_val
        max_val = max(max_val, cnt)

        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                dfs(k - dungeons[i][1], cnt + 1)
                visited[i] = False

    dfs(k, 0)
    return max_val
