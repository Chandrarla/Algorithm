n = int(input())

people = []

for _ in range(n):
    name, height, weight = tuple(input().split())
    people.append((name, int(height), int(weight)))

people.sort(key=lambda x: (x[1], -x[2]))

for person in people:
    lname, h, w = person
    print(lname, h, w)