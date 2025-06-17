# 10813번(공 바꾸기) 문제 : https://www.acmicpc.net/problem/10813
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

number:list = [0 for _ in range(N)]

for i in range(N) :
    number[i] = i + 1
    
for i in range(M) :
    A, B = map(int, input().split())
    temp = number[A-1]
    number[A-1] = number[B-1]
    number[B-1] = temp
    
print(" ".join(map(str, number)))