# 22222번(지애 상수) 문제 : https://www.acmicpc.net/problem/22222

# 이건 실제 정답의 뒷자리 22자리수도 포함했습니다. 정답 유무를 검토할 때 유용하게 사용해주세요.
print("0.4227021810348385578570...3208333444876783973337")

from decimal import Decimal, getcontext, ROUND_HALF_UP 
# from tqdm import tqdm
from multiprocessing import Pool
import os

# 참고 블로그 : https://infossm.github.io/blog/2025/01/31/problem-solving-22222/
# 참고 소스 코드 : https://github.com/Creeper0809/Algorithm/blob/main/Solve/%EC%88%98%ED%95%99/22222.py

# ==============================================================================
# 1. 초기 설정 (Initialization)
# ==============================================================================

# 최대 차수(N) 설정
MAX_N = 1000
# 출력 소수 자릿수 (문제 요구: 222자리)
PRINT_DIGITS = 222

# 안전 여유(경험치): Wynn-ε 가속 기준 160~200 권장
SAFETY = 200

# MAX_N에 비례한 보정(느린 수렴 구간 대비용): N//5 정도
PREC = PRINT_DIGITS + max(SAFETY, MAX_N // 5)
getcontext().prec = PREC

# 이후 소스 코드는 제가 올린 링크를 참고해주세요.