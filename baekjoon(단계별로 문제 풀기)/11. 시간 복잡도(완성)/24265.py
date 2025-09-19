# 24265번(알고리즘 수업 - 알고리즘의 수행 시간 4) : https://www.acmicpc.net/problem/24265
import sys

input = sys.stdin.readline

# 해당 문제의 시간 복잡도는 O(n^2)
# 해당 코드는 실행 횟수는 다음과 같습니다.
# n=7인 경우 sum 값 말고, 실행 횟수는 6+5+4+3+2+1=21회
# O(1)의 최고 차수는 2이므로 2로 출력
n:int = int(input().rstrip())
print(int(n * (n-1) / 2))
print(2)