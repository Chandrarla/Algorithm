n = int(input())

students = [tuple(map(int, input().split())) for _ in range(n)]

sorted_students = [(weight, height, idx+1) for idx, (weight, height) in enumerate(students)]

sorted_students.sort(key=lambda x: (x[0], -x[1]))

for elem in sorted_students:
    w, h, i = elem
    print(w, h, i)