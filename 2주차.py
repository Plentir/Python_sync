# else�� ����ó�� �뵵�� ��.
# && = and, || = or �� ���� �ǹ�.
# if a == 1 or b == 3:�� if a == 1 || b == 3:�̶� ����.
# 
"""
input �ޱ�.
a: 90�� �̻�.
b: ......
����ó��
"""
"""
#1: 점수를 입력받고 그 점수가 몇 등급(A~F)인지 알려준다. 이 과정을 특정 조건을 만족하기 전까지 무한히 반복하도록 코드 작성하기.
flag = 1
while flag == 1:
    score = int(input("Your score: "))
    if score >= 90 and score <= 100:
        print("Your grade: A")

    elif score >= 80 and score < 90:
        print("Your grade: B")

    elif score >= 70 and score < 80:
        print("Your grade: C")

    elif score >= 60 and score < 70:
        print("Your grade: D")

    elif score < 60 and score >= 0:
        print("Your grade: F")
"""
"""
    else: # error handling = 예외처리. try에 해당하는 조건에 해당하면 except에 있는 명령들을 실행한다.
        try:
        except: "error name"
            print("Input type error.")

    ind = input("Keep going? (y/n): ")
    if ind == "n":
        flag = 0
    elif ind == "y":
        flag = 1
    else:
        print("Input error")
<<<<<<< HEAD
"""

# 숫자 야구 만들기
"""
1. 랜덤(0~9 사이)으로 서로 다른 값 3개 받기.
2. 자릿수 = 숫자: 스트라이크, 자릿수 != 숫자 볼
3. 3스트라이크 = 아웃
ps. 중복되는 숫자를 주는 것도, 입력받는 것도 안 됨.
"""

import random

def game():
    num_sol = []
    while len(num_sol) <= 2: #난수 3개 생성(중복 제외)
        n = random.randint(0, 9)
        if not n in num_sol:
            num_sol.append(n)

    storage = []
    while 1: #게임 반복
        num_input = []
        balls = 0
        strikes = 0
        
        while len(num_input) <= 2: #임의의 수 3개 입력(중복 및 범위 밖의 수 무시, 숫자가 아닌 문자 입력 예외처리)
            try:
                n2 = int(input("0~9 사이의 수 중 원하는 수를 고르세요: "))
                if (not n2 in num_input) & (n2 >= 0) & (n2 <= 9):
                    num_input.append(n2)
                elif n2 in num_input:
                    print("이미 선택한 수입니다. 다른 수를 선택하세요.")
                else:
                    print("0~9 사이의 수가 아닙니다. 다른 수를 선택하세요.")

            except ValueError:
                print("숫자가 아닌 값을 입력했습니다. 0~9 사이의 수를 선택하세요.")
        storage.append(num_input)

        for i in range(3): #스트라이크, 볼 확인
            if num_input[i] == num_sol[i]:
                strikes += 1
            elif num_input[i] in num_sol:
                balls += 1

        if strikes == 3: #승리 및 패배 조건 확인
            print("지금까지 골랐던 수: %s\n%s strikes, Out!\n총 게임 횟수: %s회\n" %(storage, strikes, len(storage)))
        else:
            print("지금까지 골랐던 수: %s\n%sS, %sB.\n총 게임 횟수: %s회\n" %(storage, strikes, balls, len(storage)))
        
        while 1:
            retry = input("게임을 계속 하시겠습니까? y/n\n")
            try:
                if retry == "n":
                    print("게임을 종료합니다.")
                    return 0
                elif retry == "y":
                    break
                else:
                    print("y 또는 n으로 입력해 주세요.\n")

            except ValueError:
                print("y 또는 n으로 입력해 주세요.\n")
game()
