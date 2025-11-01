# 1620번(나는야 포켓몬 마스터 이다솜) 문제 : https://www.acmicpc.net/problem/1620
import sys

input = sys.stdin.readline

map_key_int = [{} for _ in range(10)]  # 10개의 빈 딕셔너리로 이루어진 리스트
map_key_str = [{} for _ in range(26)]  # 26개의 빈 딕셔너리로 이루어진 리스트

N, M = map(int, input().split())

# 입력부
for i in range(1, N + 1):
    IN: str = input().rstrip()
    map_key_int[i % 10][i] = IN  # 책 분류할 때 맨 뒤 자리수 기준으로 분류합니다.
    
    IN_1ST_LOWER = IN[0].lower()
    IN_STR_INDEX = (ord(IN_1ST_LOWER) - ord('a')) % 26  # 알파벳 기준으로 분류합니다.
    map_key_str[IN_STR_INDEX][IN] = i

# 출력부
for i in range(1, M + 1):
    IN: str = input().rstrip()
    try:  # 정수를 입력하면 문자열로 출력합니다.
        NUMBER = int(IN)  # 입력을 정수로 변환
        INT_TO_STR = map_key_int[NUMBER % 10].get(NUMBER)  # 해당 값을 가져옵니다.
        if INT_TO_STR is not None:
            print(INT_TO_STR)  # 값을 출력합니다.
    except ValueError:  # 문자열로 입력하면 정수로 출력합니다.
        IN_1ST_LOWER = IN[0].lower()
        IN_STR_INDEX = (ord(IN_1ST_LOWER) - ord('a')) % 26  # 수정된 부분
        STR_TO_INT = map_key_str[IN_STR_INDEX].get(IN)
        if STR_TO_INT is not None:
            print(STR_TO_INT)