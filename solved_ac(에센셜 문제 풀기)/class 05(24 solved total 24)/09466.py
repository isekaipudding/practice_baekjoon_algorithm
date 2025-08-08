# 9466번(텀 프로젝트) : https://www.acmicpc.net/problem/9466
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(u) :
    """
    u에서 출발해 다음 학생 v=L[u]를 따라가며 DFS.
    - 만약 v가 아직 방문되지 않았다면 dfs(v)
    - 이미 방문되었지만 아직 done[v]==False라면 사이클을 찾은 것!
      사이클 내 모든 정점을 순회하며 count 증가
    탐색이 끝나면 done[u]=True로 표시하여,
    이후 이 정점(u)는 다시 사이클 카운트에 포함되지 않도록 합니다.
    """
    global cycle_size
    visited[u] = True
    v = L[u]
    if not visited[v] :
        dfs(v)
    else:
        # v를 이미 방문했는데, 아직 처리(done) 전이라면 사이클 발생 지점
        if not done[v] :
            w = v
            while True:
                cycle_size += 1
                w = L[w]
                if w == v :
                    break
    done[u] = True

T:int = int(input().rstrip())
for _ in range(T):
    N:int = int(input().rstrip())
    # 1-index 편의를 위해 앞에 0을 붙임
    L:list = [0] + list(map(int, input().split()))

    visited:list = [False for _ in range(N+1)]
    done:list = [False for _ in range(N+1)]
    cycle_size:int = 0 # 사이클에 속한 학생 수

    # 모든 정점에 대해 DFS 수행
    for i in range(1, N + 1) :
        if not visited[i] :
            dfs(i)

    # 팀(사이클)에 속하지 않은 학생 수 = 전체 N - 사이클에 속한 학생 수
    print(N - cycle_size)