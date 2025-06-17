# 2753번(윤년) 문제 : https://www.acmicpc.net/problem/2753
import sys

input = sys.stdin.readline

year:int = int(input().rstrip())

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) :
    print("1")
else :
    print("0")