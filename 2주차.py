# else는 예외처리 용도로 씀.
# && = and, || = or 랑 같은 의미.
# if a == 1 or b == 3:는 if a == 1 || b == 3:이랑 같음.
# 
"""
input 받기.
a: 90점 이상.
b: ......
예외처리
"""
#1
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

    else: # error handling
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