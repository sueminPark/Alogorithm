import sys
input = sys.stdin.readline

n, m = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# bfs 함수
def bfs(y, x):
    size = 1  # 그림의 크기
    q = [(y, x)]
    while q:
        ey, ex = q.pop()   # 큐에서 하나씩 뽑아
        for k in range(4): # 상하좌우 움직이며
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:   # 범위 안에 좌표가 존재할 때
                if info[ny][nx] == 1 and visited[ny][nx] == False:
                    size += 1                 # 그림 크기 늘려주기
                    visited[ny][nx] = True   # 방문 처리
                    q.append((ny, nx))        # 큐에 삽입

    return size



paint = 0
max_v = 0

# 가장 외부 리스트 덩어리 돌면서 그 다음에 내부 리스트 도는 겨
for j in range(n):
    for i in range(m):
        if info[j][i] == 1 and visited[j][i] == False:
            visited[j][i] = True   # 방문처리
            paint += 1              # 전체 그림 개수 증가
            max_v = max(max_v, bfs(j,i)) # bfs를 통해 그림 크기를 구하고, 그 결과를 최댓값에 넣어주며 업데이트


print(paint)
print(max_v)