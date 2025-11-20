# 1708번(볼록 껍질) 문제 : https://www.acmicpc.net/problem/1708
import sys

input = sys.stdin.readline

def ccw(p1, p2, p3) :
    # 세 점의 방향성을 계산 (반시계 방향이면 양수, 시계 방향이면 음수, 일직선이면 0)
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def graham_scan(points) :
    # Graham Scan 알고리즘으로 볼록 껍질을 찾습니다.
    if len(points) < 3 :
        return len(points)
    
    # y좌표가 가장 작은 점을 찾고, 같다면 x좌표가 가장 작은 점을 선택
    start:tuple[int, int] = min(points, key=lambda p: (p[1], p[0]))
    
    # 시작점을 제외한 나머지 점들을 각도 순으로 정렬
    def angle_sort(p) :
        if p == start :
            return (-1, 0)
        dx:int = p[0] - start[0]
        dy:int = p[1] - start[1]
        # 각도를 계산 (atan2 사용)
        import math
        angle:float = math.atan2(dy, dx)
        # 거리가 같은 경우 거리로 정렬
        dist:int = dx*dx + dy*dy
        return (angle, dist)
    
    sorted_points:list[tuple[int, int]] = sorted(points, key=angle_sort)
    
    # 스택을 사용하여 볼록 껍질 구성
    stack:list[tuple[int, int]] = [start]
    
    for point in sorted_points:
        if point == start:
            continue
        while len(stack) >= 2 and ccw(stack[-2], stack[-1], point) <= 0:
            stack.pop()
        stack.append(point)
    
    return len(stack)

# 입력 처리
N:int = int(input().rstrip())
points:list[tuple[int, int]] = []

for _ in range(N) :
    x, y = map(int, input().rstrip().split())
    points.append((x, y))

# 결과 출력
result:int = graham_scan(points)
print(result)