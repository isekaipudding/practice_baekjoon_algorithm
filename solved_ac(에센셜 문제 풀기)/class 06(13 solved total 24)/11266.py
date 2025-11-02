# 11266번(단절점) 문제 : https://www.acmicpc.net/problem/11266
import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

V, E = map(int, input().split())

# 각 간선에 id를 부여하여 (이전 간선 하나만) 정확히 건너뛰기
graph:list = [[] for _ in range(V + 1)]
for eid in range(1, E + 1) :
    u, v = map(int, input().split())
    graph[u].append((v, eid))
    graph[v].append((u, eid))

disc:list   = [0 for _ in range(V + 1)]  # 발견 시각(DFS order)
low:list    = [0 for _  in range(V + 1)] # 역방향/자손 통해 올라갈 수 있는 가장 빠른 발견 시각
is_art:list = [False for _ in range(V + 1)]
timer:list  = [0]

def dfs(u:int, parent_edge_id:int) :
    timer[0] += 1
    disc[u] = low[u] = timer[0]
    child_count = 0

    for v, eid in graph[u] :
        if eid == parent_edge_id :
            continue # 트리 간선(부모로 가는 그 간선) 한 개만 건너뜀

        if disc[v] == 0 : # 트리 간선
            child_count += 1
            dfs(v, eid)
            low[u] = min(low[u], low[v])

            # 루트가 아니고, 자식 서브트리가 u 이상으로 못 올라오면 u는 단절점
            if parent_edge_id != 0 and low[v] >= disc[u] :
                is_art[u] = True
        else :
            # 방문된 정점 → 역방향 간선
            low[u] = min(low[u], disc[v])

    # 루트 정점은 자식이 2개 이상이면 단절점
    if parent_edge_id == 0 and child_count >= 2 :
        is_art[u] = True

# 비연결 그래프 대비 : 모든 정점에서 시작
for u in range(1, V + 1) :
    if disc[u] == 0 :
        dfs(u, 0)

result:list = [i for i in range(1, V + 1) if is_art[i]]
result.sort()

print(len(result))
if result :
    print(*result)