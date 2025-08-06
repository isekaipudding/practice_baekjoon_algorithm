# 18438번(LCS 5) 문제 : https://www.acmicpc.net/problem/18438
import sys

input = sys.stdin.readline

# 일종의 분할 정복 알고리즘인 히르쉬버그 알고리즘을 활용한 문제입니다.
# LCS 2 문제에서 제출한 소스 코드를 재활용합니다.
# C++ 소스 코드 대신 Python 소스 코드를 공유합니다.

def lcs_length(X: str, Y: str) -> list[int] :
    n, m = len(X), len(Y)
    previous:list[int] = [0] * (m+1)
    for i in range(1, n+1) :
        current:list[int] = [0] * (m+1)
        for j in range(1, m+1) :
            if X[i-1] == Y[j-1] :
                current[j] = previous[j-1] + 1
            else :
                current[j] = max(previous[j], current[j-1])
        previous = current
    return previous

def hirschberg(X: str, Y: str) -> str :
    n, m = len(X), len(Y)
    if n == 0 :
        return ""
    if n == 1 :
        return X if X in Y else ""
    
    index:int = n // 2
    X_left, X_right = X[:index], X[index:]

    LEFT:list[int] = lcs_length(X_left, Y)
    RIGHT:list[int] = lcs_length(X_right[::-1], Y[::-1])

    # Y를 split할 인덱스 k 결정
    k:int = max(range(m+1), key=lambda x: LEFT[x] + RIGHT[m-x])

    return hirschberg(X_left,  Y[:k]) + hirschberg(X_right, Y[k:])

A:str = input().rstrip()
B:str = input().rstrip()
lcs:str = hirschberg(A, B)
print(len(lcs))
print(lcs)