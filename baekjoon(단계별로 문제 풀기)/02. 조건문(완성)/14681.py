# 14681번(사분면 고르기) 문제 : https://www.acmicpc.net/problem/14681
import sys

input = sys.stdin.readline

X:int = int(input().rstrip())
Y:int = int(input().rstrip())

if X > 0 and Y > 0 : 
    print("1")
if X < 0 and Y > 0 : 
    print("2")
if X < 0 and Y < 0 : 
    print("3")
if X > 0 and Y < 0 : 
    print("4")