import numpy as np

class Ising_mat(object):
    def __init__(self,h,w, T ,J = 1):
        self.h = h
        self.w = w
        self.N = h*w
        self.J = J
        self.T = T
        self.mat = np.ones([self.h, self.w], int)
        
    def random_state(self):
        self.mat = np.random.randint(0, 2, (self.h,self.w)) * 2 - 1

    def neighbor(self,x,y):
        return (((x+1)%self.h,y),(x,(y+1)%self.w),((x-1)%self.h,y),(x,(y-1)%self.w))

    def unit_E(self,x,y):
        sum_unit_E = 0
        for i in self.neighbor(x,y):
            sum_unit_E += self.mat[i]
        return -self.J * self.mat[x,y]*sum_unit_E
    
    def total_E(self):
        sum_total_E = 0
        for i in range(self.h):
            for j in range(self.w):
                sum_total_E += self.unit_E(i,j)
        return sum_total_E
                
    def total_M(self):
        return abs(np.sum(self.mat))

    def random_select(self):
        x = np.random.randint(self.h)
        y = np.random.randint(self.w)
        return (x,y)
    
    def single_flip(self):
        (x,y) = self.random_select()
        s = self.mat[x,y]
        is_flip = False
        
        c_acc = self.unit_E(x,y)*(s-(-s))
        
        p_acc = np.exp(c_acc)/self.T
        
        if c_acc > 0:
            s *= -1
            is_flip = True
        elif np.random.rand() < p_acc:
            s *= -1
            is_flip = True
        self.mat[x,y] = s
        
        return (x,y,is_flip)
        
    def cluster_flip(self):
        (x,y) = self.random_select()
        P_add = 1 - np.exp(-2 * self.J / self.T)
        stack = [(x,y)]
        s = self.mat[x,y]
        lable = np.ones([self.h, self.w])
        lable[x, y] = 0
        
        while len(stack)>0:
            #print(stack)
            (current_x, current_y) = stack.pop()
            self.mat[current_x,current_y] *= -1

            for i in self.neighbor(current_x,current_y):
                if self.mat[i] == s and lable[i] and np.random.rand() < P_add:
                    stack.append(i)
                    lable[i] = 0
