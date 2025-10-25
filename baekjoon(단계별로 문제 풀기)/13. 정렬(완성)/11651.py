# 11651번(좌표 정렬하기 2) 문제 : https://www.acmicpc.net/problem/11651
import sys

input = sys.stdin.readline

# 11650번 문제(좌표 정렬하기)와 완전히 같은 유형입니다!

N:int = int(input().rstrip())
L:list = []

for i in range(N) :
    x, y = map(int, input().split())
    L.append([x, y])
    
L.sort(key = lambda x : (x[1], x[0])) # 여기서 x[0], x[1] 위치만 바꾸면 끝!

for i in range(N) :
    print("{} {}".format(L[i][0], L[i][1]))