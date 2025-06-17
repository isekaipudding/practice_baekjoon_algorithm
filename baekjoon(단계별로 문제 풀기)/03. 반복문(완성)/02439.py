# 2439번(별 찍기 - 2) 문제 : https://www.acmicpc.net/problem/2439
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())

blank:str = ""
star:str = ""

for i in range(N) :
    blank += " "

for i in range(N) :
    temp:list = list(blank)
    temp.remove(' ')
    blank = ''.join(temp)
    star += "*"
    print("{}{}".format(blank, star))