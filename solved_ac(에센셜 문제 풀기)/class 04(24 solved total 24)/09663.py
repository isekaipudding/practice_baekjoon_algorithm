# 9663번(N-Queen) 문제 : https://www.acmicpc.net/problem/9663
import sys

input = sys.stdin.readline

# 총 6가지 알고리즘이 사용되었습니다. 하나하나 다 중요한 알고리즘이군요.
 #나무위키에 있는 알고리즘을 변형했습니다.

def n_queens(n) :
    # 4. 깊이 우선 탐색 (Depth-First Search)
    # 재귀 호출 방식으로 N-Queens 문제를 해결하는 함수
    def solve(row, cols, d1, d2):
        # 1. 백트래킹 (Backtracking)
        # 모든 퀸이 배치되었을 경우
        if row == n:
            return 1  # 경우의 수 반환
        
        count = 0
        for col in range(n):
            # 5. 유망성 검사
            # 충돌 검사: 열, 주 대각선, 부 대각선의 사용 여부 확인
            if cols[col] or d1[row - col + n - 1] or d2[row + col]:
                continue  # 충돌이 있을 경우 다음 열로 넘어감
            
            # 2. 비트마스크 (Bitmask) 사용
            # 퀸을 배치 - 백트래킹 (Backtracking) 구현
            cols[col] = d1[row - col + n - 1] = d2[row + col] = 1
            count += solve(row + 1, cols, d1, d2)  # 다음 행으로 재귀 호출

            # 6. 재귀적 상태 저장
            # 퀸 제거 - 이전 상태로 되돌림
            cols[col] = d1[row - col + n - 1] = d2[row + col] = 0 

        return count

    # 3. 공간 복잡도 최적화
    # 각 열의 사용 여부를 나타내는 배열
    cols = [0 for _ in range(n)]
    # 주 대각선과 부 대각선을 위한 배열
    d1 = [0 for _ in range(2 * (n - 1) + 1)]  # 주 대각선의 사용 여부
    d2 = [0 for _ in range(2 * n)]  # 부 대각선의 사용 여부
    
    return solve(0, cols, d1, d2)  # N-Queens 문제 해결 함수 호출

# 사용자로부터 n 입력받기
n = int(input().rstrip())
print(n_queens(n))  # 경우의 수 출력