import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

##########选取的两条边要注意以下情况##############
##########1.避免重复选择一条边
##########2.避免选择的边中有重合的节点
data = np.loadtxt('average_path.txt', dtype=float)
data = data.T
plt.style.use('ggplot')

plt.plot(data[0], data[1], 'o-', label='$r_1$')
plt.xlabel('assortivity')
plt.ylabel('average path length')
plt.savefig('average_length_path.png', dpi=500, bbox_inches='tight')
plt.show()