# 1629번(곱셈) 문제 : https://www.acmicpc.net/problem/1629
import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

TEMP:int = B
binary_code:list = []

while TEMP > 0 :
    binary_code.append(TEMP & 1)
    TEMP = TEMP >> 1
binary_code.reverse()

remainder:int = 1
for i in range(len(binary_code)) :
    if binary_code[i] == 0 : # A^2k = (A^k)^2
        remainder = (remainder**2) % C
    if binary_code[i] == 1 : # A^(2k+1) = (A^k)^2 * A
        remainder = (remainder**2) % C
        remainder = (remainder * (A % C)) % C

print(remainder)