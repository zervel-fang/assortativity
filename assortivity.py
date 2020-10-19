import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

def calculate_ass(G, p , Iteration):
    #Iteration = 10000 ##迭代次数
    i = 0
    #p = 0.6   ##重连概率
    ###########开始以概率p按算法要求重连#########
    degree_nn = []
    for node in G.nodes():
        sum1 = 0
        neighbors = nx.neighbors(G, node)
        for j in neighbors:
            sum1 = sum1 + G.degree(j)
        sum1 = sum1/ G.degree(j)
        degree_nn.append(sum1)
    ############计算r3############################
    degree = np.array(G.degree())
    degree = degree.T[1]
    degree = degree.T


    value2 = np.corrcoef(degree,degree_nn)[0][1]
    #print(value2)
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
        #print(p1)
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
    value1 = round(nx.degree_assortativity_coefficient(G),6)
    M = nx.degree_mixing_matrix(G)
    M2 = M*M
    value = (M.trace() - M2.trace())/(1-M2.trace())


    #############计算r3###########################

    return value1, value,value2

def calculate_disass(G, p , Iteration):
    #Iteration = 10000 ##迭代次数
    i = 0
    #p = 0.6   ##重连概率
    ###########开始以概率p按算法要求重连#########
    degree_nn = []
    for node in G.nodes():
        sum1 = 0
        neighbors = nx.neighbors(G, node)
        for j in neighbors:
            sum1 = sum1 + G.degree(j)
        sum1 = sum1/ G.degree(j)
        degree_nn.append(sum1)
    ############计算r3############################
    degree = np.array(G.degree())
    degree = degree.T[1]
    degree = degree.T
    value2 = np.corrcoef(degree,degree_nn)[0][1]
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
    value3 = round(nx.degree_assortativity_coefficient(G),6)
    M = nx.degree_mixing_matrix(G)
    M2 = M*M
    value = (M.trace() - M2.trace())/(1-M2.trace())


    #############计算r3###########################

    return value3, value,value2

############首先生成BA网络##########


Iteration = 5000  ##迭代次数
P = [0.999999,0.99999,0.9999,0.999,0.99,0.9,0.8,0.7,0.6,0.4,0]
P1 = [0.000001,0.00001,0.0001,0.001,0.01,0.1,0.2,0.3,0.4,0.6,1]
assortivity = np.zeros((11,3))
count = 0
for i in P:
    print(i)
    G = nx.barabasi_albert_graph(200, 2)
    for j in range(10):
        value1,value2,value3 = calculate_ass(G, i, Iteration)
        assortivity[count][0]= assortivity[count][0] + value1
        assortivity[count][1] = assortivity[count][1] + value2
        assortivity[count][2] = assortivity[count][2] + value3
    assortivity[count][0] = assortivity[count][0] / 10
    assortivity[count][1] = assortivity[count][1] / 10
    assortivity[count][2] = assortivity[count][2] / 10
    count = count + 1

assortivity1 = np.zeros((11,3))
count = 0
for i in P:
    print(i)
    G = nx.barabasi_albert_graph(200, 2)
    for j in range(10):
        value1,value2,value3 = calculate_disass(G, i, Iteration)
        assortivity1[count][0]= assortivity1[count][0] + value1
        assortivity1[count][1] = assortivity1[count][1] + value2
        assortivity1[count][2] = assortivity1[count][2] + value3
    assortivity1[count][0] = assortivity1[count][0] / 10
    assortivity1[count][1] = assortivity1[count][1] / 10
    assortivity1[count][2] = assortivity1[count][2] / 10
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