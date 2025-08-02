# 2738번(행렬 덧셈) 문제 : https://www.acmicpc.net/problem/2738
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

Array2D = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N) :
    inputArray = list(map(int, input().split()))
    for j in range(M) :
        Array2D[i][j] = inputArray[j]
for i in range(N) :
    inputArray = list(map(int, input().split()))
    for j in range(M) :
        Array2D[i][j] += inputArray[j]
        
for i in range(N) :
    print(" ".join(map(str, Array2D[i])))