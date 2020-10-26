import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('results/ass.txt', dtype=float)
data = data.T

data1 = np.loadtxt('results/disass.txt', dtype=float)
data1 = data1.T

P1 = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]

plt.style.use('ggplot')
plt.figure(figsize=(12,12))
plt.subplot(121)
plt.plot(P1, data[0], 'v-', label='$r_1$')
plt.plot(P1, data[1], 'o-', label='$r_2$')
plt.xlabel('1-$p$')
plt.ylabel('assortivity')
plt.legend()

plt.subplot(122)
plt.plot(P1, data1[0], 'v-', label='$r_1$')
plt.plot(P1, data1[1], 'o-', label='$r_2$')
plt.xlabel('1-$p$')
plt.ylabel('assortivity')
plt.subplots_adjust(top=0.7, bottom=0.3)
plt.savefig('results/ass.png', dpi=500, bbox_inches='tight')
plt.show()