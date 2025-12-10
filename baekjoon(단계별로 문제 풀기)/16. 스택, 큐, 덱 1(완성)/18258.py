# 18258번(큐 2) 문제 : https://www.acmicpc.net/problem/18258
import sys
from collections import deque

input = sys.stdin.readline

N:int = int(input().rstrip())

queue = deque([]) # 큐 자료형을 사용할려면 deque 사용할 것
for i in range(N) :
    COMMAND:str = input().rstrip()
    if " " in COMMAND :
        #공백 기준으로 분리
        split_values = COMMAND.split()
        if split_values[0] == "push" : # 스택이 아닌 큐이므로 이렇게 삽입해야 합니다.
            queue.insert(0, int(split_values[1]))
    else :
        if COMMAND=="pop" :
            if len(queue) > 0 :
                print(queue.pop())
            elif len(queue) == 0 :
                print(-1)
        if COMMAND == "size" :
            print(len(queue))
        if COMMAND == "empty" :
            if len(queue) == 0 :
                print(1)
            elif len(queue) > 0 :
                print(0)
        if COMMAND == "front" :
            if len(queue) > 0 :
                print(queue[-1])
            elif len(queue) == 0 :
                print(-1)
        if COMMAND == "back" :
            if len(queue) > 0 :
                print(queue[0])
            elif len(queue) == 0 :
                print(-1)