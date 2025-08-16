# 16644번(Easy Problem) : https://www.acmicpc.net/problem/16644
# Python 대신 C언어로 해결했습니다. 아래는 C언어 소스 코드입니다.
"""
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>
#include <stdint.h>

// 그냥 말도 안 됩니다. 이게 어떻게 루비 5 밖에 안 됩니까? 구현 난이도가 루비 4입니다.

#define MXK 17000001LL
#define HASH_BITS 21
#define HASH_SIZE (1<<HASH_BITS)
#define HASH_MASK (HASH_SIZE-1)

// 전역 배열
static bool is_prime[MXK];
static long long mu[MXK];
static long long SF_DP[MXK];

// 해시 테이블 (open addressing, linear probe)
static long long hashmap_keys[HASH_SIZE];
static long long hashmap_values[HASH_SIZE];
static bool hashmap_used[HASH_SIZE];

// 간단한 64비트 해시 함수
static inline size_t hash_index(uint64_t x) {
    // MurmurHash3's fmix64 스텝 일부
    x ^= x >> 33;
    x *= 0xff51afd7ed558ccdULL;
    return (size_t)(x & HASH_MASK);
}

// 해시에서 key 조회
bool hash_get(long long key, long long *out) {
    size_t index = hash_index((uint64_t)key);
    while (hashmap_used[index]) {
        if (hashmap_keys[index] == key) {
            *out = hashmap_values[index];
            return true;
        }
        index = (index + 1) & HASH_MASK;
    }
    return false;
}

// 해시에 key -> value 저장
void hash_put(long long key, long long value) {
    size_t index = hash_index((uint64_t)key);
    while (hashmap_used[index]) {
        if (hashmap_keys[index] == key) {
            hashmap_values[index] = value;
            return;
        }
        index = (index + 1) & HASH_MASK;
    }
    hashmap_used[index] = true;
    hashmap_keys[index] = key;
    hashmap_values[index] = value;
}

// 사전 계산: μ 함수와 SF_DP 계산 (𝚺μ(i))
void init_sieve() {
    // (1) is_prime, mu 전부 초기화
    for (long long i = 0; i < MXK; i++) {
        is_prime[i] = true;
        mu[i]       = 1;      // ★ 모든 mu[i]=1로 시작
    }
    mu[1] = 1;
    SF_DP[0] = 0;
    SF_DP[1] = 1;

    for (long long i = 2; i < MXK; i++) {
        if (is_prime[i]) {
            // i는 소수
            mu[i] = -1;
            for (long long j = i*2; j < MXK; j += i) {
                is_prime[j] = false;
                mu[j] = -mu[j];
            }
            long long ii = i * i;
            for (long long j = ii; j < MXK; j += ii) {
                mu[j] = 0;     // 제곱인수 제거
            }
        }
        // -> 이제 else 분기는 절대 필요 없습니다.
        SF_DP[i] = SF_DP[i-1] + mu[i];
    }
}

// 재귀적으로 S(N) 계산 (메모이제이션 + inclusion–exclusion)
long long SF(long long N) {
    if (N < MXK) {
        return SF_DP[N];
    }
    long long cached;
    if (hash_get(N, &cached)) {
        return cached;
    }
    // 초기값 1 설정 (to avoid self-dependency)
    long long result = 1;
    hash_put(N, result);
    for (long long i = 2, j; i <= N; i = j + 1) {
        long long ni = N / i;
        j = N / ni;
        result -= SF(ni) * (j - i + 1);
    }
    hash_put(N, result);
    return result;
}

// SFI(N) 계산: sigma{i=1..√N} ( S[⌊N/i^2]) 부분 + 나머지 )
long long SFI(long long N) {
    long long result = 0;
    for (long long i = 1, j; i * i <= N; i = j + 1) {
        long long ni = N / (i * i);
        // 원본처럼 “정수 나눗셈 후”에 root를 씁니다.
        long long temp = N / ni;                    
        j = (long long) sqrtl((long double) temp);     // sqrtl → long double 버전
        result += (SF(j) - SF(i - 1)) * ni;
    }
    return result;
}

int main() {
    long long N;
    if (scanf("%lld", &N) != 1) return 0;

    // 1) sieve + μ 계산
    init_sieve();

    // 2) 초기 근사값과 이분 탐색 범위 설정
    long double pi = 3.14159265358979323846264338327950288419716939937510L;
    long double md = (long double)N / 6.0L * pi * pi;
    long long sigma = 50000;
    long long low = (md > sigma ? (long long)md - sigma : 0LL);
    long long high = (long long)md + sigma;

    // 3) 이분 탐색
    while (high - low > 1) {
        long long mid = (high + low) >> 1;
        if (SFI(mid) < N) low = mid;
        else high = mid;
    }

    // 4) 결과 출력
    printf("%lld\n", high);
    return 0;
}
"""