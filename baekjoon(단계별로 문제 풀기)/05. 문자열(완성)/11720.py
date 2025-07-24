# 11720번(숫자의 합) 문제 : https://www.acmicpc.net/problem/11720
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())
number:str = input().rstrip()

sum:int = 0
for i in range(N) :
    sum += int(number[i])
    
print(sum)