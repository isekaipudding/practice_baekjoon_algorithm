# 1330번(두 수 비교하기) 문제 : https://www.acmicpc.net/problem/1330
import sys

input = sys.stdin.readline

A, B = map(int, input().split())

if A > B :
    print(">")
elif A < B :
    print("<")
else :
    print("==")