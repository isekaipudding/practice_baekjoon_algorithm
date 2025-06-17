# 2438번(별 찍기 - 1) 문제 : https://www.acmicpc.net/problem/2438
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())

output:str = ""

for i in range(N) :
    output += "*"
    print(output)