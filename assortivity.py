import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

##########选取的两条边要注意以下情况##############
##########1.避免重复选择一条边
##########2.避免选择的边中有重合的节点
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
    r1 = round(nx.degree_assortativity_coefficient(G),6)
    M = nx.degree_mixing_matrix(G)
    M2 = M*M
    r2 = (M.trace() - M2.trace())/(1-M2.trace())
    return r1, r2

Iteration = 1500  ##迭代次数
#P = [0.999999,0.99999,0.9999,0.999,0.99,0.9,0.8,0.7,0.6,0.4,0]
P = [1, 0.95,  0.9, 0.85,  0.8, 0.75,  0.7, 0.65,  0.6, 0.55,  0.5, 0.45,  0.4, 0.35,  0.3, 0.25,  0.2, 0.15,  0.1, 0.05, 0]
P1 = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]
assortivity = np.zeros((21,2))

count = 0
for i in P:
    print(i)
    for j in range(10):
        G = nx.barabasi_albert_graph(200, 2)
        value1,value2 = calculate_ass(G, i, Iteration)
        print(value1,value2)
        assortivity[count][0]= assortivity[count][0] + value1
        assortivity[count][1] = assortivity[count][1] + value2
    assortivity[count][0] = assortivity[count][0] / 10
    assortivity[count][1] = assortivity[count][1] / 10
    count = count + 1
assortivity1 = np.zeros((21,2))
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

fid = open('ass.txt','w')

for i in assortivity:
    fid.write(str(i[0])+' '+str(i[1])+'\n')
fid.close()

fid1 = open('disass.txt','w')

for i in assortivity1:
    fid1.write(str(i[0])+' '+str(i[1])+'\n')
fid1.close()

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