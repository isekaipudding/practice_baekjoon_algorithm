# 1152번(단어의 개수) 문제 : https://www.acmicpc.net/problem/1152
import sys

input = sys.stdin.readline

string:str = input().rstrip()

count:int = 0
status:bool = True
for i in range(len(string)) :
    if string[i] != " " and status == True :
        count += 1
        status = False
    if string[i] == " " and status == False :
        status=True
        
print(count)