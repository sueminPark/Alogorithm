def solution(my_string):
    ans = ''
    for i in range(len(my_string)):
        if my_string[i] in 'aeiou':
            ans += ''
        else:
            ans += my_string[i]
            
    return ans