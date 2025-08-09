# 11660번(구간 합 구하기 5) 문제 : https://www.acmicpc.net/problem/11660
import sys

input = sys.stdin.readline

# 굳이 ChatGPT 안 쓰고도 순수 코딩만으로 풀 수 있는 문제.

N, M = map(int, input().split())

# 피보나치 수열을 다이나믹 프로그래밍 알고리즘으로 구현하는 것에서 영감을 얻었습니다.
dp:list = [[0 for _ in range(N+1)] for _ in range(N+1)]

for row in range(1, N+1, 1) :
    IN:list = list(map(int, input().split()))
    for i in range(N) : # 누적 합 알고리즘 적용
        if i == 0 :
            continue
        elif i > 0 :
            IN[i] = IN[i] + IN[i-1]
    for col in range(1, N+1, 1) : # 누적 합 알고리즘 적용 + 다이나믹 프로그래밍 알고리즘 적용
        dp[row][col] = dp[row-1][col]+IN[col-1]

for i in range(M) :
    FIRST_ROW, FIRST_COL, LAST_ROW, LAST_COL = map(int, input().split())
    # 예시로 3 3 4 4로 입력했다고 가정한 경우
    # (0행 0열부터 4행 4열까지의 합)-(0행 0열부터 2행 4열까지의 합)-(0행 0열부터 4행 2열까지의 합)+(0행 0열부터 2행 2열까지의 합)=(3행 3열부터 4행 4열까지의 합)
    result = dp[LAST_ROW][LAST_COL] - dp[FIRST_ROW-1][LAST_COL] - dp[LAST_ROW][FIRST_COL-1] + dp[FIRST_ROW-1][FIRST_COL-1]
    print(result)