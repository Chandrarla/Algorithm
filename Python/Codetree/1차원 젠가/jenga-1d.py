n = int(input())
arr = [int(input()) for _ in range(n)]
del1_s, del1_e = tuple(map(int, input().split()))
del2_s, del2_e = tuple(map(int, input().split()))


def remove_block(x, y):
    for i in range(x - 1, y):
        arr[i] = 0
    return arr


def fall(arr):
    temp = []
    BLANK = 0
    for i in range(len(arr)):
        if arr[i] != BLANK:
            temp.append(arr[i])
    return temp


arr = remove_block(del1_s, del1_e)
arr = fall(arr)
arr = remove_block(del2_s, del2_e)
arr = fall(arr)
print
print(len(arr))
for elem in arr:
    print(elem)