# 10845번(큐) 문제 : https://www.acmicpc.net/problem/10845
from collections import deque
import sys

input = sys.stdin.readline

T:int = int(input().rstrip())

queue = deque()

for i in range(T) :
    command:list = list(map(str, input().split()))
    
    if len(command) == 2 and command[0] == "push" :
        queue.appendleft(int(command[1]))
    if len(command) == 1 :
        if command[0] == "pop" :
            if len(queue) > 0 :
                print(queue.pop())
            else :
                print(-1)
        if command[0] == "size" : 
            print(len(queue))
        if command[0] == "empty" :
            if len(queue) == 0 :
                print(1)
            elif len(queue) > 0 :
                print(0)
        if command[0] == "front" :
            if len(queue) > 0 :
                print(queue[-1])
            else :
                print(-1)
        if command[0] == "back" :
            if len(queue) > 0 :
                print(queue[0])
            else :
                print(-1)