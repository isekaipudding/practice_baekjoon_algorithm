# 8393번(합) 문제 : https://www.acmicpc.net/problem/8393
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())

print(N * (N+1) // 2) # 공식을 활용해서 해결합니다.