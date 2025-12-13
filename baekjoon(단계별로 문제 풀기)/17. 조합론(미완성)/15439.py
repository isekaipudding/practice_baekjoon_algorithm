# 15439번(베라의 패션) 문제 : https://www.acmicpc.net/problem/15439
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())
print(N * (N-1))