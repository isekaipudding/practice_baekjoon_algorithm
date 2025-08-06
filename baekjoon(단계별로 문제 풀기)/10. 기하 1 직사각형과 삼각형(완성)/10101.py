# 10101번(삼각형 외우기) 문제 : https://www.acmicpc.net/problem/10101
import sys

input = sys.stdin.readline

A:int = int(input().rstrip())
B:int = int(input().rstrip())
C:int = int(input().rstrip())

if A+B+C == 180 :
    if A==B and B==C and C==A :
        print("Equilateral")
    elif (A!=60 and A==B) or (B!=60 and B==C) or (C!=60 and C==A) :
        print("Isosceles")
    elif A!=B and B!=C and C!=A :
        print("Scalene")
else :
    print("Error")