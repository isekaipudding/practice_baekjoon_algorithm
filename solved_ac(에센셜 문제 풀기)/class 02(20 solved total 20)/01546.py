# 1546번(평균) 문제 : https://www.acmicpc.net/problem/1546
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())

number:list = list(map(int, input().split()))
    
print(sum(number)*100 / (max(number)*N))