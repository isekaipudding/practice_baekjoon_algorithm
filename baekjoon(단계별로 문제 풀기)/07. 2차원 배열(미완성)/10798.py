# 10798번(세로읽기) 문제 : https://www.acmicpc.net/problem/10798
import sys

input = sys.stdin.readline

Array1D = ["" for _ in range(5)]
ArrayLength = [0 for _ in range(5)]

for i in range(5) :
    Array1D[i] = input().rstrip()
    ArrayLength[i] = len(Array1D[i])
    
maxLength:int = 0
for i in range(5) :
    if maxLength < len(Array1D[i]) :
        maxLength = len(Array1D[i])
        
result:str = ""
for i in range(maxLength) :
    for j in range(5) :
        temp:str = Array1D[j]
        if i < len(temp) :
            result += temp[i]
            
print(result)