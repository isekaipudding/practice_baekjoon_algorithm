# 2750번(수 정렬하기) 문제 : https://www.acmicpc.net/problem/2750
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())

number:list = []
for i in range(N) :
    num:int = int(input().rstrip())
    number.append(num)
    
number.sort()
for i in range(len(number)) :
    print(number[i])