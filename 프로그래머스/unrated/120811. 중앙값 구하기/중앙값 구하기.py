def solution(array):
    lst = sorted(array)
    ans = lst[len(lst)//2 + len(lst) % 2 -1]
    return ans