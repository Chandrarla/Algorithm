X, Y = list(input().split())


def Rev(string):
    rev_string = int(''.join(reversed(string)))
    return(rev_string)

ans = Rev(str(int(Rev(X))+ int(Rev(Y))))
print(ans)