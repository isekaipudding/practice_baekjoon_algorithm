# 1167번(트리의 지름) 문제 : https://www.acmicpc.net/problem/1167
import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

# 깊이 우선 탐색 알고리즘 채택
def dfs(node, dist) :
    global max_distance, max_node
    visited[node] = True
    if dist > max_distance:
        max_distance = dist
        max_node = node
    for next_node, weight in graph[node]:
        if not visited[next_node]:
            dfs(next_node, dist + weight)

V:int = int(input().rstrip())
# 노드의 개수가 최대 10만개이므로 엄청 많아 인접 리스트로 선언
graph:list = [[] for _ in range(V + 1)]

for _ in range(V):
    query:list = list(map(int, input().split()))
    start:int = query[0]
    index:int = 1
    while index < len(query):
        if query[index] == -1:
            break
        end:int = query[index]
        weight:int = query[index + 1]
        graph[start].append((end, weight)) # 가중치 있는 단거리 그래프이므로 이렇게 원소를 추가합니다.
        index += 2

visited:list = [False for _ in range(V + 1)] # 방문 여부 확인을 위해 visited 리스트를 추가합니다.
max_distance:int = 0
max_node:int = 1

# 첫 번째 DFS from 임의의 노드(예: 1)
dfs(1, 0)

# 두 번째 DFS from max_node 구하기
visited:list = [False for _ in range(V + 1)]
max_distance:int = 0
dfs(max_node, 0)

# 최종적으로 트리의 지름인 max_distance 출력
print(max_distance)