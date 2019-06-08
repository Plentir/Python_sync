def floyd(array_weights):
    _len = len(array_weights)

    P = [[0 for n in range(_len)] for p in range(_len)] 
    D = [[array_weights[p][n] for n in range(_len)] for p in range(_len)]
    # 이상은 함수 내부 변수 초기화 코드

    print("<Input>")
    for n in range(_len):  # 양식에 맞게 input 출력.

        for p in range(_len):

            if p == _len - 1:
                print("%2s\n" %D[n][p], end = "")

            else:
                print("%2s  " %D[n][p], end = "")

    print("\n################## Start! ##################")

    for k in range(_len):  # 플로이드 알고리즘으로 최단경로 탐색

        for i in range(_len):            

            for j in range(_len):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k + 1

        print("\n<k = ", k + 1, ">", sep = "")

        for n in range(_len):  # 매 루프(k = 0, 1, ..., n)마다 D를 표 형태로 출력

            for p in range(_len):
                if p == _len - 1:
                    print("%2s\n" %D[n][p], end = "")

                else:
                    print("%2s  " %D[n][p], end = "")

    print("\n################### End! ###################\n\n<Final>")

    for n in range(_len):  # 루프 완료 후, D의 최종 상태를 출력

        for p in range(_len):
            if p == _len - 1:
                print("%2s\n" %D[n][p], end = "")

            else:
                print("%2s  " %D[n][p], end = "")

    print("\n<P>")  # P를 표 형태로 출력

    for i in range(len(P)):

        for j in range(len(P)):
            if j != len(P) - 1:
                print("%2s  " %P[i][j], end = "")

            else:
                print("%2s" %P[i][j])

    return P


def path_finder(_from, _to, inter):  # 경유지 탐색 및 출력 함수
    via = inter[_from][_to]

    if via != 0:
        path_finder(_from, via - 1, inter)
        print(via, ", ", end = "")
        path_finder(via - 1, _to, inter)


if __name__ == "__main__":  # 최단경로 탐색 및 출력까지 모두 포함.  
    P = floyd(
        [
            [0, 6, 4, 99, 99],
            [99, 0, 99, 7, 5],
            [3, 99, 0, 2, 99],
            [99, 4, 99, 0, 6],
            [2, 99, 7, 99, 0]
        ]
    )  # 경로 탐색 알고리즘 호출

    print("")

    for i in range(len(P)):  # P 사용하여 경로 출력

        for j in range(len(P)):
            if i == j:
                pass

            elif P[i][j] != 0:
                print("%s => %s : %s , " %(i + 1, j + 1, i + 1), end = "")
                path_finder(i, j, P)
                print(j + 1, "")

            elif P[i][j] == 0:
                print("%s => %s : %s , %s" %(i + 1, j + 1, i + 1, j + 1))
