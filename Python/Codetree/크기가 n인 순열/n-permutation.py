n = int(input())
arr = []
visited = [0]* (n+1)

def choose(curr_num):
    if curr_num == n+1:
        for elem in arr:
            print(elem, end= " ")
        print()
        return

    for i in range(1, n+1):
        if visited[i]:
            continue
        else:
            arr.append(i)
            visited[i] = 1
            choose(curr_num+1)
            arr.pop()
            visited[i] = 0

choose(1)