import sys
input = sys.stdin.readline
import heapq

n, e = map(int, input().split())
edges = [[] for i in range(n+1)]

# 양쪽 노드 정보 저장
for i in range(e):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

v1, v2 = map(int, input().split())

ans = float('inf')


def dijkstra(start, s):
    # 시작노드로부터 모든 노드까지 최단거리 저장할 리스트 무한대로 초기화
    distance = [ans] * (s+1) # 이거 몰랐는데 블로그 참고함

    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0 # 시작 노드 최단거리 0으로

    # 큐 빌떄까지
    while q:
        # 가장 짧은 거리 노드 꺼내
        dist, node = heapq.heappop(q)

        # 현재 노드 최단 거리가 이미 계산된 거리보다 작으면 무시ㄱ
        if distance[node] < dist:
            continue

        # 현재 노드 인접노드 확인
        for n, w in edges[node]:
            # 인접 노드 거쳐가는 새로운 거리 계산해주기
            cost = dist + w

            # 새로운 거리가 기존 거리보다 짧으면 갱신
            # 우선순위 큐에 추가
            if distance[n] > cost:
                distance[n] = cost
                heapq.heappush(q, [cost, n])

    return distance

# 최단 경로 담아
d1 = dijkstra(1, n)
d2 = dijkstra(v1, n)
d3 = dijkstra(v2, n)


# v1을 먼저 들리거나
# v2를 먼저 들리거나
# 둘 중 더 짧은 거리 쓰자
result = min(d1[v2] + d2[n] + d3[v1], d1[v1] + d2[v2] + d3[n])


if result == ans:
    print(-1)
else:
    print(result)