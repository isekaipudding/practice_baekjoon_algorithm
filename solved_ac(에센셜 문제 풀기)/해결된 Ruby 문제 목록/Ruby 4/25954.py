# 25954번(LCS 9) 문제 : https://www.acmicpc.net/problem/25954
import sys

input = sys.stdin.readline

# 가장 빠른 C++ 소스 코드를 참고하여 PyPy 말고 Python으로 TLE 피할 수 있는지 테스트 합니다.
# Python으로 안 되네요. PyPy로 얼마나 개선되는지 체크합니다.

# 이제 LCS 1부터 LCS 9까지 모든 LCS 시리즈를 다 해결했습니다!

A:str = input().rstrip()
B:str = input().rstrip()

N:int = len(A)
M:int = len(B)

# h_prev : 이전 행, h_cur : 현재 행
# 초기: h[0][j] = j (j = 0..M)
h_prev = list(range(M + 1))
h_cur = [0 for _ in range(M + 1)]

result:int = 0

for i in range(N) :
    ai = A[i]
    v = 0

    for j in range(1, M + 1) :
        up = h_prev[j] # h[!c][j]
        if ai != B[j - 1] :
            # h[c][j] = max(v, up)
            if v > up :
                value = v
            else :
                value = up
            h_cur[j] = value
            # v += up - h[c][j]
            v += up - value
        else :
            # h[c][j] = v; v = up
            h_cur[j] = v
            v = up

        diff = j - h_cur[j]
        if diff > 0 :
            result += diff * (M - j + 1)

    # 다음 행으로 넘어갈 때 스왑
    h_prev, h_cur = h_cur, h_prev

print(result)

# 참고로 188[ms] 기록이 나온 C언어 소스 코드는 다음과 같습니다.
"""
#pragma GCC optimize("Ofast","unroll-loops","no-stack-protector","fast-math")
#pragma GCC target("sse2","avx","avx2","sse4.2")

#include <stdio.h>
#include <string.h>

static char a[7002], b[7002];
static int h[2][7002];

// 안타깝게도 Python에서 루프 도는 과정에서의 비용이 무거워서 Python AC는 불가능으로 판단되었습니다.
// 그래서 C언어로 어디까지 성능 최적화 되나 호기심이 들어서 #pragma를 활용하여 최적화를 시도합니다.

int main(void) {
    if (scanf("%7000s%7000s", a + 1, b + 1) != 2) return 0;

    int n = (int)strlen(a + 1);
    int m = (int)strlen(b + 1);

    int *h0 = h[0];
    int *h1 = h[1];

    for (int j = 1; j <= m; ++j) {
        h0[j] = j;
    }

    long long result = 0;

    for (int i = 1, c = 1; i <= n; ++i, c ^= 1) {
        int *hp = (c ? h0 : h1) + 1; // j=1 위치
        int *hc = (c ? h1 : h0) + 1;
        const char *bp = b + 1;

        int v = 0;
        int w = m; // w = n이 아닌 w = m으로 해야 합니다.(25% 반례)

        int j = 1;
        for (; j <= m; ++j, --w, ++hp, ++hc, ++bp) {
            int up = *hp;
            int value;

            if (a[i] != *bp) {
                value = (v > up ? v : up);
                *hc = value;
                v += up - value;
            } else {
                value = v;
                *hc = value;
                v = up;
            }

            int diff = j - value;
            if (diff > 0) {
                result += (long long)diff * w;
            }
        }
    }

    printf("%lld\n", result);
    return 0;
}
"""