# 14003번(가장 긴 증가하는 부분 수열 5) : https://www.acmicpc.net/problem/14003
import sys
from bisect import bisect_left

input = sys.stdin.readline

def longest_increasing_subsequence(arr) :
    if not arr :
        return 0, []

    lis = []  # LIS의 요소들을 저장할 리스트
    parent = [-1] * len(arr)  # LIS에 있는 요소들의 이전 인덱스를 추적할 배열
    lis_indices = []  # lis에 있는 요소들의 인덱스를 저장할 리스트

    for i, num in enumerate(arr) :
        pos = bisect_left(lis, num)
        if pos == len(lis) :
            lis.append(num)
            if lis_indices :
                parent[i] = lis_indices[-1]
            lis_indices.append(i)
        else:
            lis[pos] = num
            lis_indices[pos] = i
            if pos > 0 :
                parent[i] = lis_indices[pos - 1]

    # 부모 참조를 사용하여 LIS 재구성
    final_lis = []
    k = lis_indices[-1]
    while k >= 0 :
        final_lis.append(arr[k])
        k = parent[k]

    final_lis.reverse()
    return len(lis), final_lis

# 입력 처리
N = int(input().rstrip())
numbers = list(map(int, input().split()))

# LIS의 길이와 수열 구하기
lis_length, lis_sequence = longest_increasing_subsequence(numbers)

# 결과 출력
print(lis_length)
print(" ".join(map(str, lis_sequence)))