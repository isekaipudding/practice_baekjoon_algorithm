# 5622번(다이얼) 문제 : https://www.acmicpc.net/problem/5622
import sys

input = sys.stdin.readline

index:list = [
    [],
    [],
    ['A','B','C'],
    ['D','E','F'],
    ['G','H','I'],
    ['J','K','L'],
    ['M','N','O'],
    ['P','Q','R','S'],
    ['T','U','V'],
    ['W','X','Y','Z']
]

string:str = input().rstrip()

result:int = 0
for i in range(len(string)) :
    if 'A' <= string[i] and string[i] <= 'C' :
        result += 2
    if 'D' <= string[i] and string[i] <= 'F' :
        result += 3
    if 'G' <= string[i] and string[i] <= 'I' :
        result += 4
    if 'J' <= string[i] and string[i] <= 'L' :
        result += 5
    if 'M' <= string[i] and string[i] <= 'O' :
        result += 6
    if 'P' <= string[i] and string[i] <= 'S' :
        result += 7
    if 'T' <= string[i] and string[i] <= 'V' :
        result += 8
    if 'W' <= string[i] and string[i] <= 'Z' :
        result += 9
    
result += len(string)
print(result)