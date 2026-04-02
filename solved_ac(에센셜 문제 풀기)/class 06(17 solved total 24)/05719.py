# 5719번(거의 최단 경로) 문제 : https://www.acmicpc.net/problem/5719
import sys
import heapq
from collections import deque

input = sys.stdin.readline

# 최단경로(1753번) 소스 코드를 재활용합니다.

INF:int = 10**15

def dijkstra(start_node, graph, num_nodes, removed) :
    distances:list = [INF for _ in range(num_nodes)]
    distances[start_node] = 0
    pq:list[tuple] = [(0, start_node)]

    while pq :
        cur_d, u = heapq.heappop(pq)
        if cur_d != distances[u] :
            continue
        for v, w in graph[u] :
            # 제거된 간선(어떤 최단 S->D 경로에 포함된 간선)은 건너뜁니다.
            if (u, v) in removed :
                continue
            nd = cur_d + w
            if nd < distances[v]:
                distances[v] = nd
                heapq.heappush(pq, (nd, v))
    return distances

while True :
    N, M = map(int, input().split())
    if N == 0 and M == 0 :
        break

    S, D = map(int, input().split())

    graph:list = [[] for _ in range(N)]
    rev:list   = [[] for _ in range(N)] # 역그래프 : 역추적용

    for _ in range(M) :
        U, V, P = map(int, input().split())
        graph[U].append((V, P))
        rev[V].append((U, P))

    removed:set = set()

    # (1) S로부터의 최단거리 배열 계산
    dist1:list = dijkstra(S, graph, N, removed)

    # D에 도달 불가능하면 “거의 최단 경로”도 존재할 수 없습니다.
    if dist1[D] == INF :
        print("-1")
        continue

    # (2) D에서 역방향으로 올라가며 최단경로에 속한 모든 간선을 제거 표시
    queue = deque([D])
    visited = [False for _ in range(N)]
    visited[D] = True
    while queue :
        v = queue.popleft()
        for u, w in rev[v] :
            if dist1[u] + w == dist1[v] :
                # 간선 u->v가 어떤 S->D 최단 경로에 포함됩니다.
                if (u, v) not in removed :
                    removed.add((u, v))
                    if not visited[u]:
                        visited[u] = True
                        queue.append(u)

    # (3) 제거된 간선을 무시하며 다익스트라 재실행 -> 거의 최단 경로
    dist2:list = dijkstra(S, graph, N, removed)
    print(str(dist2[D] if dist2[D] != INF else -1))