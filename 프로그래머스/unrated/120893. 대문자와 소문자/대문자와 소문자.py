def solution(my_string):
    ans = ''
    for i in range(len(my_string)):
        if my_string[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            ans += my_string[i].lower()
        elif my_string[i] in 'abcdefghijklmnopqrstuvwxyz':
            ans += my_string[i].upper()
    return ans
        