# 12100번(2048(Easy)) : https://www.acmicpc.net/problem/12100
import sys

input = sys.stdin.readline

MAX_TURN: int = 5 # 최대 이동 횟수 (5번)

def merge_line(line) :
    """
    1차원 리스트를 왼쪽으로 밀고,
    인접한 같은 숫자는 한 번만 합친 뒤,
    오른쪽에 0을 채워 원래 길이를 유지합니다.
    """
    out:list = [] # 합병 후 숫자들을 담을 리스트
    skip:bool = False # 직전 합병 여부 플래그
    for x in line :
        if x == 0 :
            continue  # 0은 건너뛰고
        if not skip and out and out[-1] == x :
            # 마지막 숫자와 같고, 아직 합병하지 않았으면
            out[-1] <<= 1  # 합치기
            skip = True   # 다음에 또 합병 금지
        else :
            out.append(x)
            skip = False
    # 0을 추가하여 원래 길이로 맞추기
    return out + [0 for _ in range(len(line) - len(out))]


def move(board, direction) :
    """
    board를 복사하지 않고 새로운 new 보드를 만들어
    direction에 따라 타일을 이동 및 합칩니다.
    0 : 위
    1 : 아래
    2 : 오른쪽
    3 : 왼쪽
    """
    N:int = len(board)
    # 반환할 그래프
    new:list = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N) :
        merged:list = []
        line:list = []
        # 위/아래는 열 단위, 왼쪽/오른쪽은 행 단위 처리
        if direction in (0, 1) :
            # i번째 열 추출
            line = [board[r][i] for r in range(N)]
            if direction == 1 :
                # 아래로: 반전 -> 합병 -> 반전
                merged = merge_line(line[::-1])[::-1]
            else :
                # 위로: 그대로 합병
                merged = merge_line(line)
            # new 보드에 결과 쓰기
            for r in range(N) :
                new[r][i] = merged[r]
        elif direction in (2, 3) :
            # i번째 행 복사
            line = board[i][:]
            if direction == 2 :
                # 오른쪽: 반전 -> 합병 -> 반전
                merged = merge_line(line[::-1])[::-1]
            else:
                # 왼쪽: 그대로 합병
                merged = merge_line(line)
            new[i] = merged

    return new


def solve(graph) :
    """
    최대 5번 이동 조합을 모두 시도해보고,
    보드 내 최대 타일 값을 반환합니다.
    """
    if N == 1 :
        return graph[0][0]

    result:int = 0
    # 이동 방향 조합 수: 4^(MAX_TURN)
    for time in range(1 << (2 * MAX_TURN)) :
        copy:list = graph
        TEMP:int = time
        for _ in range(MAX_TURN) :
            # 비트마스크 알고리즘 사용
            direction = TEMP & 3  # 하위 2비트
            TEMP >>= 2           # 다음 2비트로 이동
            copy = move(copy, direction)
        # 보드 전체를 탐색하며 최대값 갱신
        for r in range(N) :
            for c in range(N) :
                result = max(result, copy[r][c])

    return result

# 입력 처리
N:int = int(input().rstrip())
board:list = [list(map(int, input().split())) for _ in range(N)]
print(solve(board))