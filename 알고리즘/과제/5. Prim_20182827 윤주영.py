# nodes = [[0, 6, 7, 99, 10, 9]]
# class Prim:
#     def __init__(self, Nodes):
#         self.__ary = Nodes
#         self.__from = 1
#         self.__to = 1
#         self.__dist = __ary[0][0]  # 트리에서 가장 가까운 노드 사이의 거리.
        
#     def prim(self, ary):
#         while ary[-1].count(0) == len(ary[-1]):

# C=[[0,6,7,99,10,9],[6,0,8,99,99,99],[7,8,0,4,5,99],[99,99,4,0,3,99],[10,99,5,3,0,11],[9,99,99,99,11,0]]
def Prim(C):
    frm=[]
    dist=[]
    T=[]
    n=len(C[0])

    for i in range(0,n):  # 첫 번째 노드(frm = 0)에서부터 트리를 그린다고 할 때, 그 노드로부터 다른 노드들까지의 거리를 담고 있는 C[0]의 원소들을 dist에 차례대로 추가한다.
        frm.append(0)
        dist.append(C[0][i])
    
    for k in range(0,len(C) - 1):
        value=99
        best=0
        for j in range(k,len(C[k])):
            if C[k][j] < value and C[k][j] > 0: ## 추가 : dist[i]중 가장 작은 값을 찾아 그 값을 value, index를 best에 넣은다.
                value=C[k][j]
                best=j
        T.append([frm[best] + 1,best + 1])
        print(best,frm[best-1])
        print(k,T)
        dist[best]=0

        for i in range(1,n):
            if(C[best][i]<dist[i]):
                frm[i]=best
                dist[i]=C[best][i]

    return T

if __name__ == "__main__":
    C=[[0,6,7,99,10,9],[6,0,8,99,99,99],[7,8,0,4,5,99],[99,99,4,0,3,99],[10,99,5,3,0,11],[9,99,99,99,11,0]]

    T=Prim(C)
    print(T)
    total=0
    for i in range(len(C) - 1):
        total+=C[T[i][0] - 1][T[i][1] - 1]

    print(total)