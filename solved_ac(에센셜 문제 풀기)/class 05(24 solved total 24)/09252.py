# 9252번(LCS 2) 문제 : https://www.acmicpc.net/problem/9252
import sys

input = sys.stdin.readline

def longest_common_subsequence(A: str, B: str) -> tuple[int, str] :
    n, m = len(A), len(B)
    # 1) DP 테이블 채우기 (길이 계산)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1) :
        for j in range(1, m + 1) :
            if A[i-1] == B[j-1] :
                dp[i][j] = dp[i-1][j-1] + 1
            else :
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # 2) 역추적(back‐tracking)으로 실제 LCS 문자열 복원
    lcs_chars = []
    i, j = n, m
    while i > 0 and j > 0 :
        if A[i-1] == B[j-1] :
            # 매칭된 문자
            lcs_chars.append(A[i-1])
            i -= 1
            j -= 1
        else :
            # 더 큰 쪽으로 이동
            if dp[i-1][j] > dp[i][j-1] :
                i -= 1
            else:
                j -= 1
    lcs_chars.reverse()
    
    return dp[n][m], ''.join(lcs_chars)

A:str = input().rstrip()
B:str = input().rstrip()
length, lcs_str = longest_common_subsequence(A, B)
print(length)
print(lcs_str)