# 24264번(알고리즘 수업 - 알고리즘의 수행 시간 3) : https://www.acmicpc.net/problem/24264
import sys

input = sys.stdin.readline

# 해당 문제의 시간 복잡도는 O(n^2)
# 해당 코드는 실행 횟수 n^2번이므로 n**2으로 출력
# O(1)의 최고 차수는 2이므로 2로 출력
n:int = int(input().rstrip())
print(n**2)
print(2)