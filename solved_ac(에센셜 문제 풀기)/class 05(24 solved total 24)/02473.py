# 2473번(세 용액) : https://www.acmicpc.net/problem/2473
import sys

input = sys.stdin.readline

# 2467번(용액) 문제에 있던 소스 코드를 재활용했습니다.

N:int = int(input().rstrip())
L:list = list(map(int, input().split()))
L.sort()

closest_sum:int = 3 * 10 ** 9
# 간단한 출력을 위해 tuple로 저장합니다.
result:tuple = (0, 0, 0)

# 잘 보시면 이건 결국 이진 탐색 알고리즘인 것을 알 수 있습니다.
for i in range(N - 2) :
    START_INDEX:int = i + 1
    END_INDEX:int = N - 1
    while START_INDEX < END_INDEX :
        # 여기서 두 포인터 알고리즘이 사용됩니다.
        current_sum:int = L[i] + L[START_INDEX] + L[END_INDEX]
        # 가장 가까운 값을 찾기 위해 비교
        if abs(current_sum) < abs(closest_sum) :
            closest_sum = current_sum
            result = (L[i], L[START_INDEX], L[END_INDEX])
        # sum이 0보다 작으면 START_INDEX를 늘리고, 크면 END_INDEX를 줄입니다.(이진 탐색)
        if current_sum < 0 :
            START_INDEX += 1
        elif current_sum > 0 :
            END_INDEX -= 1
        else :
            break # 정확히 0이면 바로 종료

print(*result) # 튜플로 하면 join() 없이 * 기호로 바로 출력 가능