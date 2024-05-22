K, N = list(map(int, input().split()))
arr = []

def choose(curr_num):
    if curr_num == N + 1:
        print_arr()
        return

    for i in range(1, K + 1):
        if i not in arr:  # 중복 방지
            arr.append(i)
            choose(curr_num + 1)
            arr.pop()

def print_arr():
    for elem in arr:
        print(elem, end=" ")
    print()

choose(1)

'''
가능한 순열을 모두 생성하고, 걸러내기 떄문에 비효율적인 방식, 시간초과 남
def choose(curr_num):
    if curr_num == N+1:
        print_arr()
        return

    for i in range(K):
        arr.append(i+1)
        choose(curr_num+1)
        arr.pop()

def print_arr():
    if not is_dup(arr):
        for elem in arr:
            print(elem, end=" ")
        print()
# print( -, end = "") 출력 방식과 .join(-)을 구별할것

def is_dup(arr):
    tmp = sorted(arr) # tmp를 sort 하지 않아서 오답 발생
    if len(tmp) == 1: return False
    for i in range(len(tmp)-1):
        if tmp[i] == tmp[i+1]:
            return True
    return False
'''