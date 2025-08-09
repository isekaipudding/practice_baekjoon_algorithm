# 12865번(평범한 배낭) 문제 : https://www.acmicpc.net/problem/12865
import sys

input = sys.stdin.readline

# 입력 받기
N, K = map(int, input().split())

# 물품 정보를 저장할 리스트
items = []

# 각 물품 정보 입력 받기
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

# 다차원 리스트 dp를 생성하여 값 초기화
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

# 다이나믹 프로그래밍 수행
for i in range(1, N + 1):
    for w in range(1, K + 1):
        weight, value = items[i - 1]
        if weight > w:  # 해당 물품을 배낭에 넣을 수 없는 경우
            dp[i][w] = dp[i-1][w]
        else:  # 해당 물품을 배낭에 넣을 수 있는 경우
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)

# 배낭에 넣을 수 있는 물건들의 가치합의 최댓값 출력
print(dp[N][K])