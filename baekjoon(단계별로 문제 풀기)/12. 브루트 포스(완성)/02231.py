# 2231번(분해합) 문제 : https://www.acmicpc.net/problem/2231
import sys

input=sys.stdin.readline

N:int=int(input().rstrip())

# 반례를 찾았습니다. 1의 자리수도 분해합이 존재했습니다. 그러므로 N>0로 수정합니다.
if N>0 :
    temp:int = -1
    status:bool = False
    # 분해합 대상이 존재할 때 N과 차이는 최대 9*N의 숫자 개수입니다.
    for i in range(N-9*len(str(N)),N) :
        # 이것도 잘못되었으므로 i>9에서 i>0으로 수정합니다.
        if i>0 :
            temp = i
            for j in range(len(str(i))) :
                temp += (int)(str(i)[j])
        # 최소한희 분해합을 찾으면 탈출합니다.
        if temp == N :
            temp = i
            status = True
            break
    if status == True :
        print(temp)
    else :
        print(0)
else :
    print(0)