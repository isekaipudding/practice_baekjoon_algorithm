# 24511번(queuestack) 문제 : https://www.acmicpc.net/problem/24511
import sys

input = sys.stdin.readline

# 복습 중입니다.

N:int = int(input().rstrip())
structure:list = list(map(int, input().split()))
L:list = list(map(int, input().split()))
M:int = int(input().rstrip())
command:list = list(map(int, input().split()))

stack:list = [L[i] for i in range(-1, -N-1, -1) if structure[i] == 0]

# M이 스택 길이보다 더 작은 경우가 있어 여기서 31% 반례 발생
result:list = stack[0:min(len(stack), N, M)] + command[0:max(0, M-len(stack))]
print(*result)