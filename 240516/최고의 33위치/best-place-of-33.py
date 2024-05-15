n = int(input())
arr_2d = [list(map(int, input().split())) for _ in range(n)]


def get_total_coin(row_s, col_s, row_e, col_e):
    total_coin = 0
    for row in range(row_s, row_e +1):
        for col in range(col_s, col_e+1):
            total_coin += arr_2d[row][col]
    return total_coin

max_gold = 0

for row in range(n):
    for col in range(n):
        if row +2 >=n or col +2 >= n:
            continue

        total_coin = get_total_coin(row, col, row+2, col+2)

        max_gold = max(max_gold, total_coin)

print(max_gold)