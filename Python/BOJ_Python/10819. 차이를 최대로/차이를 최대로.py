n = int(input())
arr = list(map(int, input().split()))
tmp = []
is_visited = [0] * (n+1)
max_val = 0

def calculate():
    sum = 0
    for i in range(n-1):
        sum += abs(tmp[i] - tmp[i+1])
    return sum


def choose(curr_num):
    global  max_val

    if curr_num == n+1:
        max_val = max(max_val, calculate())
        return

    for i in range(len(arr)):
        if is_visited[i]:
            continue
        else:
            tmp.append(arr[i])
            is_visited[i] = 1
            choose(curr_num+1)
            tmp.pop()
            is_visited[i] = 0

choose(1)
print(max_val)
