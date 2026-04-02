# 2618번(경찰차) 문제 : https://www.acmicpc.net/problem/2618
import sys

sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

# 뭐 이렇게 어려움?ㄷㄷ

def manhattan_distance(a, b) :
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def dfs1(index1, index2) :
    next_case:int = max(index1, index2) + 1
    
    if next_case > W :
        return 0
    
    if dp[index1][index2] != -1 :
        return dp[index1][index2]

    distance1:int = manhattan_distance(police1[index1], L[next_case]) + dfs1(next_case, index2)
    distance2:int = manhattan_distance(police2[index2], L[next_case]) + dfs1(index1, next_case)
    
    dp[index1][index2] = min(distance1, distance2)
    return dp[index1][index2]
    
def dfs2(index1, index2) :
    next_case:int = max(index1, index2) + 1
    
    if next_case > W :
        return
    
    distance1:int = manhattan_distance(police1[index1], L[next_case]) + dfs1(next_case, index2)
    distance2:int = manhattan_distance(police2[index2], L[next_case]) + dfs1(index1, next_case)
    
    if distance1 < distance2 :
        print(1)
        dfs2(next_case, index2)
    else :
        print(2)
        dfs2(index1, next_case)
    
N:int = int(input().rstrip())
W:int = int(input().rstrip())
L:list = [[0, 0]] + [list(map(int, input().split())) for _ in range(W)]

police1:list = [[1, 1]] + L[1:]
police2:list = [[N, N]] + L[1:]

dp:list = [[-1 for _ in range(W + 1)] for _ in range(W + 1)]

print(dfs1(0, 0))
dfs2(0, 0)