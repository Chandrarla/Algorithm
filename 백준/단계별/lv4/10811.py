N, M = map(int, input().split()) # N = 리스트 크기, M = 반복 횟수
arr = []

for i in range(N):
    arr.append(i+1) # 바구니에 번호 할당

for _ in range(M):
    i, j = map(int, input().split()) # 구간 입력

    front = arr[:i-1] # 리스트 슬라이싱
    middle = arr[i-1:j]
    middle.reverse()
    back = arr[j:]
    arr = front + middle + back

print(*arr)