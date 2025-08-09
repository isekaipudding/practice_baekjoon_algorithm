# 11725번(트리의 부모 찾기) 문제 : https://www.acmicpc.net/problem/11725
from collections import deque
import sys

input = sys.stdin.readline

# 너비 우선 탐색 알고리즘 사용
def bfs(root) :
    queue = deque()
    queue.append(root)
    while queue :
        root = queue.popleft() # 부모 노드를 추출합니다.
        for i in range(len(graph[root])) : # 인접 리스트에서 원소를 추출하는 방법
            if visited[graph[root][i]] == 0 : # 만약 자식 노드의 부모 노드가 아직 설정되지 않았다면
                queue.append(graph[root][i]) # 자식 노드를 큐에 저장하고
                visited[graph[root][i]] = root # 해당 노드의 부모 노드 정보를 저장합니다.

N:int = int(input().rstrip())

# 노드의 최대 개수가 많아서 인접 리스트 사용
graph:list = [[] for _ in range(N+1)]

for i in range(N-1) :
    u, v = map(int, input().split())
    # 무방향 가중치 없는 인접 리스트이므로 저장을 아래와 같이 합니다.
    graph[u].append(v)
    graph[v].append(u)
    
# 원활한 탐색을 위해 각 리스트마다 오름차순으로 정렬합니다.
for i in range(N+1) :
    graph[i].sort()

visited:list = [0 for _ in range(N+1)] # 이게 제일 중요합니다.
root:int = 1 # 루트 노드 설정
bfs(root)

# 출력 형식에 맞게 출력
for i in range(2, N+1, 1) :
    print(visited[i])