sentence = input()

if ' ' == sentence[0] and ' ' == sentence[-1]:
    print(sentence.count(' ')-1)
elif ' ' == sentence[0] or ' ' == sentence[-1]:
    print(sentence.count(' '))
else:
    print(sentence.count(' ')+1)

#[ hi my name ]
# 단어수 : 3개, 공백 : 4
#[hi my name ]
# 단어수 : 3개, 공백 : 3개