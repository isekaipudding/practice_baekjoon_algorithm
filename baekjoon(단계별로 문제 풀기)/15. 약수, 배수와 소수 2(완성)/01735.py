# 1735번(분수 합) 문제 : https://www.acmicpc.net/problem/1735
import sys

input=sys.stdin.readline

#아... 이것은 유클리드 호제법이라는 것이다. gcd는 최대공약수, lcm은 최소공배수를 의미하지.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# A/B + C/D 형태로 표현
A, B = map(int, input().split())
C, D = map(int, input().split())

Denominator = A*D + C*B # 분자 구하기
Numerator = B * D # 분모 구하기
Great = gcd(Denominator,Numerator) # 최대공약수 구하기
# 분자와 분모를 서로소 형태로 구하기
Denominator //= Great
Numerator //= Great
print("{} {}".format(Denominator, Numerator))