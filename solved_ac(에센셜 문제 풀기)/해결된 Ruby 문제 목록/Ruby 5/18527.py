# 18527번(All Kill) 문제 : https://www.acmicpc.net/problem/18527
import sys

input = sys.stdin.readline

# 주차 함수 : https://en.wikipedia.org/wiki/Parking_function

MOD:int = 998244353

numbers, time = map(int, input().split())
L:list = []
for _ in range(numbers) :
    X:int = int(input().rstrip())
    L.append(X)

time += 1

result:int = 1
for i in range(numbers - 1, -1, -1) :
    time -= L[i] - 1
    result = result * time % MOD
    
result = result * (time - numbers) % MOD
result = result * pow(time, MOD - 2, MOD) % MOD

print(result)

"""
우선 아이디어 시간이 Y1, Y2, ..., Yn이라고 할 때 그 도착시간은 {1, 2, ..., t}^n 집합의 원소입니다.
즉, 전체 경우의 수는 t^n이 되고 따라서 p * t^n은 All Kill 가능한 경우의 수입니다.
여기서 All Kill 가능한 경우의 수는 (1) 모든 문제들을 다 해결하면서 (2) 각 문제의 코딩이 끊기지 않는 것이 중요합니다.

먼저 주차 함수(parking function) 문제로 변형해서 다르게 풀 생각입니다.
그런데 주차 함수의 고전적인 형태는 원형 형태이므로 원형 주차 함수로 변형합니다.
길이 t짜리 직선에 n개의 연속 블록(길이 x_i)을 "친구가 도착 시간 Y_i에 빈 슬롯부터 순서대로 차지"하는 과정을
길이 t + 1짜리 원형으로 바꾸어 생각할 수 있습니다.

우선 여기서 "이 블록이 들어갈 수 있는 시작 위치"의 초기식을 구하면 M_n = t + 1이 되는 것을 알 수 있습니다.
왜냐면 길이가 t+1인 원형 리스트에서 아직 아무 것도 놓지 않았기 때문입니다.
그 다음 그 블록이 차지하는 칸 수는 x_n칸이나 시작 위치에서 겹치지 않게 놓을려면
그 블록이 차지한 x_n칸 중 맨 첫 칸 한 곳만이 실제 시작점으로 쓰이고, 나머지 x_n-1칸은 "다른 블록이 시작할 수 없는 영역"입니다.
따라서 n-1번째 블록이 차지할 수 있는 시작 위치는 M_(n-1) = M_n - (x_n - 1)이고 이것이 바로 점화식입니다.
초기식과 점화식이 존재하니 dp로 풀 수 있습니다.
하지만 n이 10^5이나 되어서 일일히 저장하고 활용할려고 하면 시간 및 공간이 낭비될 우려가 있습니다.
따라서 여기서는 dp를 활용하지 않습니다.

대신 공식을 유도하면 M_k = t + 1 - sigma(from j = k+1, to j = n)(x_j - 1)로 유도할 수 있습니다.
이렇게 하면 dp 없이도 k번째 블록이 들어갈 수 있는 시작 위치의 개수를 구할 수 있습니다.
그 뒤 모든 블록이 겹치지 않고 원형 위에 배치하는 방법은
모든 블록의 시작 위치 개수를 전부 곱하면 구할 수 있습니다.
따라서 pi(from k = 1, to k = n) M_k로 유도할 수 있습니다.
지금까지의 모든 과정을 표현한 코드가 바로
time += 1

result:int = 1
for i in range(numbers - 1, -1, -1) :
    time -= L[i] - 1
    result = result * time % MOD
이것입니다.

그 다음 원형 배치 전체 수에서 All Kill 유도 수를 구할려면 어떤 수를 곱해야 합니다.
빈 슬롯의 수가 F라고 가정할 때 F = t - sigma(x_i)라고 표현할 수 있습니다.
왜냐면 시간이 t로 주어진다면 전체 슬롯의 수는 t가 되고 그 중 문제 풀기 위해 사용된 총 슬롯 수는 sigma(x_i)입니다.

비록 문제를 해결하기 위해 원형 배치를 했으나 결국 실제 시간은 직선 상으로 나타나기 때문에
원형 배치를 다시 직선 배치로 변환해야 합니다.
이 때 시작점을 어디에 잡느냐에 대한 회전 상태는 총 t + 1 - sigma(x_i - 1)입니다.
이를 식 정리하면 t + 1 - sigma(x_i) + n = F + n + 1이 됩니다.

시작점 회전 상태 중 정상적으로 직선 위 파킹("All Kill")이 되는 회전 상태는
t + 1 - sigma(x_i)이고 이것을 다시 정리하면 F + 1이 됩니다.
따라서 p * t^n = pi(M_k) * (F + 1) / (F + n + 1)으로 유도됩니다.
이 과정을 모듈러 곱셈 역원을 활용하여 코드로 구현하면
result = result * (time - numbers) % MOD
result = result * pow(time, MOD - 2, MOD) % MOD
이렇게 구현됩니다.

마지막으로 print(result)로 코드를 출력하면 이 문제는 해결됩니다.
역시 루비 문제라 그런지 풀이가 꽤나 많이 복잡하고 어렵습니다.
"""