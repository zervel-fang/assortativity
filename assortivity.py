import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

def calculate_ass(G, p , Iteration):
    i = 0
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
        p1 = random.random()
        #print(p1)
        ############在网络中移除原来的边并加上新的边##########
        if p1 < p and index1 != index2:
            if (order_arr[0][0], order_arr[0][1]) not in G.edges() and (order_arr[0][0], order_arr[0][1]) not in G.edges():
                G.remove_edge(edge1[0], edge1[1])
                G.remove_edge(edge2[0], edge2[1])
                G.add_edge(order_arr[0][0], order_arr[0][1])
                G.add_edge(order_arr[0][2], order_arr[0][3])
                i = i + 1
        if p1 >= p and index1 != index2:
            #################随机重连####################
            rand_index = random.sample(range(0, 4), 4)
            if (order_arr[0][rand_index[0]], order_arr[0][rand_index[1]]) not in G.edges() and (order_arr[0][rand_index[2]], order_arr[0][rand_index[3]]) not in G.edges():
                G.remove_edge(edge1[0], edge1[1])
                G.remove_edge(edge2[0], edge2[1])
                G.add_edge(order_arr[0][rand_index[0]], order_arr[0][rand_index[1]])
                G.add_edge(order_arr[0][rand_index[2]], order_arr[0][rand_index[3]])
                i = i + 1
    r1 = round(nx.degree_assortativity_coefficient(G),6)
    M = nx.degree_mixing_matrix(G)
    M2 = M*M
    r2 = (M.trace() - M2.trace())/(1-M2.trace())
    return r1, r2

def calculate_disass(G, p , Iteration):
    i = 0
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

        p1 = random.random()
        ############在网络中移除原来的边并加上新的边##########
        if p1 < p and index1 != index2:
            if (order_arr[0][0], order_arr[0][2]) not in G.edges() and (order_arr[0][1], order_arr[0][3]) not in G.edges():
                G.remove_edge(edge1[0], edge1[1])
                G.remove_edge(edge2[0], edge2[1])
                G.add_edge(order_arr[0][0], order_arr[0][3])
                G.add_edge(order_arr[0][1], order_arr[0][2])
                i = i + 1
                #print(i)
        if p1 > p and index1 != index2:
            #################随机重连####################
            rand_index = random.sample(range(0, 4), 4)
            if (order_arr[0][rand_index[0]], order_arr[0][rand_index[1]]) not in G.edges() and (order_arr[0][rand_index[2]], order_arr[0][rand_index[3]]) not in G.edges():
                G.remove_edge(edge1[0], edge1[1])
                G.remove_edge(edge2[0], edge2[1])
                G.add_edge(order_arr[0][rand_index[0]], order_arr[0][rand_index[1]])
                G.add_edge(order_arr[0][rand_index[2]], order_arr[0][rand_index[3]])
                i = i + 1
    r1 = round(nx.degree_assortativity_coefficient(G),6)
    M = nx.degree_mixing_matrix(G)
    M2 = M*M
    r2 = (M.trace() - M2.trace())/(1-M2.trace())
    return r1, r2


Iteration = 1000  ##迭代次数
P = [0.999999,0.99999,0.9999,0.999,0.99,0.9,0.8,0.7,0.6,0.4,0]
P1 = [0.000001,0.00001,0.0001,0.001,0.01,0.1,0.2,0.3,0.4,0.6,1]
assortivity = np.zeros((11,2))
count = 0
for i in P:
    print(i)
    G = nx.barabasi_albert_graph(200, 2)
    for j in range(10):
        value1,value2 = calculate_ass(G, i, Iteration)
        assortivity[count][0]= assortivity[count][0] + value1
        assortivity[count][1] = assortivity[count][1] + value2
    assortivity[count][0] = assortivity[count][0] / 10
    assortivity[count][1] = assortivity[count][1] / 10
    count = count + 1

assortivity1 = np.zeros((11,2))
count = 0
for i in P:
    print(i)
    G = nx.barabasi_albert_graph(200, 2)
    for j in range(10):
        value1,value2 = calculate_disass(G, i, Iteration)
        assortivity1[count][0]= assortivity1[count][0] + value1
        assortivity1[count][1] = assortivity1[count][1] + value2
    assortivity1[count][0] = assortivity1[count][0] / 10
    assortivity1[count][1] = assortivity1[count][1] / 10
    count = count + 1
plt.figure(figsize=(16,16))
plt.style.use('ggplot')
plt.subplot(121)
assortivity = assortivity.T
plt.semilogx(P1,assortivity[0],'o-',label='$r_1$')
plt.semilogx(P1,assortivity[1],'^-',label='$r_2$')
plt.xlabel('1-$p$')
plt.ylabel('assortivity')

plt.subplot(122)
assortivity1 = assortivity1.T
plt.semilogx(P1,assortivity1[0],'o-',label='$r_1$')
plt.semilogx(P1,assortivity1[1],'^-',label='$r_2$')
plt.xlabel('1-$p$')
plt.ylabel('assortivity')
plt.legend()
plt.subplots_adjust(top=0.7,bottom=0.3)
plt.savefig('ass_disass.png',dpi=500,bbox_inches='tight')
plt.show()