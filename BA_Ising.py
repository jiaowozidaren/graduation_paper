import numpy as np
import math
import networkx as nx

class Ising_BA_mat(object):
    def __init__(self,n,m, T ,J = 1,seed = 0):
        self.n = n
        self.m = m
        self.J = J
        self.T = T
        self.mat = nx.barabasi_albert_graph(n, m,seed = seed)
        self.state = np.ones(n)
        
    def random_state(self):
        self.state = np.random.randint(0, 2 ,self.n) * 2 - 1

    def neighbor(self,x):
        return list(self.mat.neighbors(x))

    def unit_E(self,x):
        x_nei = self.neighbor(x)
        sum_unit_E = 0
        for i in x_nei:
            sum_unit_E += self.state[i]
        return -self.J * self.state[x] * sum_unit_E
    
    def total_E(self):
        sum_total_E = 0
        for i in range(self.n):
            sum_total_E += self.unit_E(i)
        return sum_total_E
                
    def total_M(self):
        return abs(np.sum(self.state))

    def random_select(self):
        x = np.random.randint(self.n)
        return x
    
        
    def cluster_flip(self):
        x = self.random_select()
        P_add = 1 - np.exp(-2 * self.J / self.T)
        stack = [x]
        s = self.state[x]
        lable = np.ones(self.n)
        lable[x] = 0
        
        while len(stack)>0:
            #print(stack)
            x_current = stack.pop()
            self.state[x_current] *= -1
            x_nei = self.neighbor(x_current)
            
            for i in x_nei:
                if self.state[i] == s and lable[i] and np.random.rand() < P_add:
                    stack.append(i)
                    lable[i] = 0
    def img(self):
        try:
            img = self.state.reshape(int(math.sqrt(self.n)),int(math.sqrt(self.n)))
            return img
        except IOError:
            print ("Error: 数据尺寸无法转化为正方形")
