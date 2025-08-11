# 10828번(스택) 문제 : https://www.acmicpc.net/problem/10828
import sys

input = sys.stdin.readline

T:int = int(input().rstrip())

stack:list = []

for i in range(T) :
    command:list = list(map(str, input().split()))
    
    if len(command) == 2 and command[0] == "push" :
        stack.append(int(command[1]))
    if len(command) == 1 :
        if command[0] == "pop" :
            if len(stack) > 0 :
                print(stack.pop())
            else :
                print(-1)
        if command[0] == "size" : 
            print(len(stack))
        if command[0] == "empty" :
            if len(stack) == 0 :
                print(1)
            elif len(stack) > 0 :
                print(0)
        if command[0] == "top" :
            if len(stack) > 0 :
                print(stack[-1])
            else :
                print(-1)