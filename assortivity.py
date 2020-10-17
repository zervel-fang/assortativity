import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

def calculate_ass(G, p , Iteration):
    #Iteration = 10000 ##迭代次数
    i = 0
    #p = 0.6   ##重连概率
    ###########开始以概率p按算法要求重连#########
    while i < Iteration:
        #print(i)
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
        if p1 > p and index1 != index2:
            #################随机重连####################
            rand_index = random.sample(range(0, 4), 4)
            G.remove_edge(edge1[0], edge1[1])
            G.remove_edge(edge2[0], edge2[1])
            G.add_edge(order_arr[0][rand_index[0]], order_arr[0][rand_index[1]])
            G.add_edge(order_arr[0][rand_index[2]], order_arr[0][rand_index[3]])
    #return round(nx.degree_assortativity_coefficient(G),6)
    M = nx.degree_mixing_matrix(G)
    M2 = M*M
    value = (M.trace() - M2.trace())/(1-M2.trace())
    return value

def calculate_disass(G, p , Iteration):
    #Iteration = 10000 ##迭代次数
    i = 0
    #p = 0.6   ##重连概率
    ###########开始以概率p按算法要求重连#########
    while i < Iteration:
        #print(i)
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
            G.add_edge(order_arr[0][0], order_arr[0][2])
            G.add_edge(order_arr[0][1], order_arr[0][3])
        if p1 > p and index1 != index2:
            #################随机重连####################
            rand_index = random.sample(range(0, 4), 4)
            G.remove_edge(edge1[0], edge1[1])
            G.remove_edge(edge2[0], edge2[1])
            G.add_edge(order_arr[0][rand_index[0]], order_arr[0][rand_index[1]])
            G.add_edge(order_arr[0][rand_index[2]], order_arr[0][rand_index[3]])
    M = nx.degree_mixing_matrix(G)
    M2 = M*M
    value = (M.trace() - M2.trace())/(1-M2.trace())
    return value

############首先生成BA网络##########

Iteration = 100000  ##迭代次数
P = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9, 1]
sum_v = 0
for i in range(2):
    print(i)
    G = nx.barabasi_albert_graph(2000, 2)
    v = calculate_ass(G, 1, Iteration)
    print(v)
    sum_v = sum_v + v


print(sum_v/2)
# assortivity = np.zeros((11,2))
# count = 0
# for i in P:
#     print(i)
#     for j in range(20):
#         value = calculate_ass(G, i, Iteration)
#         assortivity[count][0] = assortivity[count][0] + value
#         value1 = calculate_disass(G, i, Iteration)
#         assortivity[count][1] = assortivity[count][1] + value1
#     assortivity[count][0] = assortivity[count][0] / 20
#     assortivity[count][1] = assortivity[count][1] / 20
#     count = count + 1
#
#
# plt.subplot(121)
# assortivity = assortivity.T
# plt.plot(P,assortivity[0])
# plt.xlabel('p')
# plt.ylabel('assortivity')
# plt.subplot(122)
# plt.plot(P,assortivity[1])
# plt.xlabel('p')
# plt.ylabel('assortivity')
# fid = open('dataset.txt','w')
# for i in range(11):
#     fid.write(str(assortivity[0][i])+' '+str(assortivity[1][i])+'\n')
# plt.show()