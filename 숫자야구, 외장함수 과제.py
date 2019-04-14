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
    c_answer = "" # 정답(correct_answer)
    while len(c_answer) < 3: # 정답 생성(3자리 수가 될 때까지.)
        temp = str(randint(0, 9))
        if not temp in c_answer:
            c_answer += temp
    
    while 1:
        try:
            p_answer = str(input("""0~9 사이의 서로 다른 숫자 3개를 입력하세요.
            입력한 숫자: """)) # 사용자 입력값(player_answer)
            if int(p_answer) >= 0 & int(p_answer) <= 987 & p_answer != "000": # 유효성 검사(게임 규칙)
                

    strk = 0
    ball = 0
    for i in range(0, 2 + 1): # 스트라이크/볼 확인
        if p_answer[i] == c_answer[i]: # 스트라이크 조건
            strk += 1
        elif p_answer[i] in c_answer: # 볼 조건
            ball += 1
    
    flag_rtry = 0
    while flag_rtry == 0:
        try:
            rtry = 


NumBB()