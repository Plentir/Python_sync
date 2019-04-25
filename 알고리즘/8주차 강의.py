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
def Fibo(n):
	seq = [0, 1]
	if n >= 2:
		for i in range(2, n + 1):
			seq.append(seq[i - 1] + seq[i - 2])
		return seq[-1]
	elif n == 1:
		return seq[1]
	elif n == 0:
		return seq[0]
	else:
		return "NA"
		
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
    if len(ary) <= 1:
        return ary

    pivot = ary[randint(0, len(ary) - 1)]
    less = []
    more = []
    equal = []
    for a in ary:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)
    return QkSort(less) + equal + QkSort(more)

if __name__ == "__main__":
    a = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15, 16]
    b = [16, 15, 14, 13, 12, 11, 10, 10, 9, 8, 7, 6, 5, 4, 4, 4, 3, 2, 1]
    c = [16, 14, 14, 12, 10, 8, 8, 8, 6, 6, 4, 2, 0, 0, 0, 0, -2, -4, -6]
    d = [1, 10, -1, 234, 11, 10, 0, -13, 412, 22, 45, -101, -7, -7, -7, 1]
    e = [0, 12, -1, -100, 123, 22, 2, 0, 59, 91, -1, 12]
    print(BubSort(d))
    print(MrgSort(d))
    print(QkSort(d))
    #print(QkSort(d))
