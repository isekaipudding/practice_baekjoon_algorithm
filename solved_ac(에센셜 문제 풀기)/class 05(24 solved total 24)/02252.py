# 2252번(줄 세우기) : https://www.acmicpc.net/problem/2252
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def topological_sort(N, edges) :
    graph:dict = defaultdict(list)
    indegree:dict = defaultdict(int)

    # 그래프 구성 및 진입 차수 계산
    for A, B in edges :
        graph[A].append(B)
        indegree[B] += 1

    # 모든 노드에 대해 진입 차수가 없으면 0으로 초기화
    for i in range(1, N + 1) :
        indegree.setdefault(i, 0)

    # 진입 차수가 0인 노드 큐에 삽입
    queue = deque()
    for node in range(1, N + 1) :
        if indegree[node] == 0 :
            queue.append(node)

    result:list = []
    while queue :
        current:int = queue.popleft()
        result.append(current)
        for neighbor in graph[current] :
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0 :
                queue.append(neighbor)

    # 사이클 검출
    if len(result) != N :
        raise ValueError("Cycle detected, not a DAG")

    return result

# 입력 처리
N, M = map(int, input().split())
edges:list = []
for _ in range(M) :
    A, B = map(int, input().split())
    edges.append((A, B))

# 위상 정렬 수행
sorted_order = topological_sort(N, edges)
print(*sorted_order)