x, y = 0, 0

order = input()

dir_num = 3

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for elem in order:
    if elem == "L":
        dir_num = (dir_num + 3) % 4
    elif elem == "R":
        dir_num = (dir_num + 1)% 4
    else:
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)