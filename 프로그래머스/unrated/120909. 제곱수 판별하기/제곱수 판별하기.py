def solution(n):
    ans = n ** (1/2)
    if ans % 1 == 0:
        return 1
    else:
        return 2