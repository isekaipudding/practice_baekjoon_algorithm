# 9012번(괄호) 문제 : https://www.acmicpc.net/problem/9012
import sys

input = sys.stdin.readline

T:int = int(input().rstrip())

for i in range(T) :
    VPS:str = input().strip()
    count:int = 0
    for j in range(len(VPS)) :
        if ord(VPS[j]) == 40 : # 기호 ( 이면 +1
            count += 1
        if ord(VPS[j]) == 41 : # 기호 ) 이면 -1
            count -= 1
        if count < 0 : # count 0 미만인 것은 무조건 VPS가 안 되는 경우이므로 break
            break
    if count == 0 :
        print("YES")
    else :
        print("NO")