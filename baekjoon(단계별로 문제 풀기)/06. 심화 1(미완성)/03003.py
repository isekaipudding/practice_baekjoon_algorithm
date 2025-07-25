# 3003번(킹, 퀸, 룩, 비숍, 나이트, 폰) 문제 : https://www.acmicpc.net/problem/3003
import sys

input = sys.stdin.readline

chess:list = [1, 1, 2, 2, 2, 8]
change:list = list(map(int, input().split()))
result:list = [0, 0, 0, 0, 0, 0]
for i in range(6) :
    result[i] = chess[i] - change[i]
    
print(" ".join(map(str, result)))