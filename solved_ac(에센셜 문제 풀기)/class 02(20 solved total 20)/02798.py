# 2798번(블랙잭) 문제 : https://www.acmicpc.net/problem/2798
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

max:int = 0
for i in range(0, N-2) :
    if max == M : # 실행 횟수를 줄이기 위한 코드1
        break
    for j in range(i+1, N-1) :
        for k in range(j+1, N) :
            if numbers[i] + numbers[j] + numbers[k] <= M :
                if numbers[i] + numbers[j] + numbers[k] > max :
                    max = numbers[i] + numbers[j] + numbers[k]
            else : # 실행 횟수를 줄이기 위한 코드2
                break
print(max)