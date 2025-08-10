# 1003번(피보나치 함수) 문제 : https://www.acmicpc.net/problem/1003
import sys

input = sys.stdin.readline

# 다이나믹 프로그래밍 알고리즘 사용
dp:list = [0 for _ in range(41)]
dp[1] = 1

for i in range(2, 41, 1) :
    dp[i] = dp[i-1] + dp[i-2] # 점화식

T:int = int(input().rstrip())
N:int = 0

for i in range(T) :
    N = int(input().rstrip())
    if N == 0 :
        print("{} {}".format(1, dp[0]))
    elif 1 <= N and N <= 40 :
        print("{} {}".format(dp[N-1], dp[N]))