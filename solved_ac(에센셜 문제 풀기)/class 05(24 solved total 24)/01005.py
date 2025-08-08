# 1005번(ACM Craft) 문제 : https://www.acmicpc.net/problem/1005
import sys
from collections import deque

input = sys.stdin.readline

T:int = int(input().rstrip())

def bfs(dp, queue, graph, count, cost, end) :
    while queue :
        child:int = queue.popleft()
        for neighbor in graph[child] :
            count[neighbor] -= 1
            dp[neighbor] = max(dp[neighbor], dp[child] + cost[neighbor])
            if count[neighbor] == 0 :
                queue.append(neighbor)
        
        # 출력
        if count[end] == 0 :
            print(dp[end])
            break

for _ in range(T) :
    N, K = map(int,input().split())
    cost:list = [0] + list(map(int,input().split()))
    graph:list[list[int]] = [[] for _ in range(N+1)]
    count:list = [0 for _ in range(N+1)]
    count[0] = -1
    # 그래프 정보 삽입
    for _ in range(K) :
        u, v = map(int, input().split())
        graph[u].append(v)
        count[v] += 1
    end:int = int(input().rstrip())

    # 메모리 설정
    dp:list = [0 for _ in range(N+1)]
    queue = deque()
    for i in range(1, N+1) :
        if count[i] == 0 :
            queue.append(i)
            dp[i] = cost[i]
    
    bfs(dp, queue, graph, count, cost, end)