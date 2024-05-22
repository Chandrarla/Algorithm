digits = []
binary = list(map(int, list(input())))
length = len(binary)

num = 0
for i in range(length):
    num = num * 2 + binary[i]
    
print(num)