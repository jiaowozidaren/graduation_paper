import numpy as np
import Ising as Is
import matplotlib.pyplot as plt
import math
import matplotlib as mpl
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

fig, ax = plt.subplots()
data = []

T = 4
g = Is.Ising_mat(100,100,T)
g.random_state()

print("begin")

for i in range(150):
    _ = g.cluster_flip()
    #_ = g.single_flip()
    data.append(g.mat.copy())
    
for frame in range(0, len(data)):
    ax.cla()
    
    ax.set_title("Step {}".format(frame))
    plt.imshow(data[frame], cmap=mpl.cm.winter)
    plt.savefig('D:\\R\\ising_grid'+str(frame)+'.png')

print("competed")

