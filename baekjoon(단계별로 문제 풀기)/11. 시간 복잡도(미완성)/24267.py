# 24267번(알고리즘 수업 - 알고리즘의 수행 시간 6) : https://www.acmicpc.net/problem/24267
import sys

input = sys.stdin.readline

# 해당 문제의 시간 복잡도는 O(n^3)
# 해당 코드는 실행 횟수는 (1/6)*(n-2)*(n-1)*n
# O(1)의 최고 차수는 3이므로 3으로 출력
n:int = int(input().rstrip())
print(int((n-2) * (n-1) * n / 6))
print(3)