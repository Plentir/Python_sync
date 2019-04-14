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
        
        try: #임의의 수 3개 입력(중복 및 범위 밖의 수 무시, 숫자가 아닌 문자 입력 예외처리) - 한 번에 3개를 전부 받아야 함.
            n2 = input("0~9 사이의 수 중 원하는 수 3개를 고르세요: ") #입력: abc 꼴로.
            if (n2 >= 0) and (n2 <= 987):
                num_input.append(n2)
            else:
                print("0~9 사이의 수 3개가 아닙니다. 다시 선택하세요.")

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
        
        while 1: #게임 반복 여부 결정
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

if '__init__' == '__main__':
    game()
