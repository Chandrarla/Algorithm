def find_VPS(PS):
    for elem in PS:
        if elem == "(":
            stack.append("(")
        else:
            if len(stack) == 0:
                return ("NO")
            stack.pop()
    if len(stack) == 0:
        return ("YES")
    else:
        return ("NO")

T = int(input())

for _ in range(T):
    stack = []
    PS = input()
    print(find_VPS(PS))
