n = int(input())
lst1 = list(map(int, input().split()))

lst2 = [(i, k) for i, k in enumerate(lst1, start=1) ]

lst2.sort(key=lambda x: x[1])

lst3 = [(a, b, index + 1) for index, (a, b) in enumerate(lst2)]
#list comprehension으로 append를 안 쓰도록

lst3.sort(key=lambda x: x[0])

for (_, _, i) in lst3:
    print(i, end=" ")