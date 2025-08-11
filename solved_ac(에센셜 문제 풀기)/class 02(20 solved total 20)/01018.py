# 1018번(체스판 다시 칠하기) 문제 : https://www.acmicpc.net/problem/1018
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

ChessBoard:list = []
for i in range(N) :
    WBCellsIn1Row = input().rstrip()
    ChessBoard.append(WBCellsIn1Row)
    
MIN_COUNT:int = 32 # 이론적으로 가능한 Chill해야 하는 최대 개수

for i in range(0, N-7, 1) : # 행 기준으로 시작점 목록
    for j in range(0, M-7, 1) : # 열 기준으로 시작점 목록
        count:int = 0
        for a in range(0, 8, 1) : # 시작점(행) 기준으로 0행부터 7행까지
            for b in range(0, 8, 1) : # 시작점(열) 기준으로 0열부터 7열까지
                if ((i+a) + (j+b)) % 2 == 0 :
                    if ChessBoard[i+a][j+b] != 'W' : # 하얀색 칸이 아닌 경우 하얀색 칸으로 Chill할 것
                        count += 1
                else :
                    if ChessBoard[i+a][j+b] != 'B' : # 검은색 칸이 아닌 경우 검은색 칸으로 Chill할 것
                        count += 1
        if count > 32 : # 흑백 반전 시키는 과정입니다.
            count = 64 - count
        if count < MIN_COUNT :
            MIN_COUNT = count
            
print(MIN_COUNT)