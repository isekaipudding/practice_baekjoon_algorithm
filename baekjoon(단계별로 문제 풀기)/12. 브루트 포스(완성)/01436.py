# 1436번(영화감독 숌) 문제 : https://www.acmicpc.net/problem/1436
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())

result:int = 0
index:int = 0

# 원래 이것보다 더 효율적인 알고리즘이 존재합니다.
# 그러나 여기서는 브루트포스 알고리즘로 풀라고 했으니 일일히 1씩 더하는 알고리즘 적용
while True :
    result += 1
    if '666' in str(result) :
        index += 1
    if index >= N :
        break
print(result)