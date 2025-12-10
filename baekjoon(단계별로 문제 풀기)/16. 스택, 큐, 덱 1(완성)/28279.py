# 28279번(덱 2) 문제 : https://www.acmicpc.net/problem/28279
import sys
from collections import deque

input = sys.stdin.readline

N:int = int(input().rstrip())

queue = deque([]) # 큐 자료형을 사용할려면 deque 사용할 것
for i in range(N) :
    COMMAND:str = input().rstrip()
    if " " in COMMAND :
        # 공백 기준으로 분리
        split_values = COMMAND.split()
        int_values = [int(value) for value in split_values]
        if int_values[0] == 1 :
            queue.insert(0, int_values[1])
        if int_values[0] == 2 :
            queue.append(int_values[1])
    else :
        COMMAND:int = int(COMMAND)
        if COMMAND==3 :
            if len(queue) > 0 :
                print(queue.popleft())
            elif len(queue) == 0 :
                print(-1)
        if COMMAND == 4 :
            if len(queue) > 0 :
                print(queue.pop())
            elif len(queue) == 0 :
                print(-1)
        if COMMAND == 5 :
            print(len(queue))
        if COMMAND == 6 :
            if len(queue) > 0 :
                print(0)
            elif len(queue) == 0 :
                print(1)
        if COMMAND == 7 :
            if len(queue) > 0 :
                print(queue[0])
            elif len(queue) == 0 :
                print(-1)
        if COMMAND == 8 :
            if len(queue) > 0 :
                print(queue[-1])
            elif len(queue) == 0 :
                print(-1)