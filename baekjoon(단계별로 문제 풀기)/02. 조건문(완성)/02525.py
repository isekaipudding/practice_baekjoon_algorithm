# 2525번(오븐 시계) 문제 : https://www.acmicpc.net/problem/2525
import sys

input = sys.stdin.readline

hour, minute = map(int, input().split())
even:int = int(input().rstrip()) # 고기가 even하게 익지 않았어요.

minute += even % 60

if minute >= 60 :
    hour += 1
    minute -= 60
    
hour += even // 60
hour %= 24

print("{} {}".format(hour, minute))