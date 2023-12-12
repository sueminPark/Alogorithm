def solution(s1, s2):
    cnt = 0
    for i in range(len(s2)):
        if s2[i] in s1:
            cnt += 1
    return cnt