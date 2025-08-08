# 1806번(부분합) 문제 : https://www.acmicpc.net/problem/1806
import sys

input = sys.stdin.readline

N, S = map(int, input().split())
L:list = list(map(int, input().split()))

# 누적 합 알고리즘 사용
prefix:list = [0 for _ in range(N + 1)]
for i in range(N) :
    prefix[i+1] = prefix[i] + L[i]
    
start = 0
min_length = N + 1  # 가능한 최대 길이보다 큰 값으로 초기화

# 시간 복잡도가 O(N^2)에서 O(N)으로 개선되었습니다.
# 투 포인터 알고리즘 사용
for end in range(1, N+1, 1) :
    # 투 포인터 알고리즘을 한 번 더 사용
    # 누적합(Prefix sum) 활용: prefix[end] - prefix[start] >= S 인 순간
    while prefix[end] - prefix[start] >= S :
        min_length = min(min_length, end - start)
        start += 1

if min_length == N + 1 :
    print(0)
else :
    print(min_length)