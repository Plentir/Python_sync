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
                p_ans = input("""\n0부터 9까지의 서로 다른 정수 3개를 입력하세요.
입력한 숫자: """)
                if int(p_ans) >= 0 and int(p_ans) <= 999 and len(p_ans) == 3: # 음수 및 자리 수 판별, ValueError 트리거.
                    for i in p_ans:
                        if p_ans.count(i) != 1 : # 각 자리 숫자 중복 여부 판별
                            flag_inp = 0
                            print("중복된 숫자가 있습니다.\n")
                            break
                        else:
                            flag_inp = 1
                else:
                    print("0부터 9까지의 수로 이루어진 세 자리 수가 아닙니다.\n")
            except ValueError: # 숫자가 아닌 자료형 판별
                print("숫자가 아닌 문자가 포함되어 있습니다.\n")
                flag_inp = 0
        #hist_ans.append(int(p_ans)) # 입력값 저장

        strk = 0
        ball = 0
        for j in range(3): # 스트라이크/볼 확인
            if p_ans[j] == c_ans[j]: # 스트라이크 조건
                strk += 1
            elif p_ans[j] in c_ans: # 볼 조건
                ball += 1

        hist_ans.append((int(p_ans), "%sS" %strk, "%sB" %ball)) # 지난 게임 결과 기록
        if strk == 3: # 게임 결과 출력
            print("""\n%sS, %sB.
3 strikes OUT!
게임 횟수: %s
게임 기록: %s\n
게임을 종료합니다.""" %(strk, ball, len(hist_ans), hist_ans))
            return 1 # 종료
        else:
            print("""\n%sS, %sB.
게임 횟수: %s
게임 기록: %s\n""" %(strk, ball, len(hist_ans), hist_ans))

        while 1: # 게임 반복 여부 확인(틀린 경우.)
            rtry = input("게임을 계속 하시겠습니까? (y/n)\n")
            if rtry == "n":
                flag_rtry = 0
                print("\n게임을 종료합니다.")
                return 1 # 종료
            elif rtry == "y":
                flag_rtry = 1
                break
            else:
                print("y 또는 n으로 입력해 주십시오.\n")

if __name__ == "__main__":
    NumBB()
