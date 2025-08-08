# 1562번(계단 수) : https://www.acmicpc.net/problem/1562
import sys

input = sys.stdin.readline

MOD:int = 1000000000

dp:list = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(100 + 1)]

for i in range(1, 10, 1) :
    dp[1][i][1 << i] = 1

N:int = int(input().rstrip())

for i in range(2, N+1, 1) :
    for j in range(10) :
        for k in range(1 << 10) :
            if j > 0 :
                dp[i][j][k | (1 << j)] += dp[i-1][j-1][k]
            if j < 9 :
                dp[i][j][k | (1 << j)] += dp[i-1][j+1][k]

result:int = 0
for i in range(10) :
    result += dp[N][i][1023]
    
print(result % MOD)