import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

##########选取的两条边要注意以下情况##############
##########1.避免重复选择一条边
##########2.避免选择的边中有重合的节点
data = np.loadtxt('clustering_ass.txt', dtype=float)
data = data.T
plt.style.use('ggplot')

plt.plot(data[0], data[1], 'o-', label='$r_1$')
plt.xlabel('$r_2$')
plt.ylabel('clustering coefficient')
plt.savefig('clustering_ass.png', dpi=500, bbox_inches='tight')
plt.show()