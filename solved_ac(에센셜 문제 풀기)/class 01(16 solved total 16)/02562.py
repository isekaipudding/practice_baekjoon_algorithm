# 2562번(최댓값) 문제 : https://www.acmicpc.net/problem/2562
import sys

input = sys.stdin.readline

max:int = 0
index:int = 1
for i in range(9) :
    number = int(input().rstrip())
    if number > max :
        max = number
        index = i+1
        
print(max)
print(index)