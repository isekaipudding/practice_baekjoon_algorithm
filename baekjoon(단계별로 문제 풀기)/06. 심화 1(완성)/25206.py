# 25206번(너의 평점은) 문제 : https://www.acmicpc.net/problem/25206
import sys

input = sys.stdin.readline

credit_total:int = 0
score_total:int = 0
while True :
    try :
        subject, credit, grade = map(str, input().split())
        # 아스키코드에서 49는 '1', 52는 '4'
        if 49 <= ord(credit[0]) and ord(credit[0]) <= 52 :
            if grade == "A+" :
                credit_total += ord(credit[0]) - 48
                score_total += 9 * (ord(credit[0]) - 48)
            elif grade == "A0" :
                credit_total += ord(credit[0]) - 48
                score_total += 8 * (ord(credit[0]) - 48)
            elif grade == "B+" :
                credit_total += ord(credit[0]) - 48
                score_total += 7 * (ord(credit[0]) - 48)
            elif grade == "B0" :
                credit_total += ord(credit[0]) - 48
                score_total += 6 * (ord(credit[0]) - 48)
            elif grade == "C+" :
                credit_total += ord(credit[0]) - 48
                score_total += 5 * (ord(credit[0]) - 48)
            elif grade == "C0" :
                credit_total += ord(credit[0]) - 48
                score_total += 4 * (ord(credit[0]) - 48)
            elif grade == "D+" :
                credit_total += ord(credit[0]) - 48
                score_total += 3 * (ord(credit[0]) - 48)
            elif grade == "D0" :
                credit_total += ord(credit[0]) - 48
                score_total += 2 * (ord(credit[0]) - 48)
            elif grade == "F" :
                credit_total+=ord(credit[0]) - 48
                score_total += 0 * (ord(credit[0]) - 48)
    except :
        print(score_total / (2 * credit_total))
        break