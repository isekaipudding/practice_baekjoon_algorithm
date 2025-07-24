# 2908번(상수) 문제 : https://www.acmicpc.net/problem/2908
import sys
import math

input = sys.stdin.readline

a, b = map(str, input().split())

A:list = list(a)
B:list = list(b)

x:str = ""
y:str = ""
for i in range(math.ceil((len(A)-1)/2)) : 
    temp:int = A[i]
    A[i] = A[len(A)-1-i]
    A[len(A)-1-i] = temp
for i in range(len(A)) : 
    x += A[i]
for i in range(math.ceil((len(B)-1)/2)) : 
    temp:int = B[i]
    B[i] = B[len(B)-1-i]
    B[len(B)-1-i] = temp
for i in range(len(B)) : 
    y += B[i]
    
if int(x) >= int(y) :
    print(x)
elif int(x) < int(y) :
    print(y)