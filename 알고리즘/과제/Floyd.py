def floyd(array_weights):
    _len = len(array_weights)
  
    P = [[0 for n in range(_len)] for p in range(_len)]
    D = [[array_weights[p][n] for n in range(_len)] for p in range(_len)]


    print("<Input>")
    for n in range(_len):  # 양식에 맞게 출력.

            for p in range(_len):
                if p == _len - 1:
                    print("%2s\n" %D[n][p], end = "")

                else:
                    print("%2s  " %D[n][p], end = "")
    print("################## Start! ##################", end = "")


    for k in range(_len):

        for i in range(_len):
            
            for j in range(_len):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k
        
        
        print("\nk =", k + 1)
        for n in range(_len):  # 매 루프마다 결과 출력

            for p in range(_len):
                if p == _len - 1:
                    print("%2s\n" %D[n][p], end = "")

                else:
                    print("%2s  " %D[n][p], end = "")

    
    print("################### End! ###################\n<Final>")
    for n in range(_len):  # 매 루프마다 결과 출력

        for p in range(_len):
            if p == _len - 1:
                print("%2s\n" %D[n][p], end = "")

            else:
                print("%2s  " %D[n][p], end = "")

    return P


def print_path(i, j, P):

    if P[i][j] != 0:
        print_path(i, P[i][j], P)
        print(P[i][j])
        print_path(P[i][j], j, P)

    return 0


if __name__ == "__main__":
    P = floyd(
        [
            [0, 6, 4, 99, 99],
            [99, 0, 99, 7, 5],
            [3, 99, 0, 2, 99],
            [99, 4, 99, 0, 6],
            [2, 99, 7, 99, 0]
        ]
    )

    print("\n<P>")
    for i in range(len(P)):
        print(P[i])

    print_path(3, 2, P)