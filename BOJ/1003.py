n, m = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

def is_happy_seq(A, B, C):
    global last_elem
    sum = 0
    for i in range(A, B+1):
        for j in range(C+1):
            sum += grid[i][j]
            last_elem = grid[i][j]
        if sum == last_elem * m:
            return True
        else: return False

happy_seq_cnt = 0

for row in range(n):
    for col in range(n):
        if row + (m-1) >= n:
            continue
        elif is_happy_seq(row, row+(m-1), col):
            happy_seq_cnt += 1

for col in range(n):
    for row in range(n):
        if col + (m-1) >= n:
            continue
        elif is_happy_seq(col, col+(m-1), row):
            happy_seq_cnt += 1

print(happy_seq_cnt)
