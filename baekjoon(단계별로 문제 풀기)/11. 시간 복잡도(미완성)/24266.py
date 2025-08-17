# 24266번(알고리즘 수업 - 알고리즘의 수행 시간 5) : https://www.acmicpc.net/problem/24266
import sys

input = sys.stdin.readline

# 해당 문제의 시간 복잡도는 O(n^3)
# 해당 코드는 실행 횟수는 n^3회회
# O(1)의 최고 차수는 3이므로 3으으로 출력
n:int = int(input().rstrip())
print(n**3)
print(3)