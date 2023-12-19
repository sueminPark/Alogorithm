def solution(num_list):
    # 짝수 a, 홀수 b
    a = 0
    b = 0
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            a += 1
        else:
            b += 1
    return a,b