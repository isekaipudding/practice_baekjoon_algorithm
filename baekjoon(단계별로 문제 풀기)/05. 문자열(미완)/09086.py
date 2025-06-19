# 9086번(문자열) 문제 : https://www.acmicpc.net/problem/9086
import sys

input=sys.stdin.readline

T:int = int(input().rstrip())

for i in range(T) :
    string:str = input().rstrip()
    print("{}{}".format(string[0], string[len(string) - 1]))