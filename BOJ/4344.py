# 평균을 구한다
# 평균이 넘는 개수를 비교해서 반올림

C = int(input())

for a in range(C):
    sum = 0
    cnt = 0

    A = list(map(int, input().split()))

    for i in range(1, len(A)):
        sum += A[i]

    for j in range(1, len(A)):
        if A[j] > sum / (A[0]):
            cnt += 1

    rate = round((cnt / A[0] * 100), 3)
    print("%0.3f" % rate, end='%\n')
