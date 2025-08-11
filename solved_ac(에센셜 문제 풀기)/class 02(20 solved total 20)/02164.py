# 2164번(카드2) 문제 : https://www.acmicpc.net/problem/2164
import sys

input = sys.stdin.readline

# N=1부터 N=32까지 일일히 계산한 후 규칙을 찾아서 공식으로 최적화했습니다.

N:int = int(input().rstrip())

if N == 1 :
    print(1)
elif N > 1 :
    K:int = -1
    TEMP = N - 1
    while TEMP > 0 :
        TEMP = TEMP >> 1 # 비트 마스크 알고리즘 사용
        K += 1
    print( 2 * ((N-1) % (2**K) + 1) )