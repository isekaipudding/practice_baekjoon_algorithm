# 2150번(Strongly Connected Component) 문제 : https://www.acmicpc.net/problem/2150
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

# 이 문제를 해결하기 위해 코사라주 알고리즘을 사용했습니다.
# 출처 : https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm

# 후위 순회 방식으로 스택에 저장합니다.
def dfs1(u) -> None :
    visited[u] = True
    for v in graph[u] :
        if not visited[v] :
            dfs1(v)
    order.append(u)

# 역그래프에서 하나의 SCC를 추출합니다.
def dfs2(u, component) -> None :
    visited[u] = True
    component.append(u)
    for v in reverse_graph[u] :
        if not visited[v] :
            dfs2(v, component)

# 1. 입력 및 인접 리스트 구성
nodes, edges = map(int, input().split())
graph:list = [[] for _ in range(nodes+1)]
reverse_graph:list = [[] for _ in range(nodes+1)]

for _ in range(edges) :
    u, v = map(int, input().split())
    graph[u].append(v)
    reverse_graph[v].append(u)

# 2. 1차 DFS -> 종료 순서 수집
visited:list = [False for _ in range(nodes+1)]
order:list = []
for i in range(1, nodes+1):
    if not visited[i]:
        dfs1(i)

# 3. 2차 DFS -> 역그래프에서 SCC 추출
visited:list = [False for _ in range(nodes+1)]
sccs:list = []
for u in reversed(order) :
    if not visited[u] :
        component:list = []
        dfs2(u, component)
        component.sort()
        sccs.append(component)

# 4. SCC 그룹 정렬 그리고 출력
sccs.sort(key=lambda x: x[0])
print(len(sccs))
for L in sccs :
    print(*L, end=' ');print(-1)