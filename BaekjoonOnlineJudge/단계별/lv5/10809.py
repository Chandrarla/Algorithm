from string import ascii_lowercase

word = input()
alphaList = list(ascii_lowercase)
arr = []

for i in alphaList:
    if i in word:
        arr.append(word.index(f'{i}'))
    elif i not in word:
        arr.append('-1')
print(*arr)

# for i in alphaList:
#     print(i) # >> a
#     print(alphaList[i]) # >> error