# 1918번(후위 표기식) 문제 : https://www.acmicpc.net/problem/1918
import sys

input = sys.stdin.readline

def precedence(op):
    if op == chr(43) or op == chr(45) : # 덧셈 혹은 빼기
        return 1 # 곱하기/나누기 다음으로 우선순위가 높으므로 1로 반환
    if op == chr(42) or op == chr(47) : # 곱하기 혹은 나누기
        return 2 # 우선순위가 가장 높으므로 2로 반환
    return 0 # 항이면 0으로 반환

def infix_to_postfix(expression) :
    stack = []
    result = []
    
    for char in expression :
        if char.isalnum():  # 피연산자일 경우
            result.append(char)
        elif char == '(':  # 여는 괄호
            stack.append(char)
        elif char == ')':  # 닫는 괄호
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # 여는 괄호 제거
        else:  # 연산자
            while stack and precedence(stack[-1]) >= precedence(char):
                result.append(stack.pop())
            stack.append(char)

    # 스택에 남아 있는 모든 연산자를 결과에 추가
    while stack:
        result.append(stack.pop())
    
    return result

expression = input().rstrip()
print("".join(infix_to_postfix(expression)))