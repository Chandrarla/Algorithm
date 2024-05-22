# class Person:
#     def __init__(self, name, address, region):
#         self.name = name
#         self.address = address
#         self.region = region
#
# n = int(input())
# People = []
#
# for _ in range(n):
#     name, address, region = tuple(input().split())
#     People.append(Person(name, address, region))
#
# print(People)
# 출력 : [<__main__.Person object at 0x104d53950>, <__main__.Person object at 0x104d53990>, <__main__.Person object at 0x104d539d0>]

# ---------------- 오답 ----------------

class Person:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
people = [Person(name, address, region) for name, address, region in arr]

idx = 0
for i, person in enumerate(people):
    if person.name > people[idx].name:
        idx = i

print(f"name {people[idx].name}")
print(f"addr {people[idx].address}")
print(f"city {people[idx].region}")