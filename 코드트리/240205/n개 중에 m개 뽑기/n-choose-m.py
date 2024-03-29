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

    ans.append(1)
    choose(curr_n + 1, cnt + 1)
    ans.pop()

    ans.append(0)
    choose(curr_n + 1, cnt)
    ans.pop()
    
    return


choose(1, 0)