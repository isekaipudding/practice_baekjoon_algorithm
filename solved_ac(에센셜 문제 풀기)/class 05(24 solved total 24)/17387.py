# 17387번(선분 교차 2) 문제 : https://www.acmicpc.net/problem/17387
import sys

input = sys.stdin.readline

# CCW(11758) 문제에 활용한 ccw 알고리즘 소스 코드를 여기에 재활용합니다.
# 선분 s->e가 각 벡터의 성분은 (도착 지점)-(출발 지점)으로 표현됩니다.
# 선분 A->B = (x2-x1)i + (y2-y1)j + 0 * k
# 선분 B->C = (x3-x2)i + (y3-y2)j + 0 * k
# 외적을 하면 회전 방향을 알 수 있습니다.
"""
(A->B) x (B->C)
= {(y2-y1)*0 - 0*(y3-y2)}i + {0*(x3-x2) - (x2-x1)*0}j + {(x2-x1)*(y3-y2) - (y2-y1)*(x3-x2)}k
= {(x2-x1)*(y3-y2) - (y2-y1)*(x3-x2)} k
"""
def ccw(x1, y1, x2, y2, x3, y3) :
    return (x2-x1)*(y3-y2) - (y2-y1)*(x3-x2)

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# 일직선 상에 세 점이 존재하는 경우가 있으므로 두 ccw 곱이 0보다 "작거나 같으면" 교차한 것으로 간주합니다.
if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0 :
    # 예외 사항에 의해 이것도 두 ccw 곱이 0보다 "작거나 같으면" 교차한 것으로 간주합니다.
    if ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) <= 0 :
        # 두 선분이 모두 하나의 일직선 상에 있는 예제 입력 7에서 또 예외 사항 발생.
        if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) == 0 :
            MIN_X, MAX_X, MIN_Y, MAX_Y = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)
            # L2의 양 끝점이 단 하나라도 L1 선분 안에 있는 경우
            if (MIN_X <= x3 <= MAX_X and MIN_Y <= y3 <= MAX_Y) or (MIN_X <= x4 <= MAX_X and MIN_Y <= y4 <= MAX_Y) :
                print(1)
            # 여기서 10% 반례 발생. L2의 양 끝점이 둘 다 L1 선분 안에 없어도 두 선분이 겹치는 경우가 존재합니다.
            # 아래의 조건식은 L1 좌표 범위에서 L2의 양 끝점이 모두 최소값보다 작거나 혹은 모두 최대값보다 큰 경우 교차하지 않는 것으로 간주합니다.
            elif (x3 < MIN_X and x4 < MIN_X) or (y3 < MIN_Y and y4 < MIN_Y) or (MAX_X < x3 and MAX_X < x4) or (MAX_Y < y3 and MAX_Y < y4) :
                print(0)
            else :
                print(1) 
        # 두 ccw 곱이 0보다 작은 경우이므로 무조건 두 선분은 교차합니다.
        else :
            print(1)
    else :
        print(0)
else :
    print(0)