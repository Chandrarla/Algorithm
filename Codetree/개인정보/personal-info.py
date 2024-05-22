people = []

for _ in range(5):
    name, height, weight = tuple(input().split())
    people.append((name, int(height), float(weight)))

people.sort(key=lambda x: x[0])

print("name")
for person in people:
    name, h, w = person
    print(name, h, w)
print()

people.sort(key=lambda x: -x[1])

print("height")
for person in people:
    name, h, w = person
    print(name, h, w)