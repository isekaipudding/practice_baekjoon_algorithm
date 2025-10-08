# 1557번(제곱 ㄴㄴ) : https://www.acmicpc.net/problem/1557
import sys

input = sys.stdin.readline

# 참고 자료 : https://en.wikipedia.org/wiki/M%C3%B6bius_inversion_formula
# 참고 자료 : https://en.wikipedia.org/wiki/M%C3%B6bius_function
# 위키백과에 따르면 f 와 g가 g(n) = sigma(d|n) f(d)를 만족하면 역으로 f(n) = sigma(d|n)u(d)g(n/d)로 구할 수 있습니다.
# 우선 포함 배제의 원리로 표현하면 제곱 ㄴㄴ 개수 = sigma(from i = 1, to root(x)) [x/i^2]으로 표현됩니다.
# 그 다음 g(n) = sigma(d|n) f(d)에서 n->K, d->i^2, f(d) = 1로 변환하면 g(K) = sigma(i^2|K) 1이 됩니다.
# 여기서 f(d) = 1는 수학적으로 공식 유도하기 힘들지만 간단히 설명하면 "그냥 개수 세기"를 의미합니다.
# 이걸 다시 바꾸면 count(K) = sigma(from i = 1, to root(x)) u(i)[x/i^2]이 됩니다.
# 여기서 mu(i)는 뫼비우스의 함수입니다.(포함 배제의 원리에서 부호 역할을 합니다.)
# 증명이 너무 어려워서 자세히 설명하기 어렵습니다.

# 저런, 10^9으로 올렸더니 메모리 초과 발생했습니다. 다시 10^6으로 복귀합니다.
MAX:int = 10**6 + 10
mu:list = [1] * MAX
is_prime:list = [True] * MAX
is_prime[0] = is_prime[1] = False

# 뫼비우스 함수 전처리(에라토스테네스의 체 포함)
for i in range(2, MAX) :
    if is_prime[i] :
        for j in range(i, MAX, i) :
            is_prime[j] = False
            mu[j] *= -1
        for j in range(i * i, MAX, i * i) :
            mu[j] = 0

def count_non_square(x) :
    result:int = 0
    i:int = 1
    # 다시 확인해 보니 여기서 IndexError가 발생했습니다.
    # 따라서 IndexError를 방지하기 위해 i < len(mu)를 추가합니다.
    while i * i <= x and i < len(mu):
        result += mu[i] * (x // (i * i))
        i += 1
    return result

# 이진 탐색을 이용하여 K번째 제곱 ㄴㄴ수를 구합니다.
def find_kth_non_square(K) :
    low, high = 1, 2 * K  # 충분히 넓게
    result:int = -1
    while low <= high :
        mid:int = (low + high) // 2
        count = count_non_square(mid)
        if count >= K :
            result = mid
            high = mid - 1
        else :
            low = mid + 1
    return result

K:int = int(input().rstrip())
print(find_kth_non_square(K))