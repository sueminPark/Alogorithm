n = int(input())
state = list(map(int, input().split()))
s = int(input())
for _ in range(s):
    gender, num = map(int, input().split())

    if gender == 1:
        for i in range(1, n+1):
            if i % num == 0:
                state[i-1] = 1-state[i-1]   # 남학생이 받은 수의 배수이면 숫자 바꾸기

    elif gender == 2:
        l_idx = num - 2
        r_idx = num
        while l_idx >= 0 and r_idx < n and state[l_idx] == state[r_idx]:
            if state[l_idx] == 0:
                state[l_idx], state[r_idx] = 1, 1
            elif state[l_idx] == 1:
                state[l_idx], state[r_idx] = 0, 0
            l_idx -= 1
            r_idx += 1
            
        if state[num-1] == 0:
            state[num-1] = 1
        else:
            state[num-1] = 0


for k in range(0, n, 20):
    print(*state[k: k+20])