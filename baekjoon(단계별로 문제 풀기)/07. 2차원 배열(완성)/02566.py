# 2566번(최댓값) 문제 : https://www.acmicpc.net/problem/2566
import sys

input = sys.stdin.readline

Array2D = [[0 for _ in range(9)] for _ in range(9)]

max_value = 0
max_i = 1
max_j = 1
for i in range(9) :
    string = list(map(int,input().split()))
    for j in range(9) :
        Array2D[i][j] = string[j]
        if max_value < Array2D[i][j] :
            max_value = Array2D[i][j]
            max_i = i + 1
            max_j = j + 1
            
print(max_value)
print("{} {}".format(max_i, max_j))