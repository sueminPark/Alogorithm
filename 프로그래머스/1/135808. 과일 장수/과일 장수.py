def solution(k, m, score):
    # 가장 많은 사과 팔았을 때, 얻을 수 있는 최대 이익
    answer = 0
    # k-최상품 사과 p 최하점
    # m 개씩 한 상자에 포장
    # 사과 한 상자 가격 = p*m 
    
    score.sort(reverse=True)
    
    for i in range(0, len(score), m):
        lst = score[i:i+m]
        
        if len(lst) == m:
            answer += min(lst) * m

    return answer