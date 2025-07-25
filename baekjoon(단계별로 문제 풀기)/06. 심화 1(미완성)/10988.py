# 10988번(팰린드롬인지 확인하기) 문제 : https://www.acmicpc.net/problem/10988
import sys

input = sys.stdin.readline

string:str = input().rstrip()

if string == string[::-1] :
    print(1)
else :
    print(0)