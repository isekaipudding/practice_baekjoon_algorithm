# 9465번(스티커) 문제 : https://www.acmicpc.net/problem/9465
import sys

input = sys.stdin.readline

T:int = int(input().rstrip())

for i in range(T) :
    N:int = int(input().rstrip())
    FIRST_LINE:list = list(map(int,input().split()))
    SECOND_LINE:list = list(map(int,input().split()))
    # 다이나믹 프로그래밍 알고리즘 사용
    dp_1st:list = [0 for _ in range(N+2)]
    dp_2nd:list = [0 for _ in range(N+2)]
    for j in range(2, N+2, 1) : # 여기가 핵심 알고리즘
        if dp_1st[j-2] > dp_1st[j-1] :
            dp_2nd[j] = dp_1st[j-2] + SECOND_LINE[j-2]
        else :
            dp_2nd[j] = dp_1st[j-1] + SECOND_LINE[j-2]
            
        if dp_2nd[j-2] > dp_2nd[j-1] :
            dp_1st[j] = dp_2nd[j-2] + FIRST_LINE[j-2]
        else :
            dp_1st[j] = dp_2nd[j-1] + FIRST_LINE[j-2]
            
    if dp_1st[-1] > dp_2nd[-1] :
        print(dp_1st[-1])
    else :
        print(dp_2nd[-1])