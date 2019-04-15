#피보나치 수열 - 재귀호출 이용
"""
def fbnc(n):
    res = 0
    if n <= 2:
        return res 
    else:
        return fbnc(n-1) + fbnc(n-2)
"""
#피보나치 수열 - 동적 프로그래밍 방식 이용
"""
def fibo(n):
    if n == 0 || n == 1:
        
    t = time.process_time_ns
    ary = [0, 1] # ary = [a1, a2, ..., an]
    for k in range(1, n):
        ary.append(ary[k] + ary[k - 1])
        print("f%s = %s" %(k, ary[-1]))
    return ary[-1]

fibo(10)


import time
t = time.process_time_ns
print(t)
"""
#-----------------------------------------------------------------------------------------------------------------------
#화요일 수업.
"""
키(key) = 정렬 기준이 될 값
이진 탐색: 검색 범위를 두 부분으로 나누는 과정을 반복하며 값이 있는지 탐색함.
"""
"""
def BiSrch(ary_input, value):
    low = 0
    high = len(ary_input)

    while (low < high):
        mid = int((low + high)/2)
        if value == (ary_input[mid]):
            return mid
        elif value < (ary_input[mid]):
            high = mid - 1
        else: #value > ary[mid]:
            low = mid + 1
    return -1
print(BiSrch([1, 2, 3, 4, 5, 6, 7, 8], 8))
"""
#버블 정렬
def BubleSrch(ary):
    temp = ary[0]
    for i in range(0, len(ary) - 2):
        for j in range(0, len(ary) - 1):
            if ary[j] > ary[j+1]:
                temp = ary[j+1]
                ary[j+1] = ary[j]
                ary[j] = temp
                print(ary, "안")
        print(ary, "바깥")
    return ary

print(BubleSrch([17, 37, 7, 47, 27, 67]))