# 등급에 따른 과목평점 변환 함수
def convert(a):
    if a == 'A+':
        a = 4.5
    elif a == 'A0':
        a = 4.0
    elif a == 'B+':
        a = 3.5
    elif a == 'B0':
        a = 3.0
    elif a == 'C+':
        a = 2.5
    elif a == 'C0':
        a = 2.0
    elif a == 'D+':
        a = 1.5
    elif a == 'D0':
        a = 1.0
    elif a == 'F':
        a = 0.0
    elif a == 'P':
        a = 0.0
    return a

sum = 0
creditSum = 0

for _ in range(20):
    name, credit, grade = map(str, input().split())
    # P 과목 계산에서 제외
    if grade == 'P':
        pass
    else:
        sum += float(credit)*float(convert(grade))
        creditSum += float(credit)

print(sum/creditSum)