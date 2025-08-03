# 2563번(색종이) 문제 : https://www.acmicpc.net/problem/2563
import sys

input = sys.stdin.readline

Array2D = [[False for _ in range(100)] for _ in range(100)]

T:int = int(input().rstrip())
Area:int = 0
for i in range(T) :
    N, M = map(int, input().split())
    for j in range(N, N+10) :
        for k in range(M, M+10) :
            if Array2D[j][k] == False :
                Area += 1
            Array2D[j][k] = True

print(Area)