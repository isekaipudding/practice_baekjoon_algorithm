# 14425번(문자열 집합) 문제 : https://www.acmicpc.net/problem/14425
import sys

input = sys.stdin.readline

fromAtoZ_Set = [set() for _ in range(26)] # 첫글자가 a~z인 집합 생성

N, M = map(int, input().split())

for i in range(N) :
    IN:str = input().rstrip()
    # 첫글자가 아스키코드 기준으로 a(97)부터 z(122)인 경우 해당 집합에 추가
    if 97<=ord(IN[0]) and ord(IN[0])<=122 :
        fromAtoZ_Set[ord(IN[0])-97].add(IN)

count:int = 0
for i in range(M) :
    INPUT:str = input().rstrip()
    if 97<=ord(INPUT[0]) and ord(INPUT[0])<=122 :
        if INPUT in fromAtoZ_Set[ord(INPUT[0])-97] : # 해당 원소가 포함되면면 1 추가
            count += 1
            
print(count)