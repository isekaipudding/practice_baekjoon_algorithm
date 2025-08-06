# 9506번(약수들의 합) : https://www.acmicpc.net/problem/9506
import sys

input = sys.stdin.readline

# 2^n-1이 메르센 소수를 만족할 때 해당 n을 2^(n-1)x(2^n-1)에 대입하면 그 수는 완전수입니다.
# 여기서 100000 이하의 완전수는 6, 28, 496, 8128입니다.

while True :
    N:int=int(input().rstrip())
    if N == -1 :
        break
    if N >= 2 :
        if N==6 :
            print("6 = 1 + 2 + 3")
        elif N==28 :
            print("28 = 1 + 2 + 4 + 7 + 14 ")
        elif N==496 :
            print("496 = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248")
        elif N==8128 :
            print("8128 = 1 + 2 + 4 + 8 + 16 + 32 + 64 + 127 + 254 + 508 + 1016 + 2032 + 4064")
        else :
            print("{} is NOT perfect.".format(N))