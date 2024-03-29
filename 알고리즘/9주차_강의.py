# 2019. 04. 29. Mon.
# 내일(30일)은 벤처관 711호로 갈 것.
"""
<그래프 이론>
- 그래프: 점(또는 '정점'; Node)과 선(또는 '간선'; Edge)으로 이루어진 기하학적 형태.

1) 최소 신장 트리(Minimum Spanning Tree)
    > 연결성
    > 무방향성
    > 가중치
    "점들을 모두 잇는 데 필요한 선의 최소 길이"
    일반화: n개의 점에 대해 n-1개의 선이 필요하다.
    - 입력: 인접 행렬로 표현된 2차원 배열, 정점의 개수 --> 2차원 행렬로 표현한
"""
"""
v1 <6> v2
v1 <7> v3
v3 <4> v4
v4 <3> v5
v1 <9> v6
= 29가 답.
*: 트리가 신장되는 매 단계에서, 다음 노드를 '트리'(마지막으로 연결한 노드가 아님.)와 연결하는 데 필요한 가중치가 가장 작은 걸 택함.
"""
nodes = [[0, 6, 7, 99, 10, 9]]
class Prim:
    def __init__(self, Nodes):
        self.__ary = Nodes
        self.__from = 1
        # self.__dist =  트리에서 가장 가까운 노드 사이의 거리.
        pass