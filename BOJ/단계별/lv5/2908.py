a, b = input().split()
print(reversed(a))

reversed_a = ",".join(reversed(a))
print(reversed_a)
reversed_b = "".join(reversed(b))

if int(reversed_a) > int(reversed_b):
    print(reversed_a)
else:
    print(reversed_b)

# "".join(reversed(b))
# reversed(b), b를 reverse
# 빈 string("")에 reversed b를 join
