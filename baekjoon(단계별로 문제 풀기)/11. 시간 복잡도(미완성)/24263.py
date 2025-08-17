# 24263번(알고리즘 수업 - 알고리즘의 수행 시간 2) : https://www.acmicpc.net/problem/24263
import sys

input = sys.stdin.readline

# 해당 문제의 시간 복잡도는 O(n)
# 해당 코드는 실행 횟수 n번이므로 n으로 출력
# O(1)의 최고 차수는 1이므로 1로 출력
n:int = int(input().rstrip())
print(n)
print(1)