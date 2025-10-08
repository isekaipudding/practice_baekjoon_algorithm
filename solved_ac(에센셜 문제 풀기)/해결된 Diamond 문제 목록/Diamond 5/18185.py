# 18185번(라면 사기(Small)) : https://www.acmicpc.net/problem/18185
import sys

input = sys.stdin.readline

# 문제 내용 다시 보니 라면매니아 교준이네 집이였군요.
# 그런데 상식적으로 집 근처에는 수많은 공장이 있을 확률이 적으므로 회사일 하는 것으로 스토리 변경했습니다.

# 라면 사기(large)에서 정가 3원, 할인가 2원으로 변경했습니다.

def minimum_cost(count_of_factory, regular_price, sale_price, delicious_ramen_counts):
    # 그리디 알고리즘을 적용하기 위해 반드시 필요한 변수
    current_c_price_count = 0  # 현재 'c' 가격으로 구매한 라면의 수
    current_non_c_price_count = 0  # 현재 단계에서 다른 인접 공장에서 구매 가능한 라면의 수
    next_c_price_count = 0  # 다음 단계에서 사용할 ‘c’ 가격으로 구매할 수 있는 라면의 수
    next_non_c_price_count = 0  # 다음 단계에서 사용할 수 있는 다른 공장에서 구매 가능한 라면의 수
    
    total_cost = 0  # 최소 비용 초기화
    
    # 그리디 알고리즘 적용
    if regular_price > sale_price:  # 오? 연속으로 사면 할인해준다고? 이건 못 참지!
        for i in range(count_of_factory - 1):  # 그런데 뭐 이리 할 일이 많아???
            total_cost += delicious_ramen_counts[i] * regular_price  # 일단 정가로 라면 몇 개 사볼까?
            
            total_cost += current_c_price_count * sale_price  # 저번에 남아 있던 라면들을 할인가로 다시 구매할 수 있지?
            total_cost += current_non_c_price_count * sale_price  # 이전에 갔던 공장에서 주문한 라면들도 할인가로 구매할 수 있네!

            # 다음 공장에서 라면을 몇 개 구매할까?
            if delicious_ramen_counts[i + 1] > delicious_ramen_counts[i]:  # 다음 공장에 라면이 더 많이 있네?
                next_c_price_count += delicious_ramen_counts[i]  # 그러면 지금 구매하는 것보다, 다음에 할인가로 살 수 있는 게 더 나을 것 같아.
                delicious_ramen_counts[i + 1] -= delicious_ramen_counts[i]  # 그러면 다음 공장에서는 그만큼 라면 수를 줄여야지.
            else:  # 그런데 다음 공장에서 라면이 그렇게 많이 없네?
                next_c_price_count += delicious_ramen_counts[i + 1]  # 그럼 남은 라면은 다음에 구매하도록 하고,
                delicious_ramen_counts[i + 1] = 0  # 다음 공장에 라면은 이제 다 팔렸으니 0으로 설정해야겠다.

            # 다음 단계에서 사용할 수 있는 라면 수 조정
            if delicious_ramen_counts[i + 1] > current_c_price_count:  # 다음 공장에 있는 라면 개수가 할인가로 구매할 수 있는 라면 수보다 많네?
                next_non_c_price_count += current_c_price_count  # 그러면 현재 할인가로 사용할 수 있는 라면 개수를 다음 공장에 추가하자.
                delicious_ramen_counts[i + 1] -= current_c_price_count  # 그러면 다음 공장에서 지금 구매할 수 있는 라면 수를 줄여야지.
            else:  # 다음 공장 라면 수가 현재 할인가로 구매할 수 있는 라면 수보다 적거나 같네?
                next_non_c_price_count += delicious_ramen_counts[i + 1]  # 그럼 다음 공장에서 구매할 수 있는 라면 개수를 기록해 두고,
                delicious_ramen_counts[i + 1] = 0  # 다음 공장에 있는 라면 수는 이제 0이야.

            # 상태 업데이트: 현재 단계의 c 가격과 다른 공장에서 구매한 라면 수를 업데이트
            current_c_price_count = next_c_price_count
            current_non_c_price_count = next_non_c_price_count
            # 초기화 작업: 다음 단계에서 사용할 수 있는 변수를 초기화
            next_c_price_count = 0
            next_non_c_price_count = 0

        # 마지막 공장에서 구매한 라면의 비용을 추가해볼까?
        total_cost += delicious_ramen_counts[count_of_factory - 1] * regular_price  # 마지막 공장에서 정가로 구매한 라면 비용이야.
        total_cost += current_c_price_count * sale_price  # 마지막 공장에서 남아 있는 라면들을 할인가로 구매할 수 있지.
        total_cost += current_non_c_price_count * sale_price  # 마지막 인접 공장에서 남아 있는 라면들도 할인가로 구매하는 거야.
        # 드디어 일 다 끝냈다!!! 오늘 야근 엄청 힘드네. 이제 퇴근해야지 오늘의 나 수고 많았어.
        
    else:  # 할인 가격 C원인데 B<=C이면 판매자가 사기를 친거야? 이러면 그냥 정가로 구매해야지.
        total_cost = regular_price * sum(delicious_ramen_counts)  # 모든 라면을 정가로 구매하는 비용 계산
        # 오늘 일 빨리 끝났다! 정시 퇴근 개꿀~~~!
    
    return total_cost  # 계산된 최소 비용 반환

N = int(input().rstrip())  # N개의 공장
L = list(map(int, input().split())) # 각 공장마다 존재하는 맛있는 라면의 개수

# 최소 비용 계산
result = minimum_cost(N, 3, 2, L) # 정가 3원, 할인가 2원으로 고정
print(result)