class Product:
    def __init__(self, name, code):
        self.name = name
        self.code = code

p1 = Product("codetree", 50)

p2_name, p2_code = tuple(input().split())

p2 = Product(p2_name, p2_code)

print(f"product {p1.code} is {p1.name}")
print(f"product {p2.code} is {p2.name}")