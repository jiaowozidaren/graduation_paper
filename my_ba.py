import numpy as np
import BA_Ising as bi
import matplotlib.pyplot as plt
import math
import matplotlib as mpl
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import networkx as nx


data = []
fig, ax = plt.subplots()

T = 10


g = bi.Ising_BA_mat(500,5,T)
np.random.seed(0)
g.random_state()

print("begin")

color = []
mat = []

position = nx.spring_layout(g.mat)

for i in range(200):
    _ = g.cluster_flip()
    color.append(g.state.copy())
    mat.append(g.mat.copy())
    
for i in range(200):
    
    ax.cla()
    xx = nx.draw_networkx(mat[i],pos = position,node_color = color[i],with_labels = False,node_size = 50)
    plt.title("Step {}".format(i))
    plt.savefig('D:\\BA'+str(T)+'\\BA'+str(i)+'.png')
    #plt.show()
    
print("competed")


