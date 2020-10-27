import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('final_result.txt', dtype=float)
P = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 0.999, 0.9999]


plt.style.use('ggplot')
plt.plot(P, data[0], 'o-', label='P=0.2')
plt.plot(P, data[4], '^-', label='P=0.91')
plt.plot(P, data[8], 'v-', label='P=0.94')
plt.plot(P, data[10], 's-', label='P=0.96')
plt.plot(P, data[12], '*-', label='P=0.99')
plt.plot(P, data[13], 'd-', label='P= 1')
plt.xlabel('$q$')
plt.ylabel('$M$')
plt.legend()
plt.savefig('percolation.png', dpi=500, bbox_inches='tight')
plt.show()


