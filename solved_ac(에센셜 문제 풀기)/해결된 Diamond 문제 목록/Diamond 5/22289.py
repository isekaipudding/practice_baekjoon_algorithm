# 22289번(큰 수 곱셈(3)) : https://www.acmicpc.net/problem/22289
"""
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <sstream>

using namespace std;
using ll = long long;

// 큰 수 곱셈 2(15576번)은 300,000자리수 경우에도 28[ms]로 나옵니다.
// 따라서 1,000,000자리수 경우에도 1000[ms] 안에 들어갈 것으로 판단하여 이 소스 코드 그대로 제출합니다.

// 참고 자료 : https://en.wikipedia.org/wiki/Discrete_Fourier_transform_over_a_ring
// 참고 자료 : https://en.wikipedia.org/wiki/Chinese_remainder_theorem

// Number-Theoretic Transform(NTT)입니다.
// NTT 설정
template<int mod, int prim_root>
struct NTT {
    static ll modpow(ll a, ll e=mod-2) {
        ll r = 1;
        while(e) {
            if(e&1) r = r*a % mod;
            a = a*a % mod;
            e >>= 1;
        }
        return r;
    }
    // in-place
    static void ntt(vector<int>& a, bool invert) {
        int n = a.size();
        static vector<int> rev;
        static vector<int> roots{0,1};
        if((int)rev.size() != n){
            rev.assign(n,0);
            for(int i=0;i<n;i++)
                rev[i] = (rev[i>>1]>>1) | ((i&1)?n>>1:0);
        }
        if((int)roots.size() < n){
            int k = __builtin_ctz(roots.size());
            roots.resize(n);
            while((1<<k) < n) {
                // compute 2^(k+1)-th root of unity
                ll e = modpow(prim_root, (mod-1)>>(k+1));
                for(int i=1<<k; i<(1<<(k+1)); i++){
                    roots[i] = (i&1) ? (ll)roots[i>>1]*e % mod
                                     : roots[i>>1];
                }
                k++;
            }
        }
        for(int i=0;i<n;i++){
            if(i < rev[i]) swap(a[i], a[rev[i]]);
        }
        for(int len=1; len<n; len<<=1){
            for(int i=0; i<n; i += 2*len){
                for(int j=0; j<len; j++){
                    int u = a[i+j];
                    int v = (ll)a[i+j+len] * roots[len+j] % mod;
                    a[i+j] = u+v < mod ? u+v : u+v-mod;
                    a[i+j+len] = u-v>=0 ? u-v : u-v+mod;
                }
            }
        }
        if(invert){
            reverse(a.begin()+1, a.end());
            ll inv_n = modpow(n);
            for(int &x: a) x = (ll)x * inv_n % mod;
        }
    }
    // convolution : returns length = A.size()+B.size()-1
    static vector<int> multiply(const vector<int>& A, const vector<int>& B){
        int need = (int)A.size() + (int)B.size() - 1;
        int n = 1;
        while(n < need) n <<= 1;
        vector<int> fa(A.begin(), A.end()), fb(B.begin(), B.end());
        fa.resize(n); fb.resize(n);
        ntt(fa, false);
        ntt(fb, false);
        for(int i=0;i<n;i++)
            fa[i] = (ll)fa[i] * fb[i] % mod;
        ntt(fa, true);
        fa.resize(need);
        return fa;
    }
};

// 두 개의 모듈러에 대한 NTT
using NTT1 = NTT<998244353, 3>;
using NTT2 = NTT<1004535809, 3>;

// 이건 중국인의 나머지 정리(CRT)입니다.
// x ≡ a1 (mod m1), x ≡ a2 (mod m2) 를 CRT로 복원
ll crt(ll a1, ll a2) {
    static const ll m1 = 998244353, m2 = 1004535809;
    // m1_inv = inverse of m1 mod m2
    static const ll m1_inv = [](){
        // ext-gcd or Fermat's little theorem:
        // m1^(m2-2) mod m2
        ll result = 1, base = m1;
        ll e = m2-2;
        while(e){
            if(e&1) result = result * base % m2;
            base = base * base % m2;
            e >>= 1;
        }
        return result;
    }();
    ll t = (a2 - a1) % m2;
    if(t < 0) t += m2;
    ll k = t * m1_inv % m2;
    return a1 + k * m1;  // 정확한 정수 계수
}

// 큰 수 곱셈 2(15576번)에서 여러 번 테스트한 결과 6자리씩 나누는 것이 가장 효율적입니다.
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string sa, sb;
    cin >> sa >> sb;
    if(sa=="0" || sb=="0"){
        cout<<"0\n";
        return 0;
    }

    // base = 1000000 (6자리씩 그룹화)
    const int BASE = 1000000;
    // a 그룹, b 그룹
    vector<int> A, B;
    for(int i = (int)sa.size(); i>0; i-=6){
        int x = 0;
        int start = max(0, i-6);
        for(int j=start; j<i; j++){
            x = x*10 + (sa[j]-'0');
        }
        A.push_back(x);
    }
    for(int i = (int)sb.size(); i>0; i-=6){
        int x = 0;
        int start = max(0, i-6);
        for(int j=start; j<i; j++){
            x = x*10 + (sb[j]-'0');
        }
        B.push_back(x);
    }

    // NTT convolution mod1, mod2
    auto C1 = NTT1::multiply(A, B);
    auto C2 = NTT2::multiply(A, B);
    int n = C1.size();

    // CRT 로 정확한 계수 복원
    vector<ll> C(n);
    for(int i=0;i<n;i++){
        C[i] = crt(C1[i], C2[i]);
    }

    // 자리 올림(CARRY) 처리 (base 1000000)
    for(int i=0;i<n-1;i++){
        ll carry = C[i] / BASE;
        C[i] %= BASE;
        C[i+1] += carry;
    }
    // 맨 끝도 남은 캐리 확장
    while(C.back() >= BASE){
        ll carry = C.back() / BASE;
        C.back() %= BASE;
        C.push_back(carry);
    }
    // 결과 출력 : 가장 높은 그룹은 그대로, 나머지는 6자리 0패딩
    ostringstream oss;
    int m = C.size();
    oss << C[m-1];
    for(int i=m-2; i>=0; i--){
        oss << setw(6) << setfill('0') << C[i];
    }
    cout << oss.str() << "\n";
    return 0;
}
"""