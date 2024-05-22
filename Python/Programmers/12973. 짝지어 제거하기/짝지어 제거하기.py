def solution(s):
    ans = []
    for i in s:
        if not(ans): # ans이 비어있으면
            ans.append(i)
        else:
            if ans[-1] == i:
                ans.pop()
            else:
                ans.append(i)
    if ans: return 0
    else: return 1
