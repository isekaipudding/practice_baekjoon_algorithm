# 2606번(바이러스) 문제 : https://www.acmicpc.net/problem/2606
import sys

input = sys.stdin.readline

# 1260번(DFS와 BFS) 문제를 이해하고 풀면 이 문제도 이해할 수 있습니다.
# DFS 혹은 BFS 둘 중 아무 것나 해도 상관 없으나 저는 DFS 알고리즘을 채용합니다.

# 깊이 우선 탐색 알고리즘 사용
def dfs(n) :
    global count # 전역 변수 count 사용
    visited[n] = True
    count += 1
    for i in range(1, computers + 1) :
        if graph[n][i] == 1 and visited[i] == False :
            dfs(i)

computers:int = int(input().rstrip()) # 컴퓨터 개수(노드 개수)
linked:int = int(input().rstrip()) # 직접 연결되어 있는 컴퓨터 쌍의 수(간선 개수)

# 인접 행렬, 인접 리스트 중 인접 행렬 사용
graph:list = [[0 for _ in range(computers + 1)] for _ in range(computers + 1)]

for i in range(linked) :
    u, v = map(int, input().split()) # 출발 노드 u, 도착 노드 v
    graph[u][v] = graph[v][u] = 1 # 무방향이므로 u->v, v->u 둘 다 1로 저장
    
visited:list = [False for _ in range(computers + 1)]
count = 0
dfs(1)
print(count - 1) # 1번 컴퓨터를 제외한 나머지 바이러스에 감염된 컴퓨터 수 출력