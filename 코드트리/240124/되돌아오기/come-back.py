def find_cnt(n):
    x, y = 0, 0
    dict = {'E': 0, 'S': 1, 'W': 2, "N": 3}
    dxs = [1, 0, -1, 0]
    dys = [0, -1, 0, 1]

    cnt = 0
    for _ in range(n):
        c_dir, dist = tuple(input().split())
        dist = int(dist)
        dir_num = dict[c_dir]
        for _ in range(dist):
            x, y = x + dxs[dir_num], y + dys[dir_num]
            cnt += 1
            if x == 0 and y == 0: return cnt
    return -1


n = int(input())
print(find_cnt(n))