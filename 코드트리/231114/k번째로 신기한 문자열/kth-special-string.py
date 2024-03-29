n, k, t = tuple(input().split())
n, k = int(n), int(k)
words = []

def start_with(a, b):
    if len(a)<len(b): return False
    return a[:len(b)] == b 
    # ==는 비교연산자, True/False를 리턴

words = []
for _ in range(n):
    word = input()
    if start_with(word, t):
        words.append(word)

words.sort()
print(words[k-1])