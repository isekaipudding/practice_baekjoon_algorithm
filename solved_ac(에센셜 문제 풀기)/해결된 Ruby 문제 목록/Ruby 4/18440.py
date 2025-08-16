# 18440번(LCS 7) 문제 : https://www.acmicpc.net/problem/18440
# Python 소스 코드로 하면 메모리 초과 발생하므로 C++ 소스 코드로 대체합니다.
"""
#include <bits/stdc++.h>

using namespace std;

// 원래 LCS 5 다음에는 LCS 6 도전하는 것이 맞습니다.
// 하지만 이미 히르쉬버그로 구현된 LCS 5에서 비트 집합 최적화만 하면 LCS 7 문제이네요?
// 다르게 생각해보면 LCS 7 문제를 해결하면, 출력 하나를 제거한 것이 바로 LCS 6입니다.
// 그러므로 LCS 5 소스 코드를 재활용하여 LCS 7를 먼저 해결하고 루비 문제 1+1으로 챙겨 갑니다.
// 그런데 구현하는 과정이 너무 어렵습니다.

// 참고 사이트 : https://velog.io/@bformat/BOJ-18440-LCS-7

// 설정
using U64 = unsigned long long;

// 전역 입력 문자열
static string A, B;

// A 전체 길이에 맞춘 문자별(full) 비트마스크 : masks[c][word_index]
static vector<array<U64, 1>> _dummy; // placeholder (미사용)
static vector<vector<U64>> masks, masks_rev; // size = 256 x Wfull, 역방향 추가

// 작업 버퍼들 (A 구간 길이에 맞춰 동적으로 길이 지정)
static vector<U64> S, Xbuf, Sh1, Sub, Mtmp; // 현재 상태/중간 버퍼
static vector<int> Lrow, Rrow; // L[j], R[j] (j=0...m)

// 유틸 : 비트 카운트
static inline int popcount_vector(const vector<U64>& v, int W){
    int result = 0;
    for (int i = 0; i < W; ++i) result += __builtin_popcountll(v[i]);
    return result;
}

// 유틸 : S << 1 | 1 (구간 길이 n에 맞춰 마지막 워드 마스킹)
static inline void shl1_or1(const vector<U64>& src, vector<U64>& distance, int W, int tail_bits){
    U64 carry = 0;
    for (int i = 0; i < W; ++i){
        U64 nc = src[i] >> 63;
        distance[i] = (src[i] << 1) | carry;
        carry = nc;
    }
    distance[0] |= 1ULL;
    if (tail_bits){ // 마지막 워드 마스킹
        U64 mask = (tail_bits == 64) ? ~0ULL : ((1ULL << tail_bits) - 1ULL);
        distance[W-1] &= mask;
    }
}

// distance = a - b  (자릿수 자리내림 정확히)
static inline void sub_vector(const vector<U64>& a, 
                              const vector<U64>& b,
                              vector<U64>& distance, int W)
{
    U64 borrow = 0;
    for (int i = 0; i < W; ++i) {
        U64 ai = a[i], bi = b[i];
        U64 t = ai - borrow;
        U64 b1 = (ai < borrow); // 첫 단계에서 자리내림?
        U64 d = t - bi;
        U64 b2 = (t < bi); // 두 번째 단계에서 자리내림?
        distance[i] = d;
        borrow = (b1 | b2);
    }
}

// 유틸: distance = a | b / distance = a & b / distance = ~a (inplace)
static inline void or_vector (const vector<U64>& a, const vector<U64>& b, vector<U64>& distance, int W){
    for (int i = 0; i < W; ++i) distance[i] = a[i] | b[i];
}
static inline void and_vector(const vector<U64>& a, const vector<U64>& b, vector<U64>& distance, int W){
    for (int i = 0; i < W; ++i) distance[i] = a[i] & b[i];
}
static inline void not_into(const vector<U64>& a, vector<U64>& distance, int W){
    for (int i = 0; i < W; ++i) distance[i] = ~a[i];
}

static inline void extract_mask_from(const vector<vector<U64>>& table,
                                     unsigned char c,
                                     int xl, int n,
                                     int Wfull, int Wsub, int tail_bits)
{
    const vector<U64>& full = table[c];
    int off = xl & 63; // 비트 오프셋
    int ws = xl >> 6; // 시작 워드
    for (int t = 0; t < Wsub; ++t) {
        U64 lo = (ws + t < Wfull) ? (full[ws + t] >> off) : 0ULL;
        U64 hi = 0ULL;
        if (off && ws + t + 1 < Wfull) hi = full[ws + t + 1] << (64 - off);
        Mtmp[t] = lo | hi;
    }
    if (tail_bits) {
        U64 mask = (tail_bits == 64) ? ~0ULL : ((1ULL << tail_bits) - 1ULL);
        Mtmp[Wsub - 1] &= mask;
    }
}

// L[j] = LCS(A[xl...xr], B[yl...yl+j-1])
static void lcs_prefix_bitrow(int xl, int xr, int yl, int yr,
                              int Wfull, vector<int>& out)
{
    const int n = xr - xl + 1;
    const int m = yr - yl + 1;
    const int Wsub = (n + 63) >> 6;
    const int tail_bits = (n == 0) ? 0 : ((n - 1) % 64 + 1);

    S.assign(Wsub, 0ULL);
    out[0] = 0;

    for (int j = 1; j <= m; ++j) {
        unsigned char ch = (unsigned char)B[yl + j - 1];
        extract_mask_from(masks, ch, xl, n, Wfull, Wsub, tail_bits); // ← 여기
        or_vector(S, Mtmp, Xbuf, Wsub);
        shl1_or1(S, Sh1, Wsub, tail_bits);
        sub_vector(Xbuf, Sh1, Sub, Wsub);
        not_into(Sub, S, Wsub);
        and_vector(Xbuf, S, S, Wsub);
        out[j] = popcount_vector(S, Wsub);
    }
}

// R[j] = LCS(A[xl..xr], B[yl+j..yr])  (j=0..m)
// = LCS( reverse(A[xl..xr]),  prefix_of( reverse(B[yl..yr]) ) )
static void lcs_suffix_bitrow(int xl, int xr, int yl, int yr,
                              int Wfull, vector<int>& out)
{
    const int n = xr - xl + 1;
    const int m = yr - yl + 1;
    const int Wsub = (n + 63) >> 6;
    const int tail_bits = (n == 0) ? 0 : ((n - 1) % 64 + 1);

    // 역좌표계에서의 A-sub 시작 인덱스
    const int NA = (int)A.size();
    const int rev_xl = (NA - 1 - xr); // [rev_xl .. rev_xl + n - 1]

    S.assign(Wsub, 0ULL);
    out[m] = 0;

    // Brev를 앞에서부터 스캔 : t번째 문자 = B[yr - (t-1)]
    for (int t = 1; t <= m; ++t) {
        unsigned char ch = (unsigned char)B[yr - (t - 1)];
        extract_mask_from(masks_rev, ch, rev_xl, n, Wfull, Wsub, tail_bits); // <- 역마스크
        or_vector(S, Mtmp, Xbuf, Wsub);
        shl1_or1(S, Sh1, Wsub, tail_bits);
        sub_vector(Xbuf, Sh1, Sub, Wsub);
        not_into(Sub, S, Wsub);
        and_vector(Xbuf, S, S, Wsub);
        out[m - t] = popcount_vector(S, Wsub); // suffix 인덱스로 되돌려 저장
    }
}

// 히르쉬버그 복원 (bitset DP로 L/R만 계산)
static string hirschberg(int xl, int xr, int yl, int yr, int Wfull)
{
    if (xl > xr || yl > yr) return "";
    int n = xr - xl + 1;
    int m = yr - yl + 1;

    if (n == 1){
        char c = A[xl];
        for (int j = yl; j <= yr; ++j)
            if (B[j] == c) return string(1, c);
        return "";
    }

    int mid = (xl + xr) >> 1;

    // L[j] = LCS(A[xl...mid],    B[yl...yl+j-1])  (j=0...m)
    lcs_prefix_bitrow(xl, mid, yl, yr, Wfull, Lrow);

    // R[j] = LCS(A[mid+1...xr], B[yl+j...yr])    (j=0...m)
    lcs_suffix_bitrow(mid + 1, xr, yl, yr, Wfull, Rrow);

    // k = argmax_j L[j] + R[j]
    int k = 0, best = Lrow[0] + Rrow[0];
    for (int j = 1; j <= m; ++j){
        int v = Lrow[j] + Rrow[j];
        if (v > best){ best = v; k = j; }
    }

    string left  = hirschberg(xl, mid, yl, yl + k - 1, Wfull);
    string right = hirschberg(mid + 1, xr, yl + k, yr, Wfull);
    return left + right;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> A >> B;
    const int NA = (int)A.size();
    const int NB = (int)B.size();

    // --- 전처리: A 전체에 대해 문자별(full) 비트마스크 생성 ---
    const int Wfull = (NA + 63) >> 6;
    masks.assign(256, vector<U64>(Wfull, 0ULL));
    masks_rev.assign(256, vector<U64>(Wfull, 0ULL)); // <- 역방향도 준비

    for (int i = 0; i < NA; ++i){
        unsigned char c = static_cast<unsigned char>(A[i]);
        // 정방향 비트 세우기
        masks[c][i >> 6] |= (1ULL << (i & 63));

        // ★ 역방향 좌표에도 동일 문자 위치를 세워줘야 합니다(이 두 줄을 추가하지 않아 0% 반례 발생)
        int ir = NA - 1 - i; // <- 추가
        masks_rev[c][ir >> 6] |= (1ULL << (ir & 63)); // <- 추가
    }
    /*
    위 두 줄이 없으면 lcs_suffix_bitrow()의 
    extract_mask_from(masks_rev, ch, rev_xl, n, Wfull, Wsub, tail_bits);
    부분이 항상 0으로 반환되어 반례가 발생합니다.
    */

    // 작업 버퍼들, 한 번만 최대 길이에 맞춰 확보
    S.assign(Wfull, 0ULL);
    Xbuf.assign(Wfull, 0ULL);
    Sh1.assign(Wfull, 0ULL);
    Sub.assign(Wfull, 0ULL);
    Mtmp.assign(Wfull, 0ULL);

    Lrow.assign(NB + 1, 0);
    Rrow.assign(NB + 1, 0);

    // 히르쉬버그 + 비트DP
    string lcs = hirschberg(0, NA - 1, 0, NB - 1, Wfull);
    // LCS 6의 경우는 그냥 lcs.size()만 출력하면 됩니다.
    cout << lcs.size() << '\n' << lcs << '\n';
    return 0;
}
"""