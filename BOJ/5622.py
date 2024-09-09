text = input()

sum = 0
num = [0] * 10

num = ['', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

for i in text:
    for j in range(1, 10):
        if i in num[j]:
            sum += (j+1)

print(sum)
