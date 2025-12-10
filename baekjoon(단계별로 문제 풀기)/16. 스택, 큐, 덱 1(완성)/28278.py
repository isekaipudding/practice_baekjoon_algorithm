# 28278번(스택 2) 문제 : https://www.acmicpc.net/problem/28278
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())

stack:list = []
for i in range(N) :
    COMMAND = input().strip()
    if " " in COMMAND :
        # 공백 기준으로 분리
        split_values = COMMAND.split()
        int_values = [int(value) for value in split_values]
        if int_values[0] == 1 :
            stack.append(int_values[1])
    else :
        COMMAND:int = int(COMMAND) # 정수로 변환하지 않으면 명령어 인식이 안 됩니다.
        if COMMAND == 2 :
            if len(stack) > 0 :
                print(stack.pop())
            else :
                print(-1)
        if COMMAND == 3 :
            print(len(stack))
        if COMMAND == 4 :
            if len(stack) == 0 :
                print(1)
            else :
                print(0)
        if COMMAND == 5 :
            if len(stack) > 0 :
                print(stack[-1])
            else :
                print(-1)