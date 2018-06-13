#!/usr/bin/python 
"""
-------------------------------------------------------------------------
PyPSO (1.0)  - A Python Particle Swarm Optimization code 
-------------------------------------------------------------------------
This code has two main componenets which can be used independently.
- Benchmark module (benchmark.py)- 
 This has definition of a set of benchmark functions commonly used for testing 
  ptimization modules.
- Particle Swarom Optimization Code (ParticleSwarm.py)
  This is the main PSO code which takes some input and give x_gbest, f(x_gbest)
  as well as values of f(x) at all values of x which PSO particles occupy.
PSO Inputs : Input to PSO are as follows 
    1. An Optimization function with search range [lower,upper]
    2. Number of dimensions (ndim) 
    3. Number of iterations (niter)
    4. Seed (for generating random numbers)
    Logical variables :
    5. vlimits - whether to use vmax 
    6. refwall - whether to use reflecting wall boundary 
    7. constr  - wheaher to use constriction factor
    9. wvary   - wheather to use varying w 
   10. gaussian - whether to use gaussian PSO 
PSO Output :
    1. A summary file 
    2. A Gbest file
    3. A particle data file  

 Note that the code try to find the global minimum and so if you want 
global maximum just reverse the sign. 
===========================================================================
Jayanti Prasad, April 10, 2018 
===========================================================================
"""
import numpy as np 
import sys
import benchmark as bnch 
import argparse
import defs 
import string

# we need to start with a vary high valy of f_gbest 
MAX_VAL=1.0E12

# these are the deafult values 
# number of PSO particles 
npart = 50
#number of dimensions 
ndim  = 30
# number of iterations 
niter = 1 
# default seed for generating random numbers 
seed =  123 

#default values for PSO desugn  parameters 
c1=1.494
c2=1.494
w =0.729
# to set maximum velocity which is used for setting the initial
# velocity as well as for velocity cut 
c_max = 0.5

# These are the deafult values
# no velocity maximum by default 
vlimits=False
# wheather to lowe inertial weight with iterations 
changew=False
# whether to use Bare Bone PSO
gaussian=False
# whather to use consitruction factor 
constr=False
#whether boundary condition used  
bndry=False          

# This is used to lower the inertia weight 
def getw(i,n):
    w_max  = 0.9
    w_min  = 0.4    
    dw = (w_max-w_min)/n 
    return(w_max -i * dw) 

# This is the main class which define PSO particles 
class PsoParticle:
    def __init__(self,tag,x,y,v,xpbest,ypbest):
        # these are PSO parameters  
        # Every particle has position x, velocity v, value of
        # function y, its personal best x_pbest and the value of
        # the function at pbest. We are keeping a tag also for the
        # particle 
        # The following defines a PSO Particle 
        self.tag = tag 
        self.x   = x
        self.y   = y 
        self.v   = v
        self.xpbest = xpbest
        self.ypbest = ypbest 


 # This is the move function for default PSO          
    def move(self,XGbest):

        np.random.seed(seed) 

        xi_1 = np.random.random(ndim)
        xi_2 = np.random.random(ndim)

        for i in range(0,ndim):
           self.v[i] =  w* self.v[i] + \
                        c1*xi_1[i]*(self.xpbest[i]-self.x[i])+\
                        c2*xi_2[i]*(XGbest[i] - self.x[i])
           self.x[i] = self.x[i] + self.v[i] 

# This is the move function for Gaussian PSO
    def move_gaussian(self,XGbest):

        np.random.seed(seed)

        for i in range(0,ndim):
            mu= (XGbest[i]+self.xpbest[i])/2.0  
            sigma=abs(XGbest[i]-self.xpbest[i])/2.0
            s = np.random.normal(mu, sigma, 1)
            self.x[i] = s
            
# Pbest has to be updated at every step 
    def Pbest(self):
        if (self.y < self.ypbest):
            self.ypbest = self.y
            for j in range(0,ndim):
                self.xpbest[j]=self.x[j] 

# Gbest has to be updated once  PBEST is done     
    def Gbest(self,XGbest,YGbest):
        if (self.ypbest < YGbest):
                 XGbest = self.xpbest
                 YGbest = self.ypbest 
                
        return XGbest,YGbest

# In case velocity maximum is used 
    def Vlimit(self,vmax):
         for i in range(0,ndim):
            if (self.v[i] > vmax[i]):
                self.v[i] = vmax[i]
            if (self.v[i] < -vmax[i]):
                self.v[i] = - vmax[i]

#In case boundary condition applied 
    def Boundary(self,xmin,xmax):
         for i  in range(0,ndim):
            if (self.x[i] < xmin[i]):
                self.x[i] = xmin[i]  
 
            if (self.x[i] > xmax[i]):
                self.x[i] = xmax[i] 


#This is the main program                  
if __name__=="__main__":
    
      parser = argparse.ArgumentParser()
      parser.add_argument('--ndim',type=int,help='Number of dimensions (def=30)')
      parser.add_argument('--pso-func', type=str,help='Cost function to minimize (nodef)')
      parser.add_argument('--lower', type=float,help='Lower bound of the parameters space (nodef)')
      parser.add_argument('--upper', type=float,help='Upper bound of the parameters space (nodef)')
      parser.add_argument('--niter', type=int,help='Number of iterations (def=1)')
      parser.add_argument('--seed', type=int,help='Seed for Random numbers (def=123)')
      parser.add_argument('--vlimits', action='store_true',help='If used maximum velocity (def=no)')
      parser.add_argument('--bndry', action='store_true',help='If Boundary condion used  PSO(def=no)')
      parser.add_argument('--wvary', action='store_true',help='If used wvary  (def=no)')
      parser.add_argument('--gaussian', action='store_true',help='If Gaussian PSO  (def=no)')

      if len(sys.argv) < 4:
         parser.print_usage()
         sys.exit(1)

      args = parser.parse_args()

      ndim=args.ndim
      psofunc=args.pso_func
      xmin=args.lower
      xmax= args.upper
      niter=args.niter
      seed=args.seed 
      vlimits=args.vlimits 
      gaussian=args.gaussian  
      wvary=args.wvary 
      bndry=args.bndry  
     
      # set the minimum and maximum for position/velocity 
      Xmin=[xmin]  * ndim 
      Xmax=[xmax]  * ndim 
      Vmax=[0.0]   * ndim 
      Vmin=[0.0]   * ndim 

      for i in range(0,ndim):
          Vmax[i] = Xmax[i]-Xmin[i] 
          Vmin[i] = - Vmax[i]           

      # Initilize gbest 
      XGbest=[0.0] * ndim 
      YGbest=MAX_VAL

      # Now set the initial positions an  velocities of particles randomly 
      np.random.seed(seed)

      r1 = np.random.random(ndim*npart)
      r2 = np.random.random(ndim*npart)
       
      Swarm=[] 
   
      for i in range(0,npart):
          x1=[]
          v1=[]
          xpbest=[0]*ndim
          ypbest = MAX_VAL 

          for j in range(0,ndim):
              x1.append(Xmin[j]+ r1[j+ndim*i] * (Xmax[j]-Xmin[j]))
              v1.append((r2[j+ndim*i]-1.0) * Vmax[j]) 

          y1 = getattr(bnch, psofunc)(x1)
      
          P=PsoParticle(i,x1,y1,v1,xpbest,ypbest)
          Swarm.append(P)
       
      # now compute pbest
     
      for i in range(1,npart):
          Swarm[i].Pbest()
    
      # now compute gbest 
      for i in range(1,npart):
          XGbest,YGbest=Swarm[i].Gbest(XGbest,YGbest)

      YGbest_start = YGbest

      #for i in range(0,npart):
      #     print "Starting Pbest:", Swarm[i].ypbest,Swarm[i].xpbest
      
      # now we will iterate 

      tag=str(psofunc).lower()
      
      fp1=open(tag+"_data.dat","w")  # file to write x, f(x) 
      fp2=open(tag+"_gbest.dat","w")  # file to write gbest  
      summary_file=tag+"_summary.dat"
      
      for i in range(1,niter):
           for j in range(1,npart):

               seed = seed + 2 *i + 3 *j  

               if (wvary) : 
                   w_vary = getw(i,niter)    

              # update positions and velocities

               if (gaussian): 
                   Swarm[j].move_gaussian(XGbest)
               else:
                   Swarm[j].move(XGbest)

              # Apply Vmax cut is asked for   
               if (vlimits) :
                  Swarm[j].Vlimit(Vmax)     

              #Apply BOundary condition 
               if (bndry) :
                  Swarm[j].Boundary(Xmin,Xmax)   


              # compute the cost function 
               Swarm[j].y  = getattr(bnch, psofunc)(Swarm[j].x)

              # find pbest for every particle 
               Swarm[j].Pbest()
               
              # find gbest for the swarm  
               XGbest,YGbest=Swarm[j].Gbest(XGbest,YGbest)
               
              # write the positions at every step  
               fp1.write("%d  "  % i)
               fp1.write("%d  "  % j)
               fp1.write("%12.6e "  % Swarm[j].y) 
               for k in range(1,ndim):
                   fp1.write("%12.6e "  % Swarm[j].x[k]) 
               fp1.write("\n")

           # write gbest at every iteration  
           fp2.write(" %d " % i)
           fp2.write(" %12.6e " % YGbest)
           for j in range(1,ndim):
               fp2.write(" %12.6e " % XGbest[j])
           fp2.write("\n")

      fp1.close()
      fp2.close()
      eta = - np.log10(YGbest/YGbest_start)
      print "function=",psofunc,"eta=",eta,"YGbest=",YGbest 
      defs.print_summary(summary_file,ndim,psofunc,xmin,xmax,niter,seed,\
                         vlimits,constr,bndry,wvary,gaussian,eta,YGbest)
 
      
