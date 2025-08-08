# 13460번(구슬 탈출 2) 문제 : https://www.acmicpc.net/problem/13460
import sys

input = sys.stdin.readline

def move(red_row, red_col, blue_row, blue_col, direction) :
    present_red_row, present_red_col = red_row, red_col
    present_blue_row, present_blue_col = blue_row, blue_col
    red_count = blue_count = red_back = blue_back = 0
    while True :
        red_row = red_row + direction_row[direction]
        red_col = red_col + direction_col[direction]
        red_count += 1
        if graph[red_row][red_col] == "#":
            red_back += 1
            break
        if graph[red_row][red_col] == "B":
            red_back += 1
        if graph[red_row][red_col] == "O":
            red_back = 0
            break

    while True:
        blue_row = blue_row + direction_row[direction]
        blue_col = blue_col + direction_col[direction]
        blue_count += 1
        if graph[blue_row][blue_col] == "#":
            blue_back += 1
            break
        if graph[blue_row][blue_col] == "R":
            blue_back += 1
        if graph[blue_row][blue_col] == "O":
            blue_back = 0
            break

    new_red_row = present_red_row + direction_row[direction] * (red_count - red_back)
    new_red_col = present_red_col + direction_col[direction] * (red_count - red_back)
    new_blue_row = present_blue_row + direction_row[direction] * (blue_count - blue_back)
    new_blue_col = present_blue_col + direction_col[direction] * (blue_count - blue_back)

    return new_red_row, new_red_col, new_blue_row, new_blue_col

def dfs(n, red_row, red_col, blue_row, blue_col) :
    global result
    if n >= 11 :
        return

    for d in range(4) :
        new_red_row, new_red_col, new_blue_row, new_blue_col = move(red_row, red_col, blue_row, blue_col, d)
        if (new_red_row, new_red_col, new_blue_row, new_blue_col) == (red_row, red_col, blue_row, blue_col) :
            continue

        if graph[new_blue_row][new_blue_col] == "O" :
            continue
        else :
            if graph[new_red_row][new_red_col] == "O" :
                result = min(result, n)
                return

        graph[red_row][red_col], graph[blue_row][blue_col] = ".", "."
        graph[new_red_row][new_red_col], graph[new_blue_row][new_blue_col] = "R", "B"
        dfs(n+1, new_red_row, new_red_col, new_blue_row, new_blue_col)
        graph[new_red_row][new_red_col], graph[new_blue_row][new_blue_col] = ".", "." 
        graph[red_row][red_col], graph[blue_row][blue_col] = "R", "B"

N, M = map(int, input().split())
graph:list = []
for _ in range(N) :
    graph.append(list(input().rstrip()))
direction_row:list = [-1, 1, 0, 0]
direction_col:list = [0, 0, -1, 1]

for i in range(N) :
    for j in range(M) :
        if graph[i][j] == "R" :
            out_red = (i, j)
        if graph[i][j] == "B" :
            out_blue = (i, j)
        if graph[i][j] == "O" :
            out = (i, j)
            
result:int = 11

dfs(1, out_red[0], out_red[1], out_blue[0], out_blue[1])
if result > 10 :
    print(-1)
else :
    print(result)