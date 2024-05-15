K, N = list(map(int, input().split()))
arr = []

def choose(curr_num):
    if curr_num == N:
        for elem in arr:
            print(elem, end=" ")
        print()
        return

    for i in range(1, K+1):
        if curr_num >= 2 and i == arr[-1] and i == arr[-2]:
            continue
        else:
            arr.append(i)
            choose(curr_num+1)
            arr.pop()

choose(0)