import sys
a, b = map(int, input().split())
print(a + b)

a, b = map(int, input().split())
print(a - b)

a, b = map(float, input().split())
print(a / b)

a, b = map(int, input().split())
print(a + b, )
print(a - b)
print(a * b)
print(a // b) #나눗셈 후 몫만 반환하는 연산자 '//'
print(a % b)

id = input()
print(id + '??!')

y = int(input())
print(y + 543)

A, B, C = map(int, sys.stdin.readline().split())
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)

