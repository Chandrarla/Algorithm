n = int(input())

crd = []

for i in range(n):
    x, y = tuple(map(int, input().split()))
    crd.append((abs(x)+abs(y), i+1))

crd.sort(key= lambda x: (x[0], x[1]))

for elem in crd:
    dst, i = elem
    print(i)