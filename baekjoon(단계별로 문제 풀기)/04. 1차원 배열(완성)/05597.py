# 5597번(과제 안 내신 분..?) 문제 : https://www.acmicpc.net/problem/5597
import sys

input = sys.stdin.readline

status:list = [False for _ in range(31)]

for i in range(28) :
    check = int(input().rstrip())
    if 1 <= check and check <= 30 :
        status[check] = True
        
result:list = []
for i in range(1,31) :
    if status[i] == False :
        result.append(i)
        
for num in result :
    print(num)