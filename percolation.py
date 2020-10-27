import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
##############渗流过程###############
def Judge_in_graph(G, node1, node2, node3, node4):
    ############该函数用来判断重连的边是否在原网络中########
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
        ####################选择的两条边的四个节点中不能有相同的节点##################
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
                #r1 = round(nx.degree_assortativity_coefficient(G), 6)
                #print(r1)
        if p1 >= p and tag == 1:
            #################随机重连####################
            rand_index = random.sample(range(0, 4), 4)
            judge_tag = Judge_in_graph(G, order_arr[0][rand_index[0]], order_arr[0][rand_index[1]], order_arr[0][rand_index[2]], order_arr[0][rand_index[3]])
            if judge_tag:
                G.remove_edge(edge1[0], edge1[1])
                G.remove_edge(edge2[0], edge2[1])
                G.add_edge(order_arr[0][rand_index[0]], order_arr[0][rand_index[1]])
                G.add_edge(order_arr[0][rand_index[2]], order_arr[0][rand_index[3]])
                i = i + 1
    ##############计算两种同配性系数###############
    #r1 = round(nx.degree_assortativity_coefficient(G),6)
    M = nx.degree_mixing_matrix(G)
    M2 = M*M
    r2 = (M.trace() - np.sum(M2)) / (1 - np.sum(M2))
    return G, r2


G = nx.read_edgelist('datasets/network.txt', nodetype=int)
nodes_num = len(list(G.nodes()))
q = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 0.999, 0.9999]
p = [0.2, 0.8, 0.85, 0.9, 0.91,0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1]
fout = open('results/final_result.txt', 'a+')
for p_v in p:
    G = nx.read_edgelist('datasets/network.txt', nodetype=int)
    G1 , r2 = calculate_ass(G, p_v, 1500)
    fid = open('datasets/network_ass.txt', 'w')
    edges = list(G1.edges())
    for edge in edges:
        fid.write(str(edge[0])+' '+str(edge[1])+'\n')
    fid.close()
    M = []
    for proba in q:
        #########模拟多次###########
        print(proba)
        sum_value = 0
        for index in range(1000):
            #print(index)
            G = nx.read_edgelist('datasets/network_ass.txt', nodetype=int)
            for i in range(len(list(G.nodes()))):
                #print(i)
                rand_node = random.sample(list(G.nodes()), 1)
                q1 = random.random()
                if q1 < proba:
                    ##则移除节点和边
                    nei = list(G.neighbors(rand_node[0]))
                    ####先移除边
                    #print(nei)
                    for node in nei:
                        #print(node)
                        G.remove_edge(rand_node[0], node)
                compoent = list(nx.connected_components(G))
                Giant_component = compoent[0]
            frac = len(Giant_component) / nodes_num
            sum_value = sum_value + frac
        sum_value = sum_value /1000
        M.append(sum_value)
    for val in M:
        fout.write(str(val)+' ')
    fout.write('\n')
print(M)
fout.close()