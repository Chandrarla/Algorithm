alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
alpha_num = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
sum = 0

num, radix = input().split()
num = "".join(reversed(num))

for i in range(len(num)):
    if num[i] in alphabet:
        sum += alpha_num[alphabet.index(num[i])] * (int(radix) ** i)
    else:
        sum += int(num[i]) * (int(radix) ** i)

print(sum)

# 알파벳 나올 땐 ASCII코드 사용이 좋다, ord() 사용

for i in range(len(num)):
    if ord(num[i]) >= 65 and ord(num[i]) <= 90:
        sum += (ord(num[i]) - 55) * (pow(int(radix), i))
    else:
        sum += int(num[i]) * pow((int(radix)), i)

print(sum)