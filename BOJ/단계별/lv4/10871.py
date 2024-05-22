N, X = map(int, input().split())

arr = list(map(int, input().split()))

for i in arr:
    if i < X:
        print(i, end=' ')

# print(" ", end='\n') => print(" ", end=" ") 개행 없이 출력