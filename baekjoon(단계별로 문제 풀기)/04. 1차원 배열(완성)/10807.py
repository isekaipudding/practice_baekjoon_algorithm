# 10807번(개수 세기) 문제 : https://www.acmicpc.net/problem/10807
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())
L:list = list(map(int, input().split()))
V:int = int(input().rstrip())

count:int = 0
if len(L) >= N :
    for num in L :
        if num == V :
            count += 1

print(count)