def solution(num_str):
    ans = 0
    for i in range(len(num_str)):
        ans += int(num_str[i])
    return ans