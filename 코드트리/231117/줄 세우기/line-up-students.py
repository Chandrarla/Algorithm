n = int(input())

students = [tuple(map(int, input().split())) for _ in range(n)]
arr = []

for idx, (h, w) in enumerate(students, start=1):
    arr.append((h, w, idx))

arr.sort(key = lambda x: (-x[0], -x[1], -x[2])) #정렬 키 작성할 때 괄호 자성

for item in arr:
    h, w, index = item
    print(h, w, index)