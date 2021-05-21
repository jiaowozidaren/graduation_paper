import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib as mpl
import Ising as Is

fig, ax = plt.subplots()
data = []

T = 3
g = Is.Ising_mat(20,20,T)
g.random_state()
print("begin")

for i in range(100):
    _ = g.cluster_flip()
    data.append(g.mat.copy())
    
for frame in range(0, len(data)):
    ax.cla()
    ax.imshow(data[frame], cmap=mpl.cm.winter)
    ax.set_title("Step {}".format(frame))
    ax.set_xticks([])
    ax.set_yticks([])
    plt.pause(0.01)

print("competed")
