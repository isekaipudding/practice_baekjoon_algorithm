# 10810번(공 넣기) 문제 : https://www.acmicpc.net/problem/10810
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
ball_backet:list = [0 for _ in range(N)]

for i in range(M) :
    A, B, C = map(int, input().split())
    for j in range(A-1, B) :
        ball_backet[j] = C
        
print(" ".join(map(str, ball_backet)))