"""
필기 : Traveling Salesman Problem 이란 무엇인가? Greedy 알고리즘을 적용한 해결 방법을 제안하라 “학번.txt”로 저장 후 제출

Traveling Salesman Problem은 비행기를 타고 전세계의 여러 도시에 출장을 간다는 예시로 설명할 수 있다.
비행기를 타고 전세계에 흩어진 n개의 나라에 출장을 가야 하는 상황이 발생했다고 가정하자.
이때, 비행기로 가장 짧은 거리를 이동하면서 n개의 나라를 모두 방문하기 위한 방문 순서를 알고 싶다고 하는 것이 바로 Traveling Salesman Problem이다.
이 문제를 해결하기 위해 욕심쟁이 기법을 이용한 알고리즘을 사용할 수 있다.
욕심쟁이 기법을 이용한 알고리즘을 작성하기 위해서는 다음의 요건을 만족해야 한다.

첫째, 가장 큰 문제를 바로 해결하는 대신, 전체 문제를 부분 문제로 분할한다.
둘째, 부분 문제의 해답 중에서 가장 최적화된 답을 선택한다.
셋째, 앞의 두 요건을 차례대로 반복하며 부분 문제의 최적화된 답을 모두 합치면 전체 문제의 가장 최적화된 답을 얻을 수 있다.
넷째, 세 번째 요건은 부분 문제의 최적화된 답을 합하면 전체적인 관점에서도 가장 최적의 답이 된다는 전제 하에 이뤄진다.

따라서 위의 조건을 만족하도록 아래와 같이 해결 방법을 설계할 수 있다.

첫째, 출장을 가야 하는 n개의 나라를 대륙별로 분류하고, 각 대륙 내에서 먼저 이동한 뒤 다른 대륙의 국가로 이동한다.
둘째, 이동할 때는 최대한 같은 방향으로만 이동하도록 한다. 예를 들어, 서울에서 일본으로 이동한 뒤에는 미국으로 이동할 수 있지만 인도 쪽으로 이동할 수는 없다.(미국은 서울에서 일본으로 이동하는 방향과 같은 방향이고, 인도는 그와 반대이다.) 또다른 예로는 시계 방향이나 반시계 방향으로 이동하는 것도 있다.
셋째, 각 대륙에서 얻은 최단 경로를 모두 합하면 전체 문제의 해답이 된다.
"""
"""
실기
–오름차순으로 정렬하되 최악, 최선의 경우 가장 효율이 좋은 알고리즘을 사용해 아래 조건에 맞게 정렬하라
–랜덤넘버발생기로 10개의 (0~99)사이의 숫자를 만들고
–그 중간과정과 결과를 화면과 출력하고
–최종 결과를 result.dat 화일에 출력
–제출: code 는 실행 file로 변환 2018XXXX.py, 결과 file (result.dat), code screen capture , 중간과정 screen capture – 총 4개 file

*가능한 부분 만이라도 코드완성해서 제출하라
"""
def MakeRandInt(a, b, ln):
    from random import randint
    ary = []
    while len(ary) < ln:
        ary.append(randint(a, b))
    return ary


def MrgSort(ary):
    if len(ary) <= 1:
        return ary
    mid = len(ary)//2
    ary_l = MrgSort(ary[:mid])
    ary_r = MrgSort(ary[mid:])
    return Mrg(ary_l, ary_r)


def Mrg(ary1, ary2):
    i = j = 0
    res = []
    while i < len(ary1) and j < len(ary2):
        if ary1[i] > ary2[j]:
            res.append(ary2[j])
            j += 1
        else:
            res.append(ary1[i])
            i += 1
        print(res, "중간결과")
    res += ary1[i:]
    res += ary2[j:]
    return res


if __name__ == "__main__":
    test = MakeRandInt(0, 99, 10)

    f = open("result.dat", "w")
    result = MrgSort(test)
    print(result, "최종결과")
    for i in range(len(result)):
        if i != (len(result) - 1):
            f.write("%s, " %result[i])
        else:
            f.write("%s" %result[i])
    f.close()
