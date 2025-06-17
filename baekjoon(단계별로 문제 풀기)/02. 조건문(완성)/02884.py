# 2884번(알람 시계) 문제 : https://www.acmicpc.net/problem/2884
import sys

input =sys.stdin.readline

hour, minute = map(int, input().split())

if minute < 45 :
    hour -= 1
    minute += 15
    if hour < 0 :
        hour = 23
else :
    minute -= 45
    
print("{} {}".format(hour, minute))