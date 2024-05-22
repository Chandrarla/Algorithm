# memo = [-1] * 100
#
# def fibo(n):
#     if memo[n] != -1:
#         return memo[n]
#
#     if n <= 2:
#         memo[n] = 1
#     else:
#         memo[n] = fibo(n-1) + fibo(n-2)
#
#     return memo[n]
#
# print(fibo(99))

# ----------------------------
# n = 10
#
# dp = [0] * 50
# dp[1] = 1
# dp[2] = 1
#
# for i in range(3, n+1):
#     dp[i]= dp[i-1] + dp[i-2]
#
# print(dp[n])

# ----------------------------

# import sys
#
# INT_MIN = -sys.maxsize
#
# n = 4
# a = [
#     [4],
#     [6, 2],
#     [3, 7, 9],
#     [3, 4, 9, 9]
# ]
#
# dp = [
#     [0 for _ in range(4)]
#     for _ in range(4)
# ]
#
# def initialize():
#     dp[0][0] = a[0][0]
#
#     for i in range(1, n):
#         dp[i][0] = a[0][0] + a[i][0]
#
#     for i in range(1, n):
#         dp[i][i] = a[i-1][i-1] + a[i][i]
#
# initialize()
#
# for i in range(2, n):
#     for j in range(1, i):
#         dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + a[i][j]
#
# ans = INT_MIN
# for j in range(n):
#     ans = max(ans, dp[n-1][j])
#
# print(ans)

# ------------------------

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

def initialize():
    dp[0][0] = arr[0][0]

    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + arr[0][i]

    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + arr[i][0]

initialize()

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + arr[i][j]

ans = 0
for i in range(n):
    ans = max(ans, dp[n-1][i])

print(ans)