#숫자야구
'''
규칙
1. 0~9까지의 서로 다른 숫자를 한번에 3개를 입력받는다. ex) 123, 982, 263, ...
2. 0~9까지의 서로 다른 숫자 3개로 이루어진 무작위 숫자를 만든다. (정답으로 사용.)
3. 1과 2의 숫자에서, 각 자리의 숫자에 대해 위치와 숫자가 답과 모두 같으면 '스트라이크', 자리는 다르지만 숫자가 같으면 '볼'.
4. 3 스트라이크 = 아웃
'''
from random import randint

def NumBB():
    c_ans = ""
    while len(c_ans) < 3: # 정답 생성(3자리 수가 될 때까지.)
        temp = str(randint(0, 9))
        if not temp in c_ans:
            c_ans += temp

    hist_ans = []
    flag_rtry = 1 # 게임 반복 여부. 1 = 반복, 0 = 종료
    while flag_rtry == 1:

        flag_inp = 0
        while flag_inp == 0: # 유효한 값을 받을 때까지 반복
            try:
                p_ans = str(input("""0부터 9까지의 서로 다른 정수 3개를 입력하세요.
입력한 숫자: """))
                if int(p_ans) ==
            except ValueError: # int("str") = ValueError 오류
                print("숫자가 아닌 문자가 포함되어 있습니다.\n")
                flag_inp = 0
        hist_ans.append(int(p_ans)) # 입력값 저장

        strk = 0
        ball = 0
        for j in range(3): # 스트라이크/볼 확인
            if p_ans[j] == c_ans[j]: # 스트라이크 조건
                strk += 1
            elif p_ans[j] in c_ans: # 볼 조건
                ball += 1

        if strk == 3: # 게임 결과 출력
            print("""%sS, %sB.
3 strikes OUT!
게임 횟수: %s
게임 기록: %s\n""" %(strk, ball, len(hist_ans), hist_ans))
        else:
            print("""%sS, %sB.
게임 횟수: %s
게임 기록: %s\n""" %(strk, ball, len(hist_ans), hist_ans))

        while 1: # 게임 반복 여부 확인
            rtry = input("게임을 계속 하시겠습니까? y/n\n")
            if rtry == "y":
                flag_rtry = 1
                break
            elif rtry == "n":
                flag_rtry = 0
                break
            else:
                input("y 또는 n으로 입력해 주십시오.\n")
NumBB()
