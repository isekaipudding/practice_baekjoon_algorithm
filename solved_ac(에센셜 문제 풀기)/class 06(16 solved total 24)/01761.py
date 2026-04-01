# 1761번(정점들의 거리) 문제 : https://www.acmicpc.net/problem/1761
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 2^15 < 40000 < 2^16이므로 희소 배열에서 16이면 충분합니다.
LOG = 16

def dfs(current, d, w) :
    visited[current] = True
    depth[current] = d
    distance[current] = w
    
    for next_node, weight in graph[current] :
        if not visited[next_node] :
            parent[next_node][0] = current
            dfs(next_node, d + 1, w + weight)
        
def get_lca(u, v) :
    if depth[u] > depth[v] :
        u, v = v, u

    for k in range(LOG - 1, -1, -1) :
        if depth[v] - depth[u] >= (1 << k) :
            v = parent[v][k]

    if u == v :
        return u

    for k in range(LOG - 1, -1, -1) :
        if parent[u][k] != parent[v][k] :
            u = parent[u][k]
            v = parent[v][k]

    return parent[u][0]

N:int = int(input().rstrip())

# 가중치 있는 무방향 인접 리스트
graph:list = [[] for _ in range(N + 1)]
for _ in range(N - 1) :
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
    
depth:list = [0 for _ in range(N + 1)]
distance:list = [0 for _ in range(N + 1)]
visited:list = [False for _ in range(N + 1)]
parent:list = [[0 for _ in range(LOG)] for _ in range(N + 1)]

# 트리 정보를 초기화하고 루트 노트를 1번으로 가정합니다.
# 희소 배열 초기식 : parent[i][0] = 직계 부모
dfs(1, 0, 0)

# 희소 배열 점화식 : parent[i][k] = parent[parent[i][k-1]][k-1]
for k in range(1, LOG, 1) :
    for i in range(1, N + 1, 1) :
        if parent[i][k-1] != 0 :
            parent[i][k] = parent[parent[i][k-1]][k-1]

M:int = int(input().rstrip())
for _ in range(M) :
    u, v = map(int, input().split())
    # 거리 공식 : 거리(u, v) = 거리(루트, u) + 거리(루트, v) - 2 * 거리(루트, LCA(u, v))
    print(distance[u] + distance[v] - 2 * distance[get_lca(u, v)])