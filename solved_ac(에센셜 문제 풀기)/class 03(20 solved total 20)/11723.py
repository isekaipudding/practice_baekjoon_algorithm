# 11723번(집합) 문제 : https://www.acmicpc.net/problem/11723
import sys

input = sys.stdin.readline

T:int = int(input().rstrip())
TF:list = [False for _ in range(21)]

for i in range(T) :
    command:list = list(map(str, input().split()))
    
    if len(command) == 2 :
        if command[0] == "add" :
            TF[int(command[1])] = True
        if command[0] == "remove" :
            TF[int(command[1])] = False
        if command[0] == "check" :
            if TF[int(command[1])] :
                print(1)
            else :
                print(0)
        if command[0] == "toggle" :
            if TF[int(command[1])] :
                TF[int(command[1])] = False
            else :
                TF[int(command[1])] = True
                
    if len(command) == 1 :
        if command[0] == "all" :
            for j in range(1, 21, 1) :
                TF[j] = True
        if command[0] == "empty" :
            for j in range(1, 21, 1) :
                TF[j] = False