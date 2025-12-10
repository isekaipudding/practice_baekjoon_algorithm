# 4949번(균형잡힌 세상) 문제 : https://www.acmicpc.net/problem/4949
import sys

input = sys.stdin.readline

# 아스키코드에서 ( 는 40, ) 는 41, [ 는 91, ] 는 93
while True :
    IN:str = input().rstrip()
    stack:list = []
    
    if IN == "." : # 오직 .만 입력되면 탈출
        break
    
    for i in range(len(IN)) :
        if len(stack) == 0 : # 스택 안에 공간이 없는 경우
            if ord(IN[i]) == 40 or ord(IN[i]) == 91 : # ( 혹은 [ 인 경우
                stack.append(IN[i]) 
            elif ord(IN[i]) == 41 or ord(IN[i]) == 93 : # ) 혹은 ]인 경우 무조건 균형 불가능이므로 추가하고 탈출
                stack.append(IN[i])
                break
        elif len(stack)>0 : # 스택 안에 공간이 있는 경우
            if stack[-1] == '(' :
                if ord(IN[i]) == 40 or ord(IN[i]) == 91 : # ( 혹은 [ 인 경우
                    stack.append(IN[i])
                elif ord(IN[i]) == 41 : # ) 인 경우 () 균형이 잡혀서 상쇄됩니다.
                    stack.pop()
                elif ord(IN[i]) == 93 : # ( 인 상태에서 ]가 들어오면 무조건 균형 불가능
                    stack.append(IN[i])
                    break
            elif stack[-1] == '[' :
                if ord(IN[i]) == 40 or ord(IN[i]) == 91 : # ( 혹은 [ 인 경우
                    stack.append(IN[i])
                elif ord(IN[i]) == 93 : # ] 인 경우 [] 균형이 잡혀서 상쇄됩니다.
                    stack.pop()
                elif ord(IN[i]) == 41 : # [ 인 상태에서 )가 들어오면 무조건 균형 불가능
                    stack.append(IN[i])
                    break
        
    if len(stack) > 0 :
        print("no")
    elif len(stack) == 0 :
        print("yes")