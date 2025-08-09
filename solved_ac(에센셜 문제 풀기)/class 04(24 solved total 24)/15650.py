# 15650번(N과 M(2)) 문제 : https://www.acmicpc.net/problem/15650
import sys

input = sys.stdin.readline

# 백트래킹 알고리즘 기초 문제입니다.

def backtracking(start) :
    if len(stack) == M : # 만약 스택 길이가 정해진 값과 일치하면
        print(" ".join(map(str, stack))) # 출력 형식에 따라 출력하고
        return # 반환하여 탐색을 중지합니다.
    else :
        for i in range(start, N + 1) : # 백트래킹은 dfs 혹은 bfs에서 조건을 추가하여 특정한 구간만 탐색하도록 하는 알고리즘입니다.
            stack.append(i) # 수열에 수를 추가합니다.
            backtracking(i + 1) # 깊이 우선 탐색 알고리즘 사용
            stack.pop() # 출력 완료했으면 다음 수를 저장하기 위해 하나 제거합니다.

N, M = map(int, input().split())
stack:list = [] # 스택 자료구조 사용
backtracking(1) # 시작 지점 설정하고 백트래킹 알고리즘 사용