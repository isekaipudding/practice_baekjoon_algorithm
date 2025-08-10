# 1931번(회의실 배정) 문제 : https://www.acmicpc.net/problem/1931
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())
Meeting_room:list = []

for i in range(N) : 
    Meeting_room.append(list(map(int, input().split())))
    
# 11650번 문제(좌표 정렬하기) 참고
# 1순위 시작하는 시각, 2순위 끝내는 시각이 아니었군요.
# 제가 착각했습니다. 1순위 끝내는 시각, 2순위 시작하는 시각으로 합니다.
Meeting_room.sort(key = lambda x : (x[1], x[0]))

MAX_MEETING:int = 0 # 과연 최대 몇 개의 회의를 가질 수 있을까요?
CURRENT_END:int = 0 # 최근 끝나는 시간은 0으로 합니다.

for START_TIME, END_TIME in Meeting_room : # 한 번 정보들을 추출합시다.
    if CURRENT_END <= START_TIME : # 회의 시작한 시각이 최근 끝낸 시각보다 더 크다면
        MAX_MEETING += 1 # 최대 회의실 수 하나 추가하고
        CURRENT_END = END_TIME # 끝낸 시각 정보를 갱신합니다.

print(MAX_MEETING)