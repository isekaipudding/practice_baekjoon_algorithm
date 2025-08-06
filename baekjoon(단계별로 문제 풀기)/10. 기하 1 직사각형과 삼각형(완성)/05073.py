# 5073번(삼각형과 세 변) 문제 : https://www.acmicpc.net/problem/5073
import sys

input = sys.stdin.readline

while True :
    A, B, C = map(int, input().split())
    if A==0 and B==0 and C==0 :
        break
    Length:list = [A, B, C]
    Length.sort()
    if Length[0] + Length[1] > Length[2] :
        if A==B and B==C and C==A :
            print("Equilateral")
        elif (A==B and B!=C) or (B==C and C!=A) or (C==A and A!=B) :
            print("Isosceles")
        elif A!=B and B!=C and C!=A :
            print("Scalene")
    else :
        print("Invalid")