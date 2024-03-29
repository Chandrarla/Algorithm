k, n = tuple(map(int, input().split()))
ans = []


def choose(curr_n):
    if curr_n == n + 1:
        for elem in ans:
            print(elem, end=" ")
        print()
        return

    for i in range(1, k + 1):
        ans.append(i)
        choose(curr_n+1)
        ans.pop()


choose(1)