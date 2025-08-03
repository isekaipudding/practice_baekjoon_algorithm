# 2869번(달팽이는 올라가고 싶다) 문제 : https://www.acmicpc.net/problem/2869
import sys
import math

input = sys.stdin.readline

numbers = list(map(int, input().split()))
climb:int = numbers[0]
slip:int = numbers[1]
height:int = numbers[2]
day:int = 1
if climb >= height :
    day = 1
else :
    day = 1 + math.ceil((height-climb) / (climb-slip))
print(day)