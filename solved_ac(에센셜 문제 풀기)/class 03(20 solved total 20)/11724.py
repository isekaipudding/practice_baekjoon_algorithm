# 11724번(연결 요소의 개수) 문제 : https://www.acmicpc.net/problem/11724
import sys
from collections import deque

input = sys.stdin.readline

# 1012번 문제(유기농 배추)와 큰 관련이 있는 문제입니다.

# 너비 우선 탐색 알고리즘 사용
def bfs(n) :
    queue = deque()
    queue.append(n)
    visited[n] = True
    while queue :
        n = queue.popleft()
        for i in range(1, nodes+1, 1) :
            if graph[n][i] == True and visited[i] == False :
                queue.append(i)
                visited[i] = True
    return

nodes, edges = map(int, input().split())
graph:list = [[False for _ in range(nodes + 1)] for _ in range(nodes + 1)] # 가중치 없는는 인접 행렬 선언
visited:list = [False for _ in range(nodes + 1)] # 방문 여부 리스트 선언

for i in range(edges) :
    u, v = map(int, input().split()) # u : 출발 노드, v : 도착 노드드
    # 무방향(양방향) 간선 추가가
    graph[u][v] = True
    graph[v][u] = True

connected_components:int = 0
for u in range(1, nodes+1, 1) :
    # for v in range(1, nodes+1, 1) : 이 코드는 필요없어서 생략합니다.
    if visited[u] == False : # 간선이 있어야만 연결 요소인 것은 아닙니다. 간선이 없을 경우 노드 자체가 연결 요소입니다.
        connected_components += 1
        bfs(u)
            
print(connected_components)