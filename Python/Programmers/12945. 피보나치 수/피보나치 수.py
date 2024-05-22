def solution(n):
    answer = fibo(n) % 1234567
    return answer


def fibo(n):
    F = [0,1]
    for i in range(1, n+1):
        F.append(F[i-1] + F[i])
    return F[n]