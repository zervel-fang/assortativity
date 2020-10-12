import networkx as nx
import random
import numpy as np
############首先生成BA网络##########
G = nx.barabasi_albert_graph(200,2)
Iteration = 10000 ##迭代次数
i = 0
p = 1   ##重连概率
###########开始以概率p按算法要求重连#########
while i < Iteration:
    edge = list(G.edges())
    degree = nx.degree(G)
    index1 = random.randint(0,len(G.edges)-1) ##随机获取第一条边
    index2 = random.randint(0,len(G.edges)-1) ##随机获取第二条边
    edge1 = edge[index1]
    edge2 = edge[index2]
    k1 = degree[edge1[0]]
    k2 = degree[edge1[1]]
    k3 = degree[edge2[0]]
    k4 = degree[edge2[1]]

    order_arr = [[edge1[0], edge1[1], edge2[0], edge2[1]],[k1, k2, k3, k4]]
    order_arr = np.array(order_arr)
    order_arr = order_arr[:, order_arr[1].argsort()]
    i = i + 1
    p1 = random.random()
    ############在网络中移除原来的边并加上新的边##########
    if p1 < p and index1 != index2:
        G.remove_edge(edge1[0], edge1[1])
        G.remove_edge(edge2[0], edge2[1])
        G.add_edge(order_arr[0][0], order_arr[0][1])
        G.add_edge(order_arr[0][2], order_arr[0][3])
    print("同配系数为：",str(round(nx.degree_assortativity_coefficient(G),6)))