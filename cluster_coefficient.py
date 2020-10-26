import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

def Judge_in_graph(G, node1, node2, node3, node4):
    edges = list(G.edges())
    tag = False
    if (node1, node2) not in edges and (node3, node4) not in edges:
        if (node2, node1) not in edges and (node4, node3) not in edges:
            tag = True
    return tag
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
        tag = 0
        if edge1[0] != edge2[0] and edge1[0] != edge2[1] and edge1[1] != edge2[0] and edge1[1] != edge2[1]:
            tag = 1
        order_arr = [[edge1[0], edge1[1], edge2[0], edge2[1]],[k1, k2, k3, k4]]
        order_arr = np.array(order_arr)
        order_arr = order_arr[:, order_arr[1].argsort()]
        p1 = random.random()
        ############在网络中移除原来的边并加上新的边##########
        if p1 < p and tag == 1:
            judge_tag = Judge_in_graph(G,order_arr[0][0], order_arr[0][1],order_arr[0][2], order_arr[0][3])
            if judge_tag:
                G.add_edge(order_arr[0][0], order_arr[0][1])
                G.add_edge(order_arr[0][2], order_arr[0][3])
                G.remove_edge(edge1[0], edge1[1])
                G.remove_edge(edge2[0], edge2[1])
                i = i + 1
                #print(i)
        if p1 >= p and index1 != index2 and tag == 1:
            #################随机重连####################
            rand_index = random.sample(range(0, 4), 4)
            judge_tag = Judge_in_graph(G, order_arr[0][rand_index[0]], order_arr[0][rand_index[1]], order_arr[0][rand_index[2]], order_arr[0][rand_index[3]])
            if judge_tag:
                G.remove_edge(edge1[0], edge1[1])
                G.remove_edge(edge2[0], edge2[1])
                G.add_edge(order_arr[0][rand_index[0]], order_arr[0][rand_index[1]])
                G.add_edge(order_arr[0][rand_index[2]], order_arr[0][rand_index[3]])
                i = i + 1
    #r1 = round(nx.degree_assortativity_coefficient(G),6)
    M = nx.degree_mixing_matrix(G)
    M2 = M*M
    r1 = (M.trace() - M2.trace())/(1-M2.trace())
    r2 = round(nx.average_clustering(G), 6)
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
        tag = 0
        if edge1[0] != edge2[0] and edge1[0] != edge2[1] and edge1[1] != edge2[0] and edge1[1] != edge2[1]:
            tag = 1
        order_arr = [[edge1[0], edge1[1], edge2[0], edge2[1]],[k1, k2, k3, k4]]
        order_arr = np.array(order_arr)
        order_arr = order_arr[:, order_arr[1].argsort()]
        p1 = random.random()
        ############在网络中移除原来的边并加上新的边##########
        if p1 < p and tag == 1:
            judge_tag = Judge_in_graph(G,order_arr[0][0], order_arr[0][3],order_arr[0][1], order_arr[0][2])
            if judge_tag:
                G.add_edge(order_arr[0][0], order_arr[0][3])
                G.add_edge(order_arr[0][1], order_arr[0][2])
                G.remove_edge(edge1[0], edge1[1])
                G.remove_edge(edge2[0], edge2[1])
                i = i + 1
        if p1 >= p and index1 != index2 and tag == 1:
            #################随机重连####################
            rand_index = random.sample(range(0, 4), 4)
            judge_tag = Judge_in_graph(G, order_arr[0][rand_index[0]], order_arr[0][rand_index[1]], order_arr[0][rand_index[2]], order_arr[0][rand_index[3]])
            if judge_tag:
                G.remove_edge(edge1[0], edge1[1])
                G.remove_edge(edge2[0], edge2[1])
                G.add_edge(order_arr[0][rand_index[0]], order_arr[0][rand_index[1]])
                G.add_edge(order_arr[0][rand_index[2]], order_arr[0][rand_index[3]])
                i = i + 1
    #r1 = round(nx.degree_assortativity_coefficient(G),6)
    M = nx.degree_mixing_matrix(G)
    M2 = M*M
    r1 = (M.trace() - M2.trace())/(1-M2.trace())
    r2 = round(nx.average_clustering(G),6)
    return r1, r2

Iteration = 1200  ##迭代次数
P = [1, 0.9999,  0.999, 0.99,  0.98, 0.97,  0.96, 0.95, 0.94,  0.93,  0.92, 0.75,  0.7, 0.65,  0.6, 0.5,  0.4, 0.3,  0.2, 0.1, 0]
assortivity = np.zeros((21,1))
clustering = np.zeros((21,1))

count = 0
#G = nx.barabasi_albert_graph(200, 2)
for i in P:
    print(i)
    for j in range(40):
        print(j)
        G = nx.read_edgelist('datasets/network.txt', nodetype=int)
        r1, r2 = calculate_disass(G, i, Iteration)
        print(r1, r2)
        assortivity[count] = assortivity[count] + r1
        clustering[count] = clustering[count] + r2
    assortivity[count] = assortivity[count] / 40
    clustering[count] = clustering[count] / 40
    count = count + 1

fid = open('results/clustering_ass.txt','w')
for i in range(len(P)):
    fid.write(str(assortivity[i][0]) + ' ' + str(clustering[i][0]) + '\n')
fid.close()


#plt.figure(figsize=(16, 16))
plt.style.use('ggplot')
plt.plot(assortivity, clustering, 'o-', label='$r_1$')
plt.xlabel('assortivity')
plt.ylabel('clustering coefficient')
plt.savefig('results/clustering_ass.png', dpi=500, bbox_inches='tight')
plt.show()