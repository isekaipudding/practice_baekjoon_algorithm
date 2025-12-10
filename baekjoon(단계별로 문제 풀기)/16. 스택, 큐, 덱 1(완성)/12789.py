# 12789번(도키도키 간식드리미) 문제 : https://www.acmicpc.net/problem/12789
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())

IN:list = list(map(int,input().split()))
IN.reverse() # pop()을 원활하게 사용하기 위해 역돌격 실시

# LINE : 현재 줄 서있는 곳
LINE:list = [0 for _ in range(N)]
for i in range(N) :
    LINE[i] = IN[i]

TEMP:list = [] # 한 명씩만 설 수 있는 공간

count:int = 1 # 순서대로만 들어 갈 수 있는 라인에서 현재 들어갈 수 있는 번호
while not (len(LINE) == 0 and len(TEMP) == 0) : # 더 이상 사람들이 없으면 탈출
    if len(LINE) > 0 and len(TEMP) == 0 : # 대기줄에만 사람들이 있는 경우
        if LINE[-1] == count : # 운 좋게 맨 앞 번호가 바로 간식 받을 수 있는 경우
            LINE.pop()
            count += 1
        else : # 운이 나빠서 임시 공간에 들어가야 하는 경우
            TEMP.append(LINE.pop())
    elif len(LINE) > 0 and len(TEMP) > 0 : # 대기줄, 임시 공간에 사람들이 있는 경우
        if LINE[-1] != count and TEMP[-1] != count : # 운이 매우 나빠서 임시 공간에 들어가야 하는 경우
            TEMP.append(LINE.pop())
        elif LINE[-1] == count and TEMP[-1] != count : # 운 좋게 맨 앞 번호가 바로 간식 받을 수 있는 경우
            LINE.pop()
            count += 1
        elif LINE[-1] != count and TEMP[-1] == count : # 운 좋게 임시 공간에서 바로 간식 받을 수 있는 경우
            TEMP.pop()
            count += 1
    elif len(LINE) == 0 and len(TEMP) > 0 : # 임시 공간에만 사람들이 있는 경우
        if TEMP[-1]==count : # 운 좋게 바로 간식 받을 수 있는 경우
            TEMP.pop()
            count += 1
        else : #더 이상 안 된다! 탈출!
            break
if len(TEMP) == 0 :
    print("Nice")
elif len(TEMP) > 0 :
    print("Sad")