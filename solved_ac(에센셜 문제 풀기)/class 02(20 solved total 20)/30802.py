# 30802번(웰컴 키트) 문제 : https://www.acmicpc.net/problem/30802
import sys

input = sys.stdin.readline

N:int = int(input().rstrip()) # 참가자 수

clothes_size:list = list(map(int, input().split())) # 각 사이즈마다 신청한 참가자 수

T, P = map(int,input().split()) # 옷 한 묶음 당 옷의 개수, 그리고 펜 한 묶음 당 자루 수

T_set:int = 0 # 필요한 옷의 묶음 수를 0으로 초기화

for i in range(6) : # 사이즈 종류가 6가지이므로 range(6)으로 설정
    T_set += clothes_size[i] // T # 모든 사람한테 공평하게 나눌 수 있는 묶음 수 구하기
    # T_set으로 해야 하는데 T_Set으로 해서 NameError 발생. 오타를 수정해서 해결
    if clothes_size[i] % T : # 만약 공평하게 나눠준 뒤 여전히 부족하다면
        T_set += 1 # 1 묶음을 더 구매합니다.
print(T_set) # 필요한 옷의 묶음 수 구하기
print("{} {}".format(N // P, N % P))
# 첫번째는 필요한 펜의 묶음 수를 구해야 합니다.
# 두번째는 공평하게 나눠준 뒤 남은 펜의 수를 구합니다.