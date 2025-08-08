# 9328번(열쇠) 문제 : https://www.acmicpc.net/problem/9328
import sys
from collections import deque

input = sys.stdin.readline

# 방향 : 상하좌우
dr:list = [-1, 1, 0, 0]
dc:list = [0, 0, -1, 1]

def bfs(row, col, graph, keys) :
    visited = [[False for _ in range(col + 2)] for _ in range(row + 2)]
    queue = deque()
    queue_door:list = [deque() for _ in range(26)]  # 각 문에 대한 대기 큐
    result:int = 0

    queue.append((0, 0))
    visited[0][0] = True

    while queue :
        r, c = queue.popleft()

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if not (0 <= nr < row + 2 and 0 <= nc < col + 2) :
                continue
            if visited[nr][nc] or graph[nr][nc] == '*' :
                continue

            cell = graph[nr][nc]
            visited[nr][nc] = True

            # 문
            if 'A' <= cell <= 'Z' :
                key_index = ord(cell) - ord('A')
                if keys[key_index] :
                    queue.append((nr, nc))
                else :
                    queue_door[key_index].append((nr, nc))
                continue

            # 열쇠
            if 'a' <= cell <= 'z' :
                key_index = ord(cell) - ord('a')
                if not keys[key_index] :
                    keys[key_index] = True
                    while queue_door[key_index] :
                        queue.append(queue_door[key_index].popleft())

            # 문서
            if cell == '$' :
                result += 1

            queue.append((nr, nc))

    return result

for _ in range(int(input().rstrip())) :
    row, col = map(int, input().split())
    graph:list = [['.' for _ in range(col + 2)] for _ in range(row + 2)]  # 바깥 여백 포함
    keys:list = [False for _ in range(26)]

    for i in range(1, row + 1) :
        line:str = input().strip()
        for j in range(1, col + 1) :
            graph[i][j] = line[j - 1]

    key_line:str = input().strip()
    if key_line != '0' :
        for c in key_line :
            keys[ord(c) - ord('a')] = True

    print(bfs(row, col, graph, keys))