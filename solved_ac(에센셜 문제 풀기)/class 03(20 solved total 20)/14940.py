# 14940번(쉬운 최단거리) 문제 : https://www.acmicpc.net/problem/14940
from collections import deque
import sys

input = sys.stdin.readline

# 행, 열 칸수를 입력합니다.
row, col = map(int, input().split())

# 칸의 상태값을 입력합니다.
number:list = [list(map(int, input().split())) for _ in range(row)]

# 모든 칸의 거리값을 -1로 초기화합니다.
distance:list = [[-1 for _ in range(col)] for _ in range(row)]

queue = deque()
for i in range(row) :
    for j in range(col) :
        if number[i][j] == 2 : # 만약 시작점이면
            distance[i][j] = 0 # 거리값을 0으로 하고
            queue.append((i, j)) # 큐에 저장합니다. 시작점이 바로 루트(root)입니다.
        elif number[i][j] == 0 : # 만약 벽이라면
            distance[i][j] = 0 # 어차피 벽에 오지 않으므로 거리값을 0으로 설정합니다.
            
# 상하좌우 1칸씩 움직여주는 좌표 변화량입니다.
# 상 : 행 -1칸, 열 0칸 움직입니다.
# 하 : 행 1칸, 열 0칸 움직입니다.
# 좌 : 행 0칸, 열 -1칸 움직입니다.
# 우 : 행 0칸, 열 1칸 움직입니다.
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 너비 우선 탐색 알고리즘 사용
while queue :
    r, c = queue.popleft() # 현재 칸의 좌표를 추출합니다.
    
    for i in range(4) : # nr, nc는 현재 칸으로부터 상하좌우 주변 칸의 좌표입니다.
        nr = r + dr[i]
        nc = c + dc[i]
        
        if 0 <= nr < row and 0 <= nc < col : # 범위를 벗어나지 않고
            if number[nr][nc] == 1 and distance[nr][nc] == -1 : # 지나갈 수 있는 칸에서 아직 기록되지 않았다면
                distance[nr][nc] = distance[r][c] + 1 # 주변 칸 정보를 현재 칸 기준으로 +1 해준 뒤
                queue.append((nr, nc)) # bfs 알고리즘에 따라 queue에 저장합니다.
                
# 출력 형식에 따라 출력합니다.
for i in range(row) :
    print(" ".join(map(str, distance[i])))