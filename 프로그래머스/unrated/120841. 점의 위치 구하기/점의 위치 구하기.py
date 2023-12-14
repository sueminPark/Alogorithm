def solution(dot):
    ans = 0
    if dot[0] > 0 and dot[1] > 0:
        ans = 1
    elif dot[0] < 0 and dot[1] > 0:
        ans = 2
    elif dot[0] < 0 and dot[1] < 0:
        ans = 3
    elif dot[0] > 0 and dot[1] < 0:
        ans = 4
        
    return ans