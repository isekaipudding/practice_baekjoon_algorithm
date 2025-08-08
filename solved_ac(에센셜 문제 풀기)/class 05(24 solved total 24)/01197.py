# 1197번(최소 스패닝 트리) 문제 : https://www.acmicpc.net/problem/1197
import sys

input = sys.stdin.readline

def find(parent, u) :
    if parent[u] != u :
        parent[u] = find(parent, parent[u])
    return parent[u]

def union(parent, rank, u, v) :
    root_u = find(parent, u)
    root_v = find(parent, v)
    
    if root_u != root_v :
        if rank[root_u] > rank[root_v] :
            parent[root_v] = root_u
        elif rank[root_u] < rank[root_v] :
            parent[root_u] = root_v
        else :
            parent[root_v] = root_u
            rank[root_u] += 1

def kruskal(V, edges) :
    # 간선을 가중치 순으로 정렬합니다.
    edges.sort(key=lambda x: x[2])
    
    parent = [i for i in range(V+1)]
    rank = [0] * (V+1)
    
    mst_weight = 0
    mst_edges = []

    for u, v, weight in edges :
        if find(parent, u) != find(parent, v) :
            union(parent, rank, u, v)
            mst_weight += weight
            mst_edges.append((u, v))

    return mst_weight

# 정점과 간선의 개수 입력
V, E = map(int, input().split())

edges = []

# 간선 정보 입력
for _ in range(E) :
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
    
mst_weight = kruskal(V, edges)
print(mst_weight)