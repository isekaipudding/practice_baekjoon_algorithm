# 2206번(벽 부수고 이동하기) 문제 : https://www.acmicpc.net/problem/2206
from collections import deque
import sys

input = sys.stdin.readline

# class 3에서 토마토(7576번) 문제 그리고 쉬운 최단거리(14940번) 등을 변형한 것입니다.
# 벽 부수는 여부 때문에 2차원 격자 그래프 아닌 3차원 격자 그래프를 사용해야 하네요.

def bfs(maze, row, col) :
    # 방향 벡터: 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 초기화. row, col, 벽 안 부숨(False)
    queue = deque()
    queue.append((0, 0, 0))
    
    visited:list = [[[False, False] for _ in range(col)] for _ in range(row)]
    visited[0][0][0] = True # 처음 지점 방문 처리
    
    # 여기서는 거리 리스트도 중요하니 추가합니다.
    distance:list = [[[0, 0] for _ in range(col)] for _ in range(row)]
    distance[0][0][0] = 1 # 시작점의 거리("이때 시작하는 칸과 끝나는 칸도 포함해서 센다."에 의해 1로 초기화)
    
    while queue :
        # 데이터 추출
        r, c, status = queue.popleft()
        
        # 도착했을 경우(인덱스 보정에 의해 -1 추가)
        if r == row - 1 and c == col - 1 :
            return distance[r][c][status]
        
        # 상하좌우 주변 칸 탐색
        for dr, dc in directions :
            nr:int = r + dr
            nc:int = c + dc
            
            if 0 <= nr < row and 0 <= nc < col : # 아 맞다 범위 체크를 안 했네요.
                if maze[nr][nc] == 0 and visited[nr][nc][status] == False :
                    # 벽이 아니고 방문하지 않았을 경우
                    visited[nr][nc][status] = True # 자세히 잘 보니 여기 = 아닌 ==로 해서 메모리 초과된 것 같습니다.
                    distance[nr][nc][status] = distance[r][c][status] + 1
                    queue.append((nr, nc, status))
                    
                if maze[nr][nc] == 1 and status == 0 and visited[nr][nc][1] == False :
                    # 벽을 만났고 아직 벽을 부수지 않는 경우
                    visited[nr][nc][1] = True
                    distance[nr][nc][1] = distance[r][c][status] + 1
                    queue.append((nr, nc, 1))
    
    return -1

# 행렬 입력 받기
row, col = map(int, input().split())
maze = []

# 입력 받기
for i in range(row) :
    numbers:str = input().rstrip()
    L:list = [0 for _ in range(col)]
    for j in range(len(numbers)) :
        L[j] = int(numbers[j])
    maze.append(L)

# BFS 실행 및 결과 출력
result = bfs(maze, row, col)
print(result)