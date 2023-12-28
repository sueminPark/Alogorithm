def solution(n, k):
    lst = []
    for i in range(1, n//k +1):
        lst.append(k*i)
    return lst