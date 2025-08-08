# 1106번(호텔) 문제 : https://www.acmicpc.net/problem/1106
import sys

input = sys.stdin.readline

C, N = map(int, input().split())
cities:list = [tuple(map(int, input().split())) for _ in range(N)]

MAX:int = C + 100  # 여유 있게 공간 확보
dp:list = [float('inf') for _ in range(MAX + 1)]
# 초기식
dp[0] = 0

for cost, customer in cities :
    for i in range(customer, MAX + 1) :
        # 점화식
        dp[i] = min(dp[i], dp[i - customer] + cost)

# C 이상을 만족하는 최소 비용
print(min(dp[C:]))