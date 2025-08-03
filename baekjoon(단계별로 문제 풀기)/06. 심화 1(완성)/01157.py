# 1157번(단어 공부) 문제 : https://www.acmicpc.net/problem/1157
import sys

input = sys.stdin.readline

alpha:list = [0] * 26

word:str = input().rstrip()

for i in range(len(word)) :
    if 65 <= ord(word[i].upper()) and ord(word[i].upper()) <= 90 :
        alpha[ord(word[i].upper())-65] += 1

max:int = alpha[0]
index:int = 0     
for i in range(len(alpha)) :
    if max < alpha[i] :
        max = alpha[i]
        index = i
        
alpha.sort()
alpha.reverse()

if alpha[0] != alpha[1] :
    print(chr(65 + index))
else :
    print("?")