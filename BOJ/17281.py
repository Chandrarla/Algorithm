# 1. 3아웃 발생하면 이닝 종료
# 2. 9번타자에서 1번타자
# 3. 득점 시스템
# 4. 1번 선수가 4번 타자

from itertools import permutations

inning = int(input())
expect = [list(map(int, input().split())) for _ in range(inning)]
result = float('-inf')
players = [i for i in range(1, 9)]

for case in permutations(players, 8):
    case = list(case)
    entry = case[:3] + [0] + case[3:]
    number, score = 0, 0
    for i in range(inning):
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            if expect[i][entry[number]] == 0:
               out += 1
            elif expect[i][entry[number]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif expect[i][entry[number]] == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif expect[i][entry[number]] == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif expect[i][entry[number]] == 4:
                score += 1 + b1 + b2 + b3
                b1, b2, b3 = 0, 0, 0
            number += 1
            if number == 9:
                number = 0
    result = max(result, score)
print(result)