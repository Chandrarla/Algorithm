a, b = map(int, input().split())
c = int(input())

min = b + c
hour = a + (min // 60)

if min > 59 and hour < 23:
    print(hour, min % 60)
elif min > 59 and hour >= 23:
    print(hour % 24, min % 60)
else:
    print(a, min)
