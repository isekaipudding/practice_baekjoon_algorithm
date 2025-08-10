# 1012번(유기농 배추) 문제 : https://www.acmicpc.net/problem/1012
from collections import deque
import sys

input = sys.stdin.readline

# 상, 하, 좌, 우
# 상 -> dx=0, dy=-1
# 하 -> dx=0, dy=1
# 좌 -> dx=-1, dy=0
# 우 -> dx=1, dy=0
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(graph, a, b) :
    queue = deque()
    queue.append((a,b)) # 맨 처음 cell의 정보를 저장합니다.
    graph[a][b] = 0

    while queue : # 하나의 연결 요소의 모든 cell이 1->0으로 변환할 때까지 while문을 실행합니다.
        x, y = queue.popleft() # 현재 cell의 정보를 추출합니다.
        for i in range(4) : # 해당 셀의 상하좌우를 확인합니다.
            # 주변 cell 정보를 추출합니다.
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M : # 2차원 평면 그래프 밖에 있으면
                continue # 무시하고 바로 다음 칸으로 이동
            if graph[nx][ny] == 1 : # 만약 주변에 1인 칸이 발견되면
                graph[nx][ny] = 0 # 0으로 변환하고
                queue.append((nx, ny)) # 튜플로 저장합니다.
    return

T:int = int(input().rstrip())

for i in range(T) :
    count = 0 # 연결 요소 개수
    N, M, K = map(int,input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]

    for j in range(K) :
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(N) :
        for b in range(M) :
            if graph[a][b] == 1 :
                count += 1 # 하나의 연결 요소에 닿으면 연결 요소 1개 추가
                bfs(graph, a, b) # 하나의 연결 요소에 있는 모든 cell을 1->0으로 변환
    print(count)