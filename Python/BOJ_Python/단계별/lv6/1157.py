text = input().upper()
uniText = list(set(text))

cntList = []
for i in uniText:
    cnt = text.count(i)
    cntList.append(cnt)

if cntList.count(max(cntList)) > 1:
    print("?")
else:
    maxIndex = cntList.index(max(cntList))
    print(uniText[maxIndex])
