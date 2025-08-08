# 10790번(달리기) 문제 : https://www.acmicpc.net/problem/10790
import sys
import math

input = sys.stdin.readline

def solve_case(length, first_velocity, second_velocity, time, seconds) :
    delta_velocity = second_velocity - first_velocity
    acceleration = 1 # dv / dt = 1
    speed = 0
    while time * acceleration < delta_velocity :
        if acceleration <= 0 :
            break
        segment_velocity_numerator:int = length
        segment_velocity_denominator:int = seconds * (speed + 1)
        segment_acceleration:int = 0
        if 1 < math.ceil((second_velocity * segment_velocity_denominator - segment_velocity_numerator) / (segment_velocity_denominator * time)) :
            segment_acceleration = math.ceil((second_velocity * segment_velocity_denominator - segment_velocity_numerator) / (segment_velocity_denominator * time) - 1)
        second_velocity -= segment_acceleration * time
        delta_velocity = second_velocity - first_velocity
        acceleration = 2 * (acceleration - segment_acceleration)
        speed += 1
    if acceleration <= 0 :
        return None
    else :
        return speed

T:int = int(input().rstrip())
for _ in range(T) :
    l, v1, v2, t, s = map(int, input().split())
    result = solve_case(l, v1, v2, t, s)
    print(result if result is not None else "impossible")