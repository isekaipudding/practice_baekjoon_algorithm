# 9498번(시험 성적) 문제 : https://www.acmicpc.net/problem/9498
import sys

input = sys.stdin.readline

score:int = int(input().rstrip())

if 90 <= score :
    print("A")
elif 80 <= score and score < 90 :
    print("B")
elif 70 <= score and score < 80 :
    print("C")
elif 60 <= score and score < 70 :
    print("D")
else :
    print("F")