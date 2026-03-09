# 2862번(수학 게임) : https://www.acmicpc.net/problem/2862
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())

dp:list = []
# 초기식
dp.append(1)
dp.append(1)
TEMP:int = 1
while TEMP <= N :
    TEMP = dp[-1] + dp[-2]
    if TEMP <= N :
        dp.append(TEMP)

result:int = N
while True :
    if result in dp : # 만약 결과값이 피보나치 수이면
        print(result) # 해당 피보나치 수로 출력하고 프로그램 종료합니다.
        break
    else :
        result -= dp[-1] # 최대 피보나치 수로 뺍니다.
        # dp 리스트 자체를 초기화하고 result보다 작거나 같은 피보나치 수열로 다시 만듭니다.
        dp.clear()
        dp.append(1)
        dp.append(1)
        TEMP:int = 1
        while TEMP <= result :
            TEMP = dp[-1] + dp[-2]
            if TEMP <= result :
                dp.append(TEMP)
                
"""
처음부터 제 턴일 때 동전의 개수가 피보나치 수이면 처음부터 동전을 다 가지는 경우 외에는 전부 패배합니다.
이것으로 반대로 생각해보면?
상대 턴일 때 피보나치 수로 만들면 상대는 동전을 다 가질 수 없으니 상대는 무조건 패배하게 됩니다.

이 게임의 핵심 전략은 "상대 턴일 때 동전의 개수를 피보나치 수로 만들기"입니다.

예시로 동전의 개수를 12개라고 가정합니다.
그러면 12-8 -> 4-3 -> 1개만 들고 오면 됩니다.

제가 먼저 1개 가져옵니다.
그러면 동전은 11개만 남게 되고 상대는 1개 혹은 2개만 가져올 수 있습니다.
그 뒤 상대는 무슨 수를 써도 무조건 패배하게 됩니다.
왜냐면 상대가 1개 가져오면 제가 2개를 들고 와서 상대 턴일 때 8개(피보나치 수) 만들고
상대가 2개 가져오면 제가 1개를 들고 와서 상대 턴일 때 8개(피보나치 수)로 만듭니다.
상대 턴일 때 상대가 할 수 있는 것은 항복하고 다음 게임에서 가위바위보에서 이기고 선공을 가져오는 것 뿐입니다.
"""