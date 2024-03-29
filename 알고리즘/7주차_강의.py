# 버블 정렬
def BbSort(ary):
    # a[i], a[i+1] = a[i+1], a[i] 라고 쓰면 둘의 자리가 바뀜. Packing-Unpacking
    for i in range(len(ary) - 1, 0, -1):
        flag = 1
        for j in range(i):
            if (ary[j] > ary[j + 1]):
                ary[j], ary[j + 1] = ary[j + 1], ary[j]
                flag = 0
        if flag == 0:
            print(ary)
            return ary
    print(ary)
    return ary
"""
# 합병 정렬
def MrgSort(ary):
    i = low = 0
    high = len(ary)
    j = mid = (i + high)/2
    res_ary = []
    while (i < mid and j < high):

        if ary[i] < ary[j]:
            res_ary[k] = ary[i]
            i += 1
        else:
            res_ary[k] = ary[j]
            j += 1
    print(res_ary)
    return res_ary

    ary_p1 = ary[:len(ary)/2]
    ary_p2 = ary[len(ary)/2:]
    res_ary = []
    for i in range(len(ary)):

        if ary_p1[i] > ary_p2[j]:
            res_ary[k] = ary_p1[i]
        else:
            res_ary[k] = ary_p2[j]
"""
# 퀵 정렬
from random import randint

def QkSort(ary, srt, end):
    part_ary = ary[srt : end]
    pvt = ary[0]
    idx_dst = 1
    for i in range(1, len(ary) - 1):
        if ary[i] > pvt and ary[i + 1] < pvt:
            ary[i], ary[i + 1] = ary[i + 1], ary[i]
            idx_dst += 1 # pvt(ary[0])와 자리를 바꿀 요소의 위치

"""
시험은 필기(30%, 이론) + 실기(70%, 코딩) 평가.
"""

if __name__ == "__main__":
    BbSort([66, 22, 33, 11, 55, 44])
    #MrgSort([2, 7, 36, 45, 15, 22, 25, 61])
    #QkSort([47, 84, 15, 23, 35, 92, 61, 17])
