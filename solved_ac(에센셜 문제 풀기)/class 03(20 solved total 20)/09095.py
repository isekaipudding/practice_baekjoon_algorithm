# 9095번(1, 2, 3, 더하기) 문제 : https://www.acmicpc.net/problem/9095
import sys

input = sys.stdin.readline

# 다이나믹 프로그래밍 알고리즘 문제는 귀납법으로 점화식 및 범위, 초기값 구하는 것이 중요합니다.

T:int = int(input().rstrip())

# 다이나믹 프로그래밍 알고리즘 사용
dp:list = [0 for _ in range(11)]

# 초기값
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11, 1) : # N의 범위는 4 이상의 정수입니다.
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] # 점화식
    
for i in range(T) :
    N:int = int(input().rstrip())
    print(dp[N])