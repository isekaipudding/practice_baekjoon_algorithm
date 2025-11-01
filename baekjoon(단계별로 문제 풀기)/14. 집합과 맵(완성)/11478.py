# 11478번(서로 다른 부분 문자열의 개수) 문제 : https://www.acmicpc.net/problem/11478
import sys

input = sys.stdin.readline

sentence:str = input().rstrip()

L:list = []

for i in range(len(sentence)) :
    for j in range(len(sentence)-i) :
        L.append(sentence[j:(j+i+1):1])
        
print(len(set(L)))