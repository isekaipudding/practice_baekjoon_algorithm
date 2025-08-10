# 11726번(2xn 타일링) 문제 : https://www.acmicpc.net/problem/11726
import sys

input = sys.stdin.readline

X:int = int(input().rstrip())

dp = [0 for _ in range(1001)]

# 초기값 설정
dp[0] = 1
dp[1] = 1

if X > 1 : 
    # 이 문제를 노가다하면 피보나치 수열인 것을 알 수 있습니다.
    # 다이나믹 프로그래밍 알고리즘 사용
    for i in range(2, X+1) :
        dp[i] = (dp[i-1] + dp[i-2]) % 10007 # 미리 10007 나머지를 구해서 dp에 적용합니다.
        
print(dp[X])