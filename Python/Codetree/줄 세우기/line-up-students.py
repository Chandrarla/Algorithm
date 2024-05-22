n = int(input())
students = []
for i in range(1, n + 1):
    height, weight = tuple(map(int, input().split()))
    students.append((height, weight, i))

students.sort(key=lambda x: (-x[0], -x[1], x[2]))

for height, weight, number in students:
    print(height, weight, number)