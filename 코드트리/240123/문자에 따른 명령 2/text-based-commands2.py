dirs = input()
curr_dir = 3

x, y = 0, 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for c_dir in dirs:
    # 반시계방향 회전
    if c_dir == "L":
        curr_dir = (curr_dir +3) % 4
    # 시계방향 회전
    elif c_dir == "R":
        curr_dir = (curr_dir +1) % 4
    else:
        x, y = x + dx[curr_dir], y + dy[curr_dir]

print(x, y)