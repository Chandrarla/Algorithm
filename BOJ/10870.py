# dictionary 사용한 memoization

N = int(input())
memo = {}

def fibo(n):
    if n <= 1:
        return n
    elif n not in memo:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

print(fibo(N))

# ++ List 사용하는 방법도 있음
# n = int(input())
# def fibo(n):
#     F = [0, 1]
#     for i in range(2, n+1):
#         F.append(F[i-2] + F[i-1])
#     return F[n]
#
# print(fibo(n))