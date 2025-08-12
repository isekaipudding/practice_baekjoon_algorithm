# 27866번(문자와 문자열) 문제 : https://www.acmicpc.net/problem/27866
import sys

input = sys.stdin.readline

string:str = input().rstrip()
i:int = int(input().rstrip())

print(string[i-1])