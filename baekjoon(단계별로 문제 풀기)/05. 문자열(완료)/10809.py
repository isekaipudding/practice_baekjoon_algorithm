# 10809번(알파벳 찾기) 문제 : https://www.acmicpc.net/problem/10809
import sys

input=sys.stdin.readline

alpha:list=[-1 for _ in range(26)]

string:str = input().rstrip()

for i in range(len(string)) :
    if 97 <= ord(string[i]) and ord(string[i]) <= 122 :
        if alpha[ord(string[i])-97] == -1 :
            alpha[ord(string[i])-97] = i
            
print(" ".join(map(str, alpha)))