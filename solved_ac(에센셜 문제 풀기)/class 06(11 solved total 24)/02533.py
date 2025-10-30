# 2533번(사회망 서비스) 문제 : https://www.acmicpc.net/problem/2533
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

# 기존 dp와 다르게 트리 dp는 node를 index로 지정하여 각 node에 대한 데이터를 메모리에 저장하는 방식입니다.
def dfs(node) :
    # 해당 부모 노드를 방문 처리합니다.
    visited[node] = True
    # 트리 dp에서 초기값을 설정합니다.
    dp[node][1] = 1
    # 해당 노드의 자식 노드를 추출하여 dfs 방식으로 탐색합니다.
    for i in graph[node] :
        # 아직 방문하지 않는 노드가 있다면 더 깊이 탐색합니다.
        if not visited[i] :
            dfs(i)
            # 이건 점화식입니다. 깊은 탐색이 끝나면 점화식을 적용합니다.
            dp[node][1] += min(dp[i][0], dp[i][1])
            dp[node][0] += dp[i][1]
            
N:int = int(input().rstrip())
# 무방향 가중치 없는 인접 리스트로 합니다.
graph:list = [[] for _ in range(N+1)]
for i in range(N-1) :
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited:list = [False for _ in range(N+1)]
dp:list = [[0, 0] for _ in range(N+1) ]

# 탐색을 시작합니다. 이 때 루트 노드는 1번 노드입니다.
dfs(1)

# 1번 노드의 데이터 중 최소값을 추출하여 출력합니다.
print(min(dp[1][0], dp[1][1]))