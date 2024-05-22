n, m = tuple(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0


def check_arr(arr):
    cnt = 1
    prev = 0
    global ans

    for i in range(n):
        for j in range(n):
            if arr[i][j] != prev:
                cnt = 1
                prev = arr[i][j]
            else:
                cnt += 1
                prev = arr[i][j]
        if cnt >= m:
            ans += 1

    prev = 0

    for k in range(n):
        for l in range(n):
            if arr[l][k] != prev:
                cnt = 1
                prev = arr[l][k]
            else:
                cnt += 1
                prev = arr[l][k]
        if cnt >= m:
            ans += 1

    return


check_arr(arr)
print(ans)