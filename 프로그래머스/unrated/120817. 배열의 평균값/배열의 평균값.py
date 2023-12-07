def solution(numbers):
    answer = 0
    for i in range(len(numbers)):
        answer += numbers[i]
    ans = answer / len(numbers)
    return ans