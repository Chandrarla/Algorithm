import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
cnt = 1
q = deque()
ans = deque()

for i in range(N):
    q.append(i+1)

while q:
    q.rotate(-(K-1))
    ans.append(q.popleft())

print('<'+', '.join(map(str, ans)) + '>')
