def solve(lv, tc, tp, diff):
    if lv >= diff:
        return tc
    else:
        return (diff - lv) * (tc + tp) + tc


def solution(diffs, times, limit):
    max_level, min_level = max(diffs), 1

    while min_level < max_level:
        mid_level, mid_total = (max_level + min_level) // 2, 0

        for i in range(len(diffs)):
            if not i:
                time_prev = 0
            else:
                time_prev = times[i - 1]

            time_curr = times[i]

            mid_total += solve(mid_level, time_curr, time_prev, diffs[i])

        if mid_total <= limit:
            max_level = mid_level
        else:
            min_level = mid_level + 1

    return min_level

'''
[문제 유형]
- 이분탐색

[오답 이유]
- level을 +=1 하면서 최소값을 탐색하면서 시간초과가 나왔다.
- 이분탐색을 생각하긴 했는데, 구현에 자신이 없어 러프하게 풀었던 것이 문제였음.

[유의 사항]
- min_level, max_level을 설정하고 중간값으로 계산 후 범위를 좁혀나간다.
- 이분탐색의 종료 시점은 최소, 최대가 같아지는 시점이라는 것에 유의.
'''