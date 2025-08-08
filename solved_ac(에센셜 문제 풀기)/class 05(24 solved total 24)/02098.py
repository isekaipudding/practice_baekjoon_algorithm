# 2098번(외판원 순회) 문제 : https://www.acmicpc.net/problem/2098
import sys
sys.setrecursionlimit(10 ** 4)

input = sys.stdin.readline

def dfs(current, visited) :
    if visited == (1 << N) - 1 : # 모두 방문했을 때
        return graph[current][0] if graph[current][0] else INF

    if dp[current][visited] != -1 :
        return dp[current][visited]

    MIN:int = INF
    for i in range(N) :
        if not visited & (1 << i) and graph[current][i] != 0 :
            cost = dfs(i, visited | (1 << i)) + graph[current][i]
            MIN = min(MIN, cost)

    dp[current][visited] = MIN
    return MIN

N:int = int(input().rstrip())
graph:list = [list(map(int, input().split())) for _ in range(N)]

INF:int = 10 ** 9
dp:list = [[-1] * (1 << N) for _ in range(N)]

print(dfs(0, 1))