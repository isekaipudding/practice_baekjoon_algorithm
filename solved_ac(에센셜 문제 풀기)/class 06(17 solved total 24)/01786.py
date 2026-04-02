# 1786번(찾기) 문제 : https://www.acmicpc.net/problem/1786
import sys

input = sys.stdin.readline

def compute_lps(pattern: str) -> list[int] :
    n:int = len(pattern)
    lps:list = [0 for _  in range(n+1)]
    length:int = 0
    i:int = 1
    while i < n :
        if pattern[i] == pattern[length] :
            length += 1
            lps[i] = length
            i += 1
        else :
            if length != 0 :
                length = lps[length - 1]
            else :
                lps[i] = 0
                i += 1
    return lps

def kmp_find_all(text: str, pattern: str) -> list[int] :
    lps:list = compute_lps(pattern)
    result:list = []
    i = j = 0
    N, M = len(text), len(pattern)
    while i < N :
        if text[i] == pattern[j] :
            i += 1
            j += 1
            if j == M :
                # match at text[i-M .. i-1], 1-indexed 시작 위치 = (i-M)+1
                result.append(i - M + 1)
                j = lps[j - 1]
        else :
            if j != 0 :
                j = lps[j - 1]
            else :
                i += 1
    return result

T:str = input().rstrip()
P:str = input().rstrip()

positions:list = kmp_find_all(T, P)
print(len(positions))
if positions :
    print(*positions)