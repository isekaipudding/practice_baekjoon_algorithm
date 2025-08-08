# 2239번(스도쿠) 문제 : https://www.acmicpc.net/problem/2239
import sys

input = sys.stdin.readline

def square(x, y) :
    return (x // 3) * 3 + (y // 3)

def go(z) :
    if z == 81 :  # 모든 셀을 채웠을 때
        for i in range(n) :
            print("".join(map(str, a[i])))  # 공백으로 숫자 출력
        return True  # 최초로 찾은 해답을 찾은 즉시 종료

    x = z // n  # 현재 x 좌표
    y = z % n   # 현재 y 좌표
    if a[x][y] != 0 :  # 이미 채워져 있으면 다음으로 이동
        return go(z + 1)
    else:
        for i in range(1, 10) :  # 숫자 1부터 9까지 시도
            if not c[x][i] and not c2[y][i] and not c3[square(x, y)][i] :
                # 사용 마킹
                c[x][i] = True
                c2[y][i] = True
                c3[square(x, y)][i] = True
                a[x][y] = i
                
                if go(z + 1) :  # 다음 위치 시도
                    return True
                
                # 실패 시 원래대로 되돌리기
                a[x][y] = 0
                c[x][i] = False
                c2[y][i] = False
                c3[square(x, y)][i] = False
    return False

# 전역 변수 설정
n = 9
a = [[0] * n for _ in range(n)]  # 9x9 스도쿠 보드
c = [[False] * 10 for _ in range(10)]  # 각 숫자 사용 여부
c2 = [[False] * 10 for _ in range(10)]  # 각 열 체크
c3 = [[False] * 10 for _ in range(10)]  # 3x3 블록 체크

# 입력 받기
for i in range(n) :
    row_input = list(map(int, input().rstrip()))  # 공백으로 잘라서 리스트로 변환
    for j in range(n) :
        a[i][j] = row_input[j]
        if a[i][j] != 0 :
            c[i][a[i][j]] = True
            c2[j][a[i][j]] = True
            c3[square(i, j)][a[i][j]] = True

# 스도쿠 풀이 실행
go(0)