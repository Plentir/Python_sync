"""
알아둘 것.
1) 프로그램 실행 시간 측정
2) 파일 입출력
3) 랜덤 함수 불러오기
4) "시간 복잡도가 ~인 알고리즘으로 문제를 해결하라." 형식으로 문제가 나올 수도 있음.
"""
#탐색 알고리즘
#순차 검색


#이진 탐색


#하노이의 탑


#피보나치 수열


#정렬 알고리즘
#버블 정렬
def BubSort(ary):
    for i in range(len(ary), 1, -1):  #배열 내의 모든 값에 대해 내부 반복 실행.(단, 이미 정렬이 끝난 값은 제외.)
        for j in range(i - 1):  #내부 반복(하나의 기준값으로 비교.)
            if ary[j] > ary[j + 1]:
                ary[j], ary[j + 1] = ary[j + 1], ary[j]  #swapping
    return ary
#합병 정렬
def MrgSort(ary):
    if len(ary) <= 1:  #재귀호출 종료점
        return ary
    mid = len(ary)//2  #분할 지점(절반으로 나누기.)
    part_l = MrgSort(ary[:mid])  #좌분할
    part_r = MrgSort(ary[mid:])  #우분할
    return Mrg(part_l, part_r)

def Mrg(ary1, ary2):  #정렬 후 병합 모듈
    res = []
    i = j = 0
    while i < len(ary1) and j < len(ary2):
        if ary1[i] > ary2[j]:
            res.append(ary2[j])
            j += 1
        else:
            res.append(ary1[i])
            i += 1
    if j >= len(ary2):
        res += ary1[i:]
    else:
        res += ary2[j:]
    return res

#퀵 정렬
from random import randint

def QkSort(ary):
    pvt = ary[randint(0, len(ary))]
    for i in range(len(ary)):
        if ary[i] < pvt:
            ary[i]

if __name__ == "__main__":
    print(BubSort([0, 12, -1, -100, 123, 22, 2, 0, 59, 91, -1, 12]))
    #print(MrgSort([0, 12, -1, -100, 123, 22, 2, 0, 59, 91, -1, 12]))
    pass