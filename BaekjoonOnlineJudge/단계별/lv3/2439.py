# n = int(input())
# arr = []
#
# for _ in range(n):
#     arr.append(' ')
#
# for i in range(1, n + 1):
#     arr[-i] = '*'
#     for j in arr:
#         print(j, end='')   : end='' 때문에 개행이 안 됐음.

n = int(input())

blank = ' '
star = '*'

for i in range(1, n+1):
    print(f'{blank*(n-i)}{star*i}')