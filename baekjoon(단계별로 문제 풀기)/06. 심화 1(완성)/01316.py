# 1316번(그룹 단어 체커) 문제 : https://www.acmicpc.net/problem/1316
import sys

input = sys.stdin.readline

T:int = int(input().rstrip())

count:int = 0
for i in range(T) :
    status:bool = False
    alpha:list = [False] * 26
    string = input().rstrip()
    for j in range(len(string)) :
        if j>0 :
            if string[j-1] != string[j] and alpha[ord(string[j]) - 97]==True :
                status = True
        if 97 <= ord(string[j]) and ord(string[j]) <= 122 :
            alpha[ord(string[j]) - 97] = True
    if status == False :
        count += 1
print(count)