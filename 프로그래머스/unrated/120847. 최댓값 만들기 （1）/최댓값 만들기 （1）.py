def solution(numbers):
    # 리스트 내 가장 큰 두 수를 뽑아서 곱해주면 됨
    numbers.sort(reverse=True)
    max_v = numbers[0] * numbers[1]
    return max_v