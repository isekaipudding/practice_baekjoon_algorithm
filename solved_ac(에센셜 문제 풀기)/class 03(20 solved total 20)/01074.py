# 1074번(Z) 문제 : https://www.acmicpc.net/problem/1074
import sys

input = sys.stdin.readline

# 원래 초기식 및 점화식을 찾아서 재귀 함수로 구현할려고 했으나
# index를 활용한 규칙을 적용할려면 비트마스크 알고리즘이 더 낫다고 판단했습니다.

N, row, col = map(int, input().split())

result:int = 0

TEMP:int = 2
while row :
    result += (row % 2) * TEMP
    row = row >> 1
    TEMP = TEMP << 2
    
TEMP:int = 1
while col :
    result += (col % 2) * TEMP
    col = col >> 1
    TEMP = TEMP << 2

print(result)