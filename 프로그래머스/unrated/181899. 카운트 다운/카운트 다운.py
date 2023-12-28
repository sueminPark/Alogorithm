def solution(start, end_num):
    ans =[]
    while start >= end_num:
        ans.append(start)
        start -= 1
    return ans