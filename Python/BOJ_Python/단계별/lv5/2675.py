for _ in range(int(input())):
    R, S = input().split()
    for i in range(len(S)):
        print(S[i]*int(R), end='')
    print()