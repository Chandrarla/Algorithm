my_bingo = [list(map(int, input().split())) for _ in range(5)]
called_bingo = [list(map(int, input().split())) for _ in range(5)]

def row_bingo(myBingo):
    bingo_cnt = 0
    for i in range(5):
        sum_row = 0
        for j in range(5):
            sum_row += myBingo[i][j]
        if sum_row == 0:
            bingo_cnt += 1
    return bingo_cnt

def column_bingo(myBingo):
    bingo_cnt = 0
    for i in range(5):
        sum_col = 0
        for j in range(5):
            sum_col += myBingo[j][i]
        if sum_col == 0:
            bingo_cnt += 1
    return bingo_cnt

def cross_bingo(myBingo):
    bingo_cnt = 0
    sum_diag1 = 0
    sum_diag2 = 0
    for i in range(5):
        sum_diag1 += myBingo[i][i]
        sum_diag2 += myBingo[i][4 - i]
    if sum_diag1 == 0:
        bingo_cnt += 1
    if sum_diag2 == 0:
        bingo_cnt += 1
    return bingo_cnt

def check_bingo(num):
    for i in range(5):
        for j in range(5):
            if num == my_bingo[i][j]:
                my_bingo[i][j] = 0
                return

cnt = 0

for i in range(5):
    for j in range(5):
        check_bingo(called_bingo[i][j])
        cnt += 1
        if row_bingo(my_bingo) + column_bingo(my_bingo) + cross_bingo(my_bingo) >= 3:
            print(cnt)
            exit()
