blank = ' '
star = '*'
n = int(input())

for i in range(1, n+1):
    print(blank * (n - i) + star * (2 * i - 1))
for i in reversed(range(1, n)):
    print(blank * (n - i) + star * (2 * i - 1))