cnt = 0

for i in range(int(input())):
    beforeSorted = 0
    afterSorted = 0
    word = input()

    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            beforeSorted += 1

    for k in range(len(word)-1):
        sortedWord = sorted(word)
        if sortedWord[k] != sortedWord[k+1]:
            afterSorted = afterSorted + 1

    if beforeSorted == afterSorted:
        cnt += 1

print(cnt)