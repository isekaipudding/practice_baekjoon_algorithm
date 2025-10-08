# 30919번(짧은 코드로 빠르게 많은 소수 세기) : https://www.acmicpc.net/problem/30919
# 소스 코드 최적화 시작
import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline
# 출처 : https://en.wikipedia.org/wiki/Meissel%E2%80%93Lehmer_algorithm
# 위키백과에서 먼저 알고리즘 공부한 다음, 구글링을 통해 다른 사람의 코드를 참고해서 제 스타일로 변형했습니다.
# 주석을 통해 자세한 설명을 하고 싶으나 코드 길이 제한 때문에... 하...

MAX=10**7+1
pair_of_prime_product=[2,6,30,210,2310,30030,510510]
prime_list_size=7
    
seive=[False]*MAX
count=[0]*MAX
dp=[[0]*510510 for _ in range(50)]
primes=[]

# n제곱근 구하기(이진 탐색)
def root(value, exponent) :
    low, high = 0, 10**(12//exponent)+1
    while (low+1 < high) :
        mid:int = (low+high)//2
        if mid**exponent <= value:
            low = mid
        else :
            high = mid
    return low

# 공식 적용하기
def phi(number, max_number) :
    if number == 0 :
        return max_number
    if number < 50 and max_number < 510510 :
        return dp[number][max_number]
    if number < prime_list_size :
        TEMP:int = dp[number][max_number % pair_of_prime_product[number - 1]]
        TEMP += (max_number // pair_of_prime_product[number - 1]) * dp[number][pair_of_prime_product[number - 1]]
        return TEMP
    
    prime:int = primes[number - 1]
    if max_number < MAX and prime ** 2 >= max_number :
        return count[max_number] - number + 1
    if max_number >= MAX or prime ** 3 < max_number :
        return phi(number - 1, max_number) - phi(number - 1, max_number // prime)
    
    LIMIT:int = count[root(max_number, 2)]
    result:int = count[max_number] - (LIMIT + number - 2) * (LIMIT - number + 1) // 2
    for i in range(number, LIMIT, 1) :
        result += count[max_number // primes[i]]
    
    return result

# 소수 개수 구하기
def prime_pi(number) :
    if number < MAX :
        return count[number]
    square, cubic = root(number, 2), root(number, 3)
    result:int = phi(count[cubic], number) + count[cubic] - 1
    
    for i in range(count[cubic], count[square], 1) :
        result -= prime_pi(number // primes[i]) - i
    
    return result

# 초기화
for i in range(2, MAX) :
    count[i] = count[i - 1]
    if seive[i] == False :
        count[i] += 1
        primes.append(i)
    for j in range(len(primes)) :
        if primes[j] * i >= MAX : 
            break
        seive[primes[j] * i] = True
        if i % primes[j] == 0 :
            break
for i in range(510510) :
    dp[0][i] = i
for i in range(1, 50) :
    for j in range(1, 510510) :
        dp[i][j] = dp[i-1][j] - dp[i-1][j // primes[i-1]]

T:int = int(input().rstrip())
for _ in range(T) :
    print(prime_pi(int(input().rstrip())))