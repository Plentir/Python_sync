def Quicksort(A):
    p = A[0]
    pi = 1
    for i in range(2,len(A)):
        if A[pi]>p and A[i]<p :
            A[pi],A[i]=A[i],A[pi]
            pi = pi+1
    A[pi-1],A[0]=A[0],A[pi-1]
    return pi-1

def QS(A):
    low = 0
    high = len(A)-1
    if high>low :
        global pivot
        pivot = Quicksort(A)
        QS(A[:pivot])
        QS(A[pivot+1:])
        return QS(A[:pivot])
    else :
        return A

if __name__ == "__main__":
    #print(QS([1, 2, 1, -1, 0, 10, 123, -11, -12, 1, 0]))
    print(QS([47, 84, 15, 23, 35, 92, 61, 17]))