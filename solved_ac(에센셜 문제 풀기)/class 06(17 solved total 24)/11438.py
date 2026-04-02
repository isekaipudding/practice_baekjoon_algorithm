# 11438번(LCA 2) 문제 : https://www.acmicpc.net/problem/11438
import sys
from collections import deque

input = sys.stdin.readline

# 2^16 < 100000 < 2^17이므로 LOG는 17이면 충분합니다.
LOG = 17

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

def bfs() :
    queue = deque([1])
    visited[1] = True
    depth[1] = 0
    
    while queue :
        current:int = queue.popleft()
        for node in graph[current] :
            if not visited[node] :
                visited[node] = True
                parent[node][0] = current
                depth[node] = depth[current] + 1
                queue.append(node)

N:int = int(input().rstrip())

graph:list = [[] for _ in range(N + 1)]
for _ in range(N - 1) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
parent:list = [[0 for _ in range(LOG)] for _ in range(N + 1)]
depth:list = [0 for _ in range(N + 1)]
visited:list = [False for _ in range(N + 1)]

# 너비 우선 탐색 실행
bfs()

for k in range(1, LOG, 1) :
    for i in range(1, N + 1, 1) :
        if parent[i][k-1] != 0 :
            parent[i][k] = parent[parent[i][k-1]][k-1]

M:int = int(input().rstrip())
for _ in range(M) :
    u, v = map(int, input().split())
    print(get_lca(u, v))