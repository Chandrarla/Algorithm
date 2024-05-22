n = int(input())

students = [
    tuple(input().split())
    for _ in range(n)]

students.sort(key=lambda x: (int(x[1]) + int(x[2]) + int(x[3])))

for student in students:
    name, kor, math, eng = student
    print(name, kor, math, eng)