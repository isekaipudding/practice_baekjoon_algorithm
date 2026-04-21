# 11852번(Round words) 문제 : https://www.acmicpc.net/problem/11852
"""
#include <bits/stdc++.h>

using namespace std;

using U64 = unsigned long long;

vector<vector<U64>> masks;
vector<U64> S, Xbuffer, Sh1, Sub;

int get_max_circular_lcs(const string& B_target, int W, int T) {
    int M = B_target.size();
    int max_lcs = 0;

    for (int s = 0; s < M; s++) {
        fill(S.begin(), S.end(), 0ULL);

        for (int j = 0; j < M; j++) {
            unsigned char ch = B_target[(s + j) % M];
            const vector<U64>& Mtemp = masks[ch];

            U64 carry = 0;
            for (int i = 0; i < W; i++) {
                Xbuffer[i] = S[i] | Mtemp[i];
                U64 nc = S[i] >> 63;
                Sh1[i] = (S[i] << 1) | carry;
                carry = nc;
            }
            Sh1[0] |= 1ULL;
            
            if (T) {
                U64 mask = (T == 64) ? ~0ULL : ((1ULL << T) - 1ULL);
                Sh1[W - 1] &= mask;
            }

            U64 borrow = 0;
            for (int i = 0; i < W; ++i) {
                U64 t = Xbuffer[i] - borrow;
                U64 b1 = (Xbuffer[i] < borrow);
                U64 d = t - Sh1[i];
                U64 b2 = (t < Sh1[i]);
                Sub[i] = d;
                borrow = b1 | b2;
            }

            for (int i = 0; i < W; i++) S[i] = Xbuffer[i] & (~Sub[i]);
        }

        int current_lcs = 0;

        for (int i = 0; i < W; ++i) current_lcs += bitset<64>(S[i]).count();
        
        max_lcs = (current_lcs > max_lcs) ? current_lcs : max_lcs;
    }
    
    return max_lcs;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string A, B; cin >> A >> B;

    int A_size = A.size();
    int B_size = B.size();

    if(A_size < B_size) swap(A, B);

    int N = A.size();
    int M = B.size();

    int W = (N + 63) >> 6;
    int T = (N == 0) ? 0 : ((N - 1) % 64 + 1);

    masks.assign(256, vector<U64>(W, 0ULL));
    S.assign(W, 0ULL);
    Xbuffer.assign(W, 0ULL);
    Sh1.assign(W, 0ULL);
    Sub.assign(W, 0ULL);

    for (int i = 0; i < N; ++i) {
        unsigned char c = static_cast<unsigned char>(A[i]);
        masks[c][i >> 6] |= (1ULL << (i & 63));
    }

    int result = get_max_circular_lcs(B, W, T);

    string reverseB = B;
    reverse(reverseB.begin(), reverseB.end());
    result = max(result, get_max_circular_lcs(reverseB, W, T));

    cout << result << '\n';

    return 0;
}
"""