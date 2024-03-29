n, m = tuple(map(int, input().split()))
ans = []


def choose(curr_n, cnt):
    if curr_n == n + 1:
        if cnt == m:
            for i in range(n):
                if ans[i] == 1:
                    print(i + 1, end=" ")
            print()
        return

    for j in range(1, -1, -1):
        ans.append(j)
        if j == 1:
            choose(curr_n + 1, cnt + 1)
        else:
            choose(curr_n + 1, cnt)
        ans.pop()


choose(1, 0)