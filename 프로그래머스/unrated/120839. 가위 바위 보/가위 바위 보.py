def solution(rsp):
    ans = ''
    # 가위 2 바위 0 보 5
    for i in range(len(rsp)):
        if rsp[i] == '2':
            ans += '0'
        elif rsp[i] == '0':
            ans += '5'
        elif rsp[i] == '5':
            ans += '2'
    
    return ans