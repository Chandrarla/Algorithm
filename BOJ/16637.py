import sys

n = int(input())
s = input()
result = -1 * sys.maxsize

def cal(x, op, y):
    if op == "+":
        return x+y
    if op == "*":
        return x*y
    if op == "-":
        return x-y

def dfs(idx, val):
    global result

    if idx == n-1:
        result = max(result, val)
        return

    if idx + 2 < n:
        dfs(idx+2, cal(val, s[idx+1], int(s[idx+2])))

    if idx + 4 < n:
        dfs(idx+4, cal(val, s[idx+1], cal(int(s[idx+2]), s[idx+3], int(s[idx+4]))))

dfs(0, int(s[0]))
print(result)

'''
1. 지역변수와 전역변수, global의 사용

m = 5
def func():
    print(m)  - 전역 변수 m을 읽기만 함, global 필요 없음
    m = 10    - 오류 발생: UnboundLocalError (m을 지역 변수로 간주)
    
2. if문에서 and 앞 뒤 조건의 순서
- 앞 조건이 거짓일 경우, 전체 조건은 무조건 거짓이므로 뒤의 조건은 평가하지 않음
'''

