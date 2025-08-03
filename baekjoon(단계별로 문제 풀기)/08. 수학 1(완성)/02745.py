# 2745번(진법 변환) 문제 : https://www.acmicpc.net/problem/2745
import sys

input = sys.stdin.readline

N, B = map(str, input().split())

ten_dights:int = 0

for i in range(len(N)) :
    if 48 <= ord(N[i]) and ord(N[i]) <= 57 :
        ten_dights += (ord(N[i])-48) * (int(B)**(len(N)-1-i))
    elif 65 <= ord(N[i]) and ord(N[i]) <= 90 :
        ten_dights += (ord(N[i])-65+10) * (int(B)**(len(N)-1-i))
        
print(ten_dights)