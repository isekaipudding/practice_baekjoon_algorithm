# 2623번(음악프로그램) : https://www.acmicpc.net/problem/2623
import sys
import heapq

input = sys.stdin.readline

def bfs() :
    result:list = []
    queue:list = []

    for i in range(1, N+1) :
        if in_degree[i] == 0 :
            heapq.heappush(queue, -i)  # 큰 번호 먼저 넣기 (max-heap)

    while queue :
        current = -heapq.heappop(queue)
        result.append(current)

        for next_node in graph[current] :
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0 :
                heapq.heappush(queue, -next_node)

    if len(result) == N :
        print(*result, sep='\n')
    else:
        print(0)

N, M = map(int, input().split())
graph:list = [[] for _ in range(N+1)]
in_degree:list = [0 for _ in range(N+1)]

for _ in range(M) :
    query:list = list(map(int, input().split()))
    count:int = query[0]
    for i in range(1, count):
        a:int = query[i]
        b:int = query[i+1]
        graph[a].append(b)
        in_degree[b] += 1

bfs()