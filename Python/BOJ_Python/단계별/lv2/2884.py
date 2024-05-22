a, b = map(int, input().split())

if (b >= 45):
    print("%d %d" % (a, b - 45))
elif (a == 0 and b < 45):
    print("%d %d" % (a + 23, b + 15))
else:
    print("%d %d" % (a - 1, b + 15))
