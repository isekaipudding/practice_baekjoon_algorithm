# 11400번(단절선) 문제 : https://www.acmicpc.net/problem/11400
import sys
sys.setrecursionlimit(1 << 20)

input = sys.stdin.readline

V, E = map(int, input().split())
graph:list = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

disc:list    = [0 for _ in range(V + 1)] # discovery time (DFS order)
low:list     = [0 for _ in range(V + 1)]
time:int     = 0
bridges:list = []

def dfs(u:int, parent:int) :
    global time
    time += 1
    disc[u] = low[u] = time

    for v in graph[u] :
        if v == parent :
            continue
        if disc[v] == 0 :
            dfs(v, u)
            low[u] = min(low[u], low[v])
            # u-v가 트리 간선이고, v의 서브트리가 u 이상으로 못 올라오면 단절선
            if low[v] > disc[u] :
                if u < v:
                    bridges.append((u, v))
                else :
                    bridges.append((v, u))
        else :
            # 역방향 간선
            low[u] = min(low[u], disc[v])

# 문제는 연결 그래프이지만, 안전하게 전 정점 시도
for i in range(1, V + 1):
    if disc[i] == 0 :
        dfs(i, 0)

bridges.sort() # 사전순(A, B) 정렬
print(len(bridges))
for a, b in bridges:
    print(f"{a} {b}")