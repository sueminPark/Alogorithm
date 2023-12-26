def solution(str_list, ex):
    str_list = [s for s in str_list if ex not in s]
    ans = "".join(str_list)
    return ans