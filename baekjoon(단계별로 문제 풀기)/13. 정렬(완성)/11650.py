# 11650번(좌표 정렬하기) : https://www.acmicpc.net/problem/11650
import sys

input = sys.stdin.readline

# (10814번 나이순 정렬)와 동일한 유형의 정렬 알고리즘 문제입니다.

N:int = int(input().rstrip())
L:list = []

for i in range(N) :
    x, y = map(int, input().split())
    L.append([x, y])
    
L.sort(key = lambda x : (x[0], x[1]))

for i in range(N) :
    print("{} {}".format(L[i][0], L[i][1]))