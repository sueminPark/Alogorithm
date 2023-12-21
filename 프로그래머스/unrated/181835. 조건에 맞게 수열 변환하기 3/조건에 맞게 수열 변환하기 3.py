def solution(arr, k):
    lst = []
    if k % 2==1:
        for i in range(len(arr)):
            lst.append(arr[i] * k)
    else:
        for i in range(len(arr)):
            lst.append(arr[i] +k)
    
    return lst