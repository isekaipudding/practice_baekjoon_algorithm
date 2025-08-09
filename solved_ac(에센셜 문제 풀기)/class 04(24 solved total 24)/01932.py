# 1932번(정수 삼각형) 문제 : https://www.acmicpc.net/problem/1932
import sys

input = sys.stdin.readline

N:int = int(input().rstrip())

# 다이나믹 알고리즘을 활용해서 풀었습니다.
dp:list = []

for i in range(N) :
    numbers:list=list(map(int,input().split()))
    for j in range(len(numbers)) :
        if i == 0 : # 맨 처음에는 자동으로 원소 추가
            dp.append(numbers[j]) # 초기식
        else :
            # 아래에 있는 식은 모두 점화식입니다.
            if j==0 : # 가장 왼쪽의 수는 비교하지 않고 더하기
                numbers[0] = numbers[0] + dp[0]
            elif 0<j and j<len(numbers)-1 : # 여기가 많이 복잡합니다.
                numbers[j] = max(numbers[j] + dp[j-1], numbers[j] + dp[j])
            elif j==len(numbers)-1 : # 가장 오른쪽의 수는 비교하지 않고 더하기
                dp.append(numbers[j] + dp[j-1])
    for j in range(0,len(numbers)-1,1) : # 임시저장된 수들을 dp 배열에 저장하기
        dp[j] = numbers[j]
        
print(max(dp))