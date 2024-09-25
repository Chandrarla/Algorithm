N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
memo = [[[-1] * 3 for _ in range(N)] for _ in range(N)]


def in_range(x, y):
    return 1 <= x and x < N+1 and 1 <= y and y < N+1


def is_blocked(x, y):
    if grid[x-1][y]:
        return True
    elif grid[x][y]:
        return True
    elif grid[x][y-1]:
        return True
    return False


def can_go(x1, y1, x2, y2):
    if not in_range(x2, y2):
        return False

    elif grid[x2-1][y2-1]:
        return False

    elif x1 != x2 and y1 != y2 and is_blocked(x1, y1):
        return False

    return True


def set_state(x1, y1, x2, y2):
    if x1 == x2 and y1 != y2:
        return 0
    elif x1 != x2 and y1 == y2:
        return 1
    elif x1 != x2 and y1 != y2:
        return 2


def set_dir(state):
    if state == 0:
        return [0, 1], [1, 1]
    elif state == 1:
        return [1, 1], [0, 1]
    elif state == 2:
        return [0, 1, 1], [1, 0, 1]


def move(x, y, state):
    global ans

    if x == N and y == N:
        return 1

    if memo[x-1][y-1][state] != -1:
        return memo[x-1][y-1][state]

    dxs, dys = set_dir(state)
    count = 0
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if can_go(x, y, new_x, new_y):
            new_state = set_state(x, y, new_x, new_y)
            count += move(new_x, new_y, new_state)

    memo[x-1][y-1][state] = count
    return count


ans = move(1, 2, 0)
print(ans)