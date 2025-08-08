# 10350번(은행) : https://www.acmicpc.net/problem/10350
import math
import sys

input = sys.stdin.readline

# 설명을 위해 이미 제출된 코드를 주석을 추가해서 다시 제출합니다.

def min_magic_moves(N, ASSET) :
    # 누적합 배열을 준비합니다. 각 은행의 자본을 관리할 수 있도록 만들어줍니다.
    # (누적합 알고리즘 사용)
    prefix_sum = [0 for _ in range(N * 2 + 1)]  # 원형 구조를 고려해서 크기를 두 배로 설정!
    
    # 모든 은행에 대한 누적합을 계산합니다.
    for i in range(1, N * 2 + 1):
        # 은행 자본을 누적해서 prefix_sum 배열에 저장하는데, 원형 특성을 고려해줍니다.
        prefix_sum[i] = prefix_sum[i - 1] + ASSET[(i - 1) % N]

    # 전체 자산의 합을 계산합니다. 이것은 공식에 적용하기 위함입니다.
    total_sum = sum(ASSET)
    magic_count = 0  # 여기서부터 마법의 이동 횟수를 세어볼까요?.
    
    # 은행의 각각의 시작점에서 슬라이딩 윈도우를 통해 구간 합을 계산해줍니다.(슬라이딩 윈도우 알고리즘 사용)
    for start in range(N):  # 각 은행에서 시작점을 정해주고
        for end in range(start + 1, start + N + 1):  # 해당 은행에서 N까지의 길이를 고려합니다.
            # 현재 구간의 합을 계산합니다.
            current_sum = prefix_sum[end] - prefix_sum[start]
            # 만약 현재의 합이 음수라면 마법이 필요하다는 뜻이니까
            if current_sum < 0:
                # 절대값으로 바꿔주고 전체 자산의 합으로 나누면서 반올림 해서 필요한 마법 호출 횟수를 추가합니다.
                # 여기가 핵심 공식입니다. 증명이 매우매우매우 어려워서 공식만 가져왔습니다.
                # (애드 혹 알고리즘 사용)
                magic_count += math.ceil(abs(current_sum) / total_sum)

    # 최종적으로 계산된 마법의 이동 횟수를 반환합니다.
    return magic_count

N = int(input().rstrip())  # 전세계에 존재하는 은행의 수
ASSET = list(map(int, input().split()))  # 각 은행의 자본

print(min_magic_moves(N, ASSET))