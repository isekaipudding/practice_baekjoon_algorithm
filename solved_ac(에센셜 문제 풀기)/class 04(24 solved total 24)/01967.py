# 1967번(트리의 지름) 문제 : https://www.acmicpc.net/problem/1967
import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

# 정말 익숙한 dfs 알고리즘
def dfs(node, graph, visited) :
    visited[node] = True
    farthest_node = node
    max_distance = 0

    for neighbor, weight in graph[node].items() :
        if not visited[neighbor] :
            distance, far_node = dfs(neighbor, graph, visited)
            distance += weight
            if distance > max_distance:
                max_distance = distance
                farthest_node = far_node

    return max_distance, farthest_node

def find_tree_diameter(N, edges):
    # 그래프 초기화
    graph = [dict() for _ in range(N + 1)]

    # 간선 정보 추가
    for u, v, w in edges:
        graph[u][v] = w
        graph[v][u] = w

    # 첫 번째 DFS로 가장 먼 노드 찾기
    visited = [False for _ in range(N+1)]
    _, farthest_node = dfs(1, graph, visited) # 첫번째 값은 필요 없으므로 _ 표시

    # 두 번째 DFS로 트리의 지름 구하기
    visited = [False for _ in range(N+1)]
    diameter, _ = dfs(farthest_node, graph, visited)

    return diameter

# 노드의 개수 입력 받기
N = int(input().rstrip())

# 간선정보 입력 받기
edges = []
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

# 트리의 지름 계산
diameter = find_tree_diameter(N, edges)
print(diameter)