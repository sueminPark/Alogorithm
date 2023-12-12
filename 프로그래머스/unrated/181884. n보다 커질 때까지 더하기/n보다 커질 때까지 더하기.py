def solution(numbers, n):
    ans = 0
    for i in range(len(numbers)):
        ans += numbers[i]
        if ans > n:
            return ans