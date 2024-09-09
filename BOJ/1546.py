n = int(input()) # 과목 수
subj = list(map(int, input().split())) # 과목 점수 입력

sum = 0 # 평균 구하기 위한 과목 점수 합
maxScore = max(subj) # 과목 최대 점수

for i in range(n):
    subj[i] = subj[i]/maxScore*100
    sum += subj[i]

print(sum/n)
