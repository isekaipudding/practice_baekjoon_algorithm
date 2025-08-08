# 10942번(팰린드롬?) 문제 : https://www.acmicpc.net/problem/10942
import sys
from collections import deque

input = sys.stdin.readline

N:int = int(input().rstrip())
L:list = list(map(int, input().split()))
M:int = int(input().rstrip())
queue = deque()
for _ in range(M) :
    start, end = map(int, input().split())
    queue.append((start, end))

dp:list = [[0] * (N) for _ in range(N)]

# 1. 길이 1짜리 팰린드롬
for i in range(N) :
    dp[i][i] = 1

# 2. 길이 2짜리 팰린드롬
for i in range(N-1) :
    if L[i] == L[i+1] :
        dp[i][i+1] = 1

# 3. 길이 3 이상 팰린드롬
# length = 검사할 구간의 길이
for length in range(3, N+1) :
    for start in range(0, N - length + 1) :
        end:int = start + length - 1
        # 양 끝이 같고, 안쪽 구간이 팰린드롬이면
        if L[start] == L[end] and dp[start+1][end-1] == 1 :
            dp[start][end] = 1

# 4. 질의에 답하기
# queue에 (1-based start, end)가 들어 있으므로
for s, e in queue :
    start:int = s - 1
    end:int = e - 1
    print(dp[start][end])