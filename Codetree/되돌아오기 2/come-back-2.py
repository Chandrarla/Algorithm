def find_return(dir_str):

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    dir_num = 3
    x, y = 0, 0
    cnt = 0

    for elem in dir_str:
        if elem == 'L':
            dir_num = (dir_num + 3) % 4
        elif elem == 'R':
            dir_num = (dir_num + 1) % 4
        else:
            x, y = x + dx[dir_num], y + dy[dir_num]
        cnt += 1
        if x == 0 and y == 0: return cnt
    return -1
dir_str = input()
print(find_return(dir_str))