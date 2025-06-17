# 10811번(바구니 뒤집기) 문제 : https://www.acmicpc.net/problem/10811
import sys
import math

input = sys.stdin.readline

N, M = map(int, input().split())

bucket:list = [0 for _ in range(N)]
for i in range(N) :
    bucket[i] = i + 1

#시간 복잡도 O(n*m)
for a in range(M) :
    i, j = map(int, input().split())
    for b in range(0, math.ceil((j-i)/2), 1) : #절반만 검사하여 경과 시간을 1/2 감소
        #밑의 3줄은 두 수의 위치를 변환하는 알고리즘
        temp:int = bucket[i-1+b]
        bucket[i-1+b] = bucket[j-1-b]
        bucket[j-1-b] = temp
        
print(" ".join(map(str,bucket)))