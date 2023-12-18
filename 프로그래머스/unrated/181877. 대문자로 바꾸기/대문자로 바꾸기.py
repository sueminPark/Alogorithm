def solution(myString):
    ans = ''
    for i in range(len(myString)):
        if myString[i] in 'abcdefghijklmnopqrstuvwxyz':
            ans += myString[i].upper()
        else:
            ans += myString[i]

    return ans