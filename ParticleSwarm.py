import numpy as np 
import pandas as pd

def get_row (y, x):
    data = [y]+ [x[j] for j in range(0, len(x))]
    data = ["%12.6E" % x for x in data]
    return data  
 
class Swarm:
    def __init__(self, cfg):

       self.cfg = cfg
       self.pos = np.zeros([cfg.num_part(), cfg.num_dim()])
       self.vel = np.zeros([cfg.num_part(), cfg.num_dim()])

       self.p_best =  np.zeros([cfg.num_part(), cfg.num_dim()])
       self.yp_best = 1.0E18 * np.ones([cfg.num_part()])
 
       self.g_best = np.zeros([cfg.num_dim()])
       self.best = 1.0E18

       self.x_min = np.array([self.cfg.x_min()] * self.cfg.num_dim())
       self.x_max = np.array([self.cfg.x_max()] * self.cfg.num_dim())

       self.v_max =  self.cfg.vel_max() * (self.x_max-self.x_min)

    def initilize(self):

       np.random.seed(self.cfg.random_seed())

       rx  = np.random.rand(self.cfg.num_part(), self.cfg.num_dim())
       rv  = np.random.rand(self.cfg.num_part(), self.cfg.num_dim())

       for i in range(0, self.cfg.num_part()):
           for j in range(0, self.cfg.num_dim()):
               self.pos[i,j] = self.x_min [j] + rx[i, j]  * (self.x_max[j] - self.x_min[j])
               self.vel[i,j] = self.v_max [j] * (rv[i,j] - 0.5)  
       self.__velocity_cut()

       self.__boundary_conditions()

       self.update(0) 


    def move (self):

       xi_1  = np.random.rand(self.cfg.num_part(), self.cfg.num_dim())
       xi_2  = np.random.rand(self.cfg.num_part(), self.cfg.num_dim())

       for i in range(0, self.cfg.num_part()):
           for j in range(0, self.cfg.num_dim()):
               self.vel[i,j]  = self.cfg.weight_inertia() * self.vel[i,j]\
               + xi_1[i,j] * self.cfg.weight_self_learning() * (self.p_best[i,j]-self.pos[i,j])\
               + xi_2[i,j] * self.cfg.weight_social_learning() * ( self.g_best[j]-self.pos[i,j])

       self.__velocity_cut()

       self.pos = self.pos + self.vel                   

       self.__boundary_conditions()
 

    def __velocity_cut(self):
        for i in range(0, self.cfg.num_part()):
           for j in range(0, self.cfg.num_dim()):
               if self.vel[i,j] > self.v_max[j]:
                  self.vel[i,j] = self.v_max[j]

               if self.vel[i,j] < - self.v_max[j]:
                  self.vel[i,j] = - self.v_max[j]


    def __boundary_conditions (self):
 
       for i in range(0, self.cfg.num_part()):
          for j in  range(0, self.cfg.num_dim()): 
              if self.pos[i,j] > self.x_max[j]:
                  self.pos[i,j] = self.x_max[j]
                  self.vel[i,j] = - self.vel[i,j] 
              if self.pos[i,j] <  self.x_min[j]:
                  self.pos[i,j] = self.x_min[j]
                  self.vel[i,j] = - self.vel[i,j]  
 
    def update (self, itr):

       columns = ["iter","part", "func","p_best"] + ["dim_"+str(i) for i in range(0, self.cfg.num_dim())]

       df = pd.DataFrame(columns=columns)

       y = np.array([self.cfg.cost_function()(self.pos[i,:])
           for i in range (0, self.cfg.num_part())])

       for i in range(0, self.cfg.num_part()):
           if y[i] < self.yp_best[i]:
               self.p_best[i,:]  = self.pos[i,:] 
               self.yp_best[i] = y[i] 
           df.loc[i] =  [itr, i, "%12.6e" % y[i]] + get_row(self.yp_best[i], self.p_best[i,:])  
      
       for i in range(0, self.cfg.num_part()):
            if self.yp_best[i] < self.best:
                self.g_best = self.p_best[i,:]  
                self.best = self.yp_best[i]
       return df

