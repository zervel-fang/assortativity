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
                #(i)
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
    r1 = (M.trace() - np.sum(M2)) / (1 - np.sum(M2))
    conncected = nx.is_connected(G)
    if conncected:
        r2 = round(nx.average_shortest_path_length(G), 6)
    else:
        sv = 0
        coun = 0
        for C in (G.subgraph(c).copy() for c in nx.connected_components(G)):
            v = nx.average_shortest_path_length(C)
            sv = sv + v
            coun = coun + 1
        r2 = sv / coun
    return r1, r2

def calculate_disass(G, p , Iteration):
    i = 0
    while i < Iteration:
        print(i)
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
    r1 = (M.trace() - np.sum(M2)) / (1 - np.sum(M2))
    conncected = nx.is_connected(G)
    if conncected:
        r2 = round(nx.average_shortest_path_length(G), 6)
    else:
        sv = 0
        coun = 0
        for C in (G.subgraph(c).copy() for c in nx.connected_components(G)):
            v = nx.average_shortest_path_length(C)
            sv = sv + v
            coun = coun + 1
        r2 = sv / coun
    return r1, r2

Iteration = 10000 ##迭代次数
P = [1, 0.95,  0.9, 0.85,  0.8, 0.75,  0.7, 0.65,  0.6, 0.55,  0.5, 0.45,  0.4, 0.35,  0.3, 0.25,  0.2, 0.15,  0.1, 0.05, 0]
assortivity = np.zeros((21,1))
average_path = np.zeros((21,1))
count = 0

for i in P:
    print(i)
    for j in range(10):
        G = nx.read_edgelist('datasets/network_average_path.txt', nodetype=int)
        r1, r2 = calculate_ass(G, i, Iteration)
        print(r1, r2)
        assortivity[count] = assortivity[count] + r1
        average_path[count] = average_path[count] + r2
    assortivity[count] = assortivity[count] / 10
    average_path[count] = average_path[count] / 10
    count = count + 1
fid = open('results/average_path_ass.txt', 'w')
for i in range(len(P)):
    fid.write(str(assortivity[i])+' '+str(average_path[i])+'\n')
fid.close()

plt.figure(figsize=(16,16))
plt.style.use('ggplot')
plt.semilogx(assortivity,average_path,'o-', label='$r_1$')
plt.xlabel('assortivity')
plt.ylabel('average path length')
plt.savefig('results/average_length_path.png', dpi=500, bbox_inches='tight')
plt.show()