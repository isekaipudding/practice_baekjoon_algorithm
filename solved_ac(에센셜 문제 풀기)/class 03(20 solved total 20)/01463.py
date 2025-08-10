# 1463번(1로 만들기) 문제 : https://www.acmicpc.net/problem/1463
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())

# 다이나믹 프로그래밍 알고리즘 사용
dp:list = [0 for _ in range(N+1)]
# 초기값 설정
dp[0] = 0
dp[1] = 0

for i in range(2, N+1, 1) :
    dp[i] = dp[i-1] + 1 # 점화식 1
    
    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i//2] + 1) # 점화식 2
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3] + 1) # 점화식 3
        
print(dp[N])