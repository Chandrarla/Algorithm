n, k = tuple(map(int, input().split()))
arr = [tuple(map(int, input().split()))
       for _ in range(k)]

blocks = [0]* (n+1)

# 블럭 쌓기
for a, b in arr:
    for i in range(a, b+1):
        blocks[i] += 1

max_num = max(blocks)
print(max_num)