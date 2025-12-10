# 13909번(창문 닫기) 문제 : https://www.acmicpc.net/problem/13909
import sys

input = sys.stdin.readline

# n=1부터 쭉 세보면 n=4, n=9, n=16 기준으로 해서 열린 창문의 개수가 각각 2개,3개,4개,...이렇게 규칙이 존재합니다.
# 사실 이건 n=25까지 노가다를 해보면 쉽게 규칙을 찾을 수 있는 문제입니다.
n:int = int(input().rstrip())
print(int(n**0.5))