# 25798번(초콜릿과 친구들의 습격) 문제 : https://www.acmicpc.net/problem/25798
import sys

input = sys.stdin.readline

# 에디토리얼 : https://blog.bubbler.blue/posts/chocolate1/editorial/

T:int = int(input().rstrip())

for _ in range(T) :
    M, N, K = map(int, input().split())

    # 구멍이 없으면 그냥 전체 도미노 최대 개수
    if K == 0 :
        print(M * N // 2)
        continue

    holes:set = set()
    w_removed:int = 0
    b_removed:int = 0

    for _ in range(K) :
        m, n = map(int, input().split())
        holes.add((m, n))
        # (m + n) 짝/홀로 색 구분 (1-based 좌표 그대로 사용)
        if (m + n) % 2 == 0 :
            w_removed += 1
        else:
            b_removed += 1

    # 기본 공식 : MN/2 - max(제거된 흰칸, 제거된 검은칸)
    # 여기서 그리디 적용
    result:int = M * N // 2 - max(w_removed, b_removed)

    # 예외 처리 : K=4, 흰 2개, 검정 2개 제거 + 구석 고립
    if K == 4 and w_removed == 2 and b_removed == 2:
        isolated:bool = False
        corners:list  = [(1, 1), (1, N), (M, 1), (M, N)]

        for x, y in corners :
            # 코너 자체가 구멍이면 "고립된 코너 칸"이 아님
            if (x, y) in holes :
                continue

            if x == 1 and y == 1 :
                neighbor = [(1, 2), (2, 1)]
            elif x == 1 and y == N :
                neighbor = [(1, N - 1), (2, N)]
            elif x == M and y == 1 :
                neighbor = [(M - 1, 1), (M, 2)]
            else :  # (M, N)
                neighbor = [(M - 1, N), (M, N - 1)]

            # 이웃 두 칸이 모두 구멍이면 이 코너는 완전히 고립
            if all(nn in holes for nn in neighbor) :
                isolated = True
                break

        if isolated :
            result -= 1  # MN/2 - 2 -> MN/2 - 3

    print(result)