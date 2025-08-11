# 1259번(팰린드롬수) 문제 : https://www.acmicpc.net/problem/1259
import sys

input = sys.stdin.readline

while True :
    N:str = input().rstrip() # 문자열로 입력을 받습니다.
    if N == '0' : # 만약 0이면 바로 탈출합니다.
        break
    
    status:bool = True # 판별하기 위한 상태 변수입니다.
    for i in range(0, len(N)//2, 1) : # 시간 복잡도 O(N)을 가진 브루트 포스 알고리즘 사용
        if N[i] != N[len(N) - 1 - i] : # 만약 하나라도 팰린드롬 조건을 만족하지 못 하면
            status = False # 팰린드롬이 아닌 것으로 판단하고
            break # 바로 탈출
        
    if status == True : # 만약 팰린드롬이 맞으면 yes
        print("yes")
    else : # 만약 팰린드롬이 아니면 no
        print("no")