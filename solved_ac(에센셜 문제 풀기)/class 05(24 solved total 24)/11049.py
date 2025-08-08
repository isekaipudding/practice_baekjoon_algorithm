# 11049번(행렬 곱셈 순서) 문제 : https://www.acmicpc.net/problem/11049
import sys

input = sys.stdin.readline

def build() :
    for i in range(N) :
        row, col = map(int, input().split())
        if i == 0 :
            row_col.append(row)
        row_col.append(col)

    for i in range(N+1) :
        dp[i][i] = 0

N:int = int(input().rstrip())

row_col:list = []
# 초기식(문제 조건에서 "정답은 2^31-1 보다 작거나 같은 자연수이다."에 의해 2 ** 31 - 1로 설정)
dp:list = [[2 ** 31 - 1 for _ in range(N+1)] for _ in range(N+1)]

build() # dp 배열 생성

# 점화식
for i in range(1, N) :
    for j in range(1, N + 1 - i) :
        MIN:int = 2 ** 31 - 1
        for k in range(i) :
            # 여기에 점화식을 적용합니다.
            MIN = min(MIN, dp[j][j+k] + dp[j+k+1][j+i] + row_col[j-1] * row_col[i+j] * row_col[j+k])
        dp[j][j+i] = MIN

print(dp[1][N])