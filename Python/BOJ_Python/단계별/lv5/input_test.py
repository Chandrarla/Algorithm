A = list(map(int, input().split()))
print(A)
print(type(A))

a, b = list(map(int, input().split()))
print(a, b)
print(type(a), type (b))

b, c = map(int, input().split())
print(b, c)
print(type(b), type(c))

d, e = input().split()
print(d, e)
print(type(d), type(e))

# >> 12 34
# [12, 34]
# <class 'list'>
# >> 12 34
# 12 34
# <class 'int'> <class 'int'>
# >> 12 34
# 12 34
# <class 'int'> <class 'int'>
# >> 12 34
# 12 34
# <class 'str'> <class 'str'>