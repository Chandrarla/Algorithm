def solution(s):
    int_list = [int(i) for i in s.split()]
    ans = f"{min(int_list)} {max(int_list)}"

    
    return ans