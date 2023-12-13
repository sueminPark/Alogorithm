# 가로 세로 100 정사각형 도화지
# 가로 세로 10인 종이
# 3
# 3 7
# 15 7
# 5 2

# 260

# 좌표
boards = [[0]* 100 for _ in range(100)]
cnt = 0
# 색종이 수
n = int(input())
# 색종이 붙인 위치
# 왼쪽 아래 꼭짓점 좌표
for i in range(n):
    x, y = list(map(int, input().split()))

    for x_idx in range(x, x+10):
        for y_idx in range(y, y+10):
            # x,y 좌표의 픽셀을 지나갈 떄마다 1로 표시해놓음
            boards[x_idx][y_idx] = 1
#
for row in boards:
    cnt += row.count(1)

print(cnt)