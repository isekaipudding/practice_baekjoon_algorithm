# 1019번(책 페이지) 문제 : https://www.acmicpc.net/problem/1019
import sys

input = sys.stdin.readline

n:int = int(input().rstrip()) # 자연수 n 입력받기
k:int = len(str(n)) - 1 # for문 초기값 설정 -> 예시로 12345이면 맨 앞 자리수의 10의 승수인 4를 k로 결정

count:list = [0]*10 # 초기값이 모두 0인 크기 10 list 생성
# 의미는 숫자 개수

for i in range(k, -1, -1) : # k부터 0까지 -1씩 해서 구하기
    index_target = n // (10**i) % 10 # 그 다음 for문 제어를 위해 타겟 인덱스 설정
    for index in range(10) : # 0부터 9까지 하나씩 숫자 카운트 시작
        # if문 구절이 바로 핵심 알고리즘입니다.
        if 0 <= index and index < index_target :
            if index == 0 and i == k : # 맨 앞 자리수는 0이 될 수 없습니다.
                continue
            count[index] += (n // (10**(i+1)) + 1) * (10**i)
        elif index == index_target :
            count[index] += (n // (10**(i+1))) * (10**i) + (n%(10**i)+1)
        elif index_target<index and index<=9 :
            count[index] += (n // (10**(i+1))) * (10**i)
            
# 중복된 0을 제거해줍니다.
for i in range(k) :
    count[0] -= 10**i

# 결과를 공백으로 구분하여 출력
print(" ".join(map(str, count)))