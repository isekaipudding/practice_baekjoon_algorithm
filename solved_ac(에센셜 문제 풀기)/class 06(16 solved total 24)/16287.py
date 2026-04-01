# 16287번(Parcel) 문제 : https://www.acmicpc.net/problem/16287
import sys

input = sys.stdin.readline

def main() :
    W, N = map(int, input().split())
    L:list = list(map(int, input().split()))
    L.sort()

    # dp[s] = True  ⟺  지금 보고 있는 i 기준으로,
    # 인덱스 < i 에서 서로 다른 두 원소의 합이 s인 경우가 존재
    dp:list = [False for _ in range(W + 1)]

    # i : 오른쪽 쪽에서 첫 번째 원소의 인덱스 (두 번째는 j>i)
    # 최소 i=1 (왼쪽에 최소 1개), 최대 i=n-2 (오른쪽에 최소 1개 남겨야 함)
    for i in range(1, N - 1) :
        ai = L[i]

        # (1) (i, j) 를 오른쪽 두 원소로 잡고,
        #     왼쪽 두 원소의 합이 되어야 할 값 s = w - ai - L[j] 를 dp에서 찾기
        for j in range(i + 1, N) :
            s = W - ai - L[j]
            if s < 0 :
                # L는 정렬되어 있으므로 j가 커질수록 L[j]가 커지고
                # s는 더 작아지기만 함 → 더 볼 필요 없음
                break
            if s <= W and dp[s] :
                print("YES")
                return

        # (2) 이제 i를 오른쪽 끝으로 하는 왼쪽 쌍 (j, i)들을 dp에 추가
        #     다음 i+1 루프에서 사용됨
        for j in range(i) :
            s = ai + L[j]
            if s < W :
                dp[s] = True

    print("NO")

if __name__ == "__main__":
    main()