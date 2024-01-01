def solution(n, numlist):
    lst = []
    for i in range(len(numlist)):
        if numlist[i] % n == 0:
            lst.append(numlist[i])
            
    return lst