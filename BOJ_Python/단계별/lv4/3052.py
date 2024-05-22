arr = []
result = []

for _ in range(10):
    arr.append(int(input()))

for i in range(10):
    arr[i] = arr[i] % 42

for value in arr:
    if value not in result:
        result.append(value)

print(len(result))



