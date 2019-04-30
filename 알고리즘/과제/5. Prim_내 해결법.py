"""
1) 가중치가 가장 작은 노드 사이를 잇기.
    --> 현재 트리에 포함된 노드 중 하나를 기점으로 트리 밖의 다른 노드를 이을 때, 가중치가 가장 작은 걸 택함.
    --> 트리는 1번 노드에서부터 시작함.
    --> 첫 번째 확장 시에는 1번 노드를 기준으로 가중치가 낮은 노드를 탐색.
2) 노드를 이으면, a번 노드와 b번 노드를 잇는 선의 고유값(=3차원 좌표)을 저장.
    --> (a에서, b로, 가중치 k)
3) 2에서 만든 리스트를 이용해 트리 확장 단계를 출력하기
"""
class Prim:
    def __init__(self, array, start = 1, dst = 1):
        self.__ary = array
        self.__from = start  # 트리를 만들기 위해 이동할 때의 출발지 노드.
        self.__to = dst  # 트리를 만들기 위해 이동할 때의 목적지 노드.
        self.__dist = 999  # 트리에서 가장 가까운 노드 사이의 거리. 초기값은 가장 큰 걸로.
        

    def prim(self):
        tree = []
        tot_dist = 0

        for n in range(len(self.__ary)):
            temp_nextnode = n
            self.__dist = 999

            for i in range(len(self.__ary[n])):  # 1번 노드에서부터 트리 확장 -> 가중치가 가장 작은 노드 찾기.
                if (self.__ary[n][i] < self.__dist) and (self.__ary[n][i] != 0):
                    self.__dist = self.__ary[n][i]
                    temp_nextnode = i

            tree.append((n, temp_nextnode))
            tot_dist += self.__ary[n][i]
            
        print(tree)

        return (tree, tot_dist)




if __name__ == "__main__":
    nodes = ((0, 6, 7, 999, 10, 9), (6, 0, 8, 999, 999, 999), (7, 8, 0, 4, 5, 999), (999, 999, 4, 0, 3, 999), (10, 999, 5, 3, 0, 11), (9, 999, 999, 999, 11, 0))
    test = Prim(nodes)
    test.prim()

