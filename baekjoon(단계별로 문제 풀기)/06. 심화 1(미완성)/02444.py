# 2444번(별 찍기 - 7) 문제 : https://www.acmicpc.net/problem/2444
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())

for i in range(N-1, 0, -1) :
    print(" " * i + "*" * (2*N - 1 - 2*i))
for i in range(N) :
    print(" " * i + "*" * (2*N - 1 - 2*i))