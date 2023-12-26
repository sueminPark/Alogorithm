def solution(n, control):
    ans = n
    
    for i in control:
        if i == "w":
            ans += 1
        elif i == "s":
            ans -= 1
        elif i == "d":
            ans += 10
        elif i == "a":
            ans -= 10
    return ans