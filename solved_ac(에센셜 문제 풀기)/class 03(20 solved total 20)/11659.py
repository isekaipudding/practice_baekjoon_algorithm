# 11659번(구간 합 구하기 4) 문제 : https://www.acmicpc.net/problem/11659
import sys

input = sys.stdin.readline

# 원래 누적 합 리스트는 prefix로 하는 것이 정석이나
# 다이나믹 프로그래밍 알고리즘으로부터 누적 합 알고리즘으로 유도되는 것을 알기 위해
# 일부러 dp로 변경했습니다. 저는 누적 합 리스트를 prefix로 하는 것을 선호합니다.

N, M = map(int, input().split())
L:list = list(map(int, input().split()))

# 다이나믹 프로그래밍 알고리즘 사용
dp:list = [0 for _ in range(N+1)]
dp[0] = 0 # 초기값

for i in range(1, N+1, 1) : # 범위 : N >= 1
    dp[i] = dp[i-1] + L[i-1] # 점화식
    
# 여기서 dp 대신 prefix로 변경하면 누적 합 알고리즘으로 탈바꿈하게 됩니다!

for i in range(M) :
    a, b = map(int, input().split())
    print(dp[b] - dp[a-1])