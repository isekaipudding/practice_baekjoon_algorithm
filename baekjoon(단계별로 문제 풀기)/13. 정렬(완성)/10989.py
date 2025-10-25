# 10989번(수 정렬하기 3) 문제 : https://www.acmicpc.net/problem/10989
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())
count:list = [0 for _ in range(10001)]

for i in range(N) :
    number:int = int(input().rstrip())
    count[number] += 1

for i in range(1, 10001, 1) :
    for j in range(0, count[i], 1) :
        print(i)