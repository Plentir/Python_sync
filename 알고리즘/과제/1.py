# 알고리즘

def Kruskal(array_weights, array_sections):
    tot_weights = []
    flag = 1

    while flag == 1:  # 모든 노드가 같은 섹션에 포함될 때까지 구문 반복.
        _from = _to = 0  # 초기화
        _min = 999

        for i in range(len(array_weights)):  # 가중치가 가장 작은 연결을 검색. i는 연결이 시작되는 노드의 번호(index).

            for j in range(len(array_weights[i])):  # j는 i와 연결될 노드의 번호(index).
                if array_weights[i][j] < _min and array_weights[i][j] != -1:
                    _min = array_weights[i][j]
                    _from, _to = i, j

        if array_sections[_from] != array_sections[_to]:  # 두 노드를 연결했을 때 loop가 발생하지 않으면 두 노드를 연결함.

            if array_sections.count(_to + 1) == 0:  # 섹션 통합
                for k in range(array_sections.count(_from + 1)):
                    array_sections[array_sections.index(_from + 1)] = array_sections[_to]

            else:
                for k in range(array_sections.count(_to + 1)):  # 섹션 통합
                    array_sections[array_sections.index(_to + 1)] = array_sections[_from]

            array_weights[_from][_to] = array_weights[_to][_from] = -1

            tot_weights.append((_from + 1, _to + 1, _min))  # 연결 순서 및 연결의 가중치를 단계별로 저장. >> 함수의 return값으로 사용.

            print("Connection established: Node %s <=> Node %s" %(_from + 1, _to + 1))

        else:  # 섹션 내에 loop가 발생할 경우.
            array_weights[_from][_to] = array_weights[_to][_from] = 999  # 고려하지 않을 경로.

        if len(set(array_sections)) == 1:  # 모든 노드가 하나의 섹션으로 통합되었는지 확인함.
            flag = 0

    print("Total weights:", sum(tot_weights[n][-1] for n in range(len(tot_weights))))

    return tot_weights


# 이하는 실행 코드
if __name__ == "__main__":
    
    # (6, 9)
    weights1 = [[-1, 6, 7, 999, 10, 9],  # Node 1
               [6, -1, 999, 999, 999, 999],  # Node 2
               [7, 8, -1, 4, 5, 999],  # Node 3
               [999, 999, 4, -1, 3, 999],  # Node 4
               [10, 999, 5, 3, -1, 11],  # Node 5
               [9, 999, 999, 999, 11]]  # Node 6

    sections1 = [1, 2, 3, 4, 5, 6]

    # (8, 12)
    weights2 = [[-1, 3, 6, 999, 999, 999, 999, 1], # Node 1
               [3, -1, 2, 999, 999, 999, 999, 2], # Node 2
               [6, 2, -1, 1, 999, 999, 999, 999], # Node 3
               [999, 999, 1, -1, 6, 3, 4, 999], # Node 4
               [999, 999, 999, 6, -1, 3, 999, 999], # Node 5
               [999, 999, 999, 3, 3, -1, 2, 999], # Node 6
               [999, 999, 999, 4, 999, 2, -1, 10], # Node 7
               [1, 2, 999, 999, 999, 999, 10, -1]] # Node 8

    sections2 = [1, 2, 3, 4, 5, 6, 7, 8]

    # (5, 8)
    weights3 = [[-1, 4, 4, 3, 6], # Node 1
                [4, -1, 3, 999, 7], # Node 2
                [4, 3, -1, 2, 999], # Node 3
                [3, 999, 2, -1, 5], # Node 4
                [6, 7, 999, 5, -1]] # Node 5

    sections3 = [1, 2, 3, 4, 5]

    # Kruskal(weights1, sections1)
    # print()
    Kruskal(weights2, sections2)
    # print()
    # Kruskal(weights3, sections3)
