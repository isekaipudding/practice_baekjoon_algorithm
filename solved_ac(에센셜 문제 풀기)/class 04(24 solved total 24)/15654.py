# 15654번(N과 M(5)) 문제 : https://www.acmicpc.net/problem/15654
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))

result = []
status = [False] * N  # 각 숫자의 사용 여부를 기록

def backtracking(depth):
    if depth == M:
        print(" ".join(map(str, result)))
        return
    for i in range(N):
        if not status[i]:  # 아직 사용되지 않은 숫자라면
            status[i] = True  # 사용 표시
            result.append(numbers[i])  # 숫자 추가
            backtracking(depth + 1)  # 재귀 호출
            result.pop()  # 백트래킹
            status[i] = False  # 사용을 취소

backtracking(0)