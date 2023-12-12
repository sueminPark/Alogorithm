def solution(n):
    n_str = str(n)
    ans = 0
    for i in range(len(n_str)):
        ans += int(n_str[i])
    
    return ans