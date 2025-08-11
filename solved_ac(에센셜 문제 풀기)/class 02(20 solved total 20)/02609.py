# 2609번(최대공약수와 최소공배수) 문제 : https://www.acmicpc.net/problem/2609
import sys

input = sys.stdin.readline

# 아... 이것은 유클리드 호제법이라는 것이다. gcd는 최대공약수, lcm은 최소공배수를 의미하지.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

A, B = map(int, input().split())
print(gcd(A, B))
print(lcm(A, B))