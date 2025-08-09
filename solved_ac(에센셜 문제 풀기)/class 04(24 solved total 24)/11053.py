# 11053번(가장 긴 증가하는 부분 수열) 문제 : https://www.acmicpc.net/problem/11053
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())
numbers:list = list(map(int, input().split()))

# 다이나믹 프로그래밍 알고리즘 사용
dp:list = [0 for _ in range(N)]
dp[0] = 1 # 초기식

for i in range(N) :
    # 점화식
    TEMP:int = 0
    for j in range(i) :
        if numbers[j] < numbers[i] :
            if dp[j] > TEMP :
                TEMP = dp[j]
    dp[i] = TEMP + 1

print(max(dp))