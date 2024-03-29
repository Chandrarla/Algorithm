k, n = tuple(map(int, input().split()))
arr = []

def choose(curr_n):
    if curr_n == n:
        print_ans()
        return

    for i in range(1, k + 1):

        if curr_n>=2 and i == arr[-1] and i == arr[-2]: 
        # 세 번째 자리에 i를 넣을 때 첫 번째, 두 번째 자리가 모두 i인 경우를 제외
            continue
        else:
            arr.append(i)
            choose(curr_n + 1)
            arr.pop()

def print_ans():
    for num in arr:
        print(num, end=" ")
    print()

choose(0)