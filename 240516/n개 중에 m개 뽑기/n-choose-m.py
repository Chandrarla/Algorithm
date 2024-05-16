n, m = list(map(int, input().split()))
arr = []

def choose(curr_num, cnt):
    if curr_num == n+1:
        if cnt == m:
            for elem in arr:
                print(elem, end= " ")
            print()
        return

    arr.append(curr_num)
    choose(curr_num+1, cnt+1)
    arr.pop()

    choose(curr_num+1, cnt)


choose(1, 0)