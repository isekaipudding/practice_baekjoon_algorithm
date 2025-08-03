# 1193번(분수찾기) 문제 : https://www.acmicpc.net/problem/1193
import sys
import math

input = sys.stdin.readline

X:int = int(input().strip())

# n(n+1)/2 = x에서 n의 해를 구한 뒤 ceil()을 적용합니다.
N = math.ceil(0.5*(math.sqrt(8*X-1)-1))

sum:int = int(N*(N+1)/2)

# numerator : 분자, denominator : 분모
if N%2 == 0 :
    numerator:int = N - (sum-X)
    denominator:int = 1 + (sum-X)
    print("{}/{}".format(numerator, denominator))
else :
    numerator:int = 1 + (sum-X)
    denominator:int = N - (sum-X)
    print("{}/{}".format(numerator, denominator))