"""
•필기: 동적프로그래밍 기법을 설명하고 적용 예를 한가지 들고 그에 대해 설명하라. (학번.txt)
•실기:
–A=[1,2,3,4,6,7,8,9], B=5 를 이용하여 B가 A에 있나를 찾는 순차탐색프로그램을 작성하라. B가 A에 있으면 A의 index, 없으면 “NA”을 출력하게 만들어라
– 학번.py, coding 캡쳐, 결과캡쳐  로 만들어 (총 3가지) 첨부하라

–총 4개의 file을 Smart campus에 제출하라

–시간제안이 있음에 유의하라
"""

B = 5
def SriSrch(Value):
    A = [1, 2, 3, 4, 6, 7, 8, 9]
    for i in range(len(A)):
        if Value == A[i]:
            print("Index:", i)
            return i
    print("NA")
    return "NA"

if __name__ == '__main__':
    SriSrch(B)
    