def solution(my_string):
    num = '0123456789'
    ans = 0
    for i in range(len(my_string)):
        if my_string[i] in num:
            ans += int(my_string[i])
        else:
            ans += 0
    return ans
        
            