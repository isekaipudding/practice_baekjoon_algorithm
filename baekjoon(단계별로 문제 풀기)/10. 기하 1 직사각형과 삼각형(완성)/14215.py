# 14215번(세 막대) 문제 : https://www.acmicpc.net/problem/14215
import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())
Length:list = [A, B, C]
Length.sort()

if Length[0] + Length[1] > Length[2] :
    print(sum(Length))
else :
    print(2 * (Length[0] + Length[1]) - 1)