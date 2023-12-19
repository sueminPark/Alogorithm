def solution(money):
    num = 0
    change = 0
    num = money // 5500  
    change = money - num * 5500
    
    return num, change