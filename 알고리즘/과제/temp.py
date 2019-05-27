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
                    P[i][j] = k + 1
        
        
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


    weights = [[0, 6, 4, 100, 100], 
           [100, 0, 100, 7, 5], 
           [3, 100, 0, 2, 100], 
           [100, 4, 100, 0, 6], 
           [2, 100, 7, 100, 0]]

    Floyd(weights)


def path_finder(i, j, P):

    if P[i][j] != 0:
        a = path_finder(i, P[i][j] - 1, P)
        
        print(a)
        print("%s => %s :" %(i + 1, j + 1), end = "")
        
        for t in a:
            if t != 0:
                print(" %s ," %t, end = "")
            
        print(" %s" %(j + 1))
        
        path_finder(P[i][j] - 1, j, P)
        
        print("\n")
        
        return (i + 1, P[i][j], j + 1)
    
    
    elif i != j:
        print("%s => %s :" %(i + 1, j + 1), i + 1, ",", j + 1)
    
        return (i + 1, 0, j + 1)
    
    return


for i in range(len(P)):
    for j in range(len(P)):
        path_finder(i, j, P)
