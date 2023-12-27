def solution(arr):
    res = []
    for i in range(len(arr)):
        for _ in range(arr[i]):
            res.append(arr[i])
    
    return res