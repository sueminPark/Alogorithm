def solution(num_list):
    times = 1
    sum = 0
    for i in range(len(num_list)):
        times *= num_list[i]
        sum += num_list[i]
        
    sum_sq = sum**2
    
    if times < sum_sq :
        return 1
    elif times > sum_sq :
        return 0
    else:
        return print("error")