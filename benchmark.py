#!/usr/bin/python 
import numpy as np

# function (0) 
# Is defined for any range (-10.0,10.0)  
def Parabola(X):
   n=len(X)
   y = 0.0
   for i  in range(0,n):
        y = y + (X[i])**2.0 
   return(y) 


# function (1)
# defined for x in [-30,30]
def Rosenbrock(X):
    n = len(X)
    y = 0.0 
    for i in range(0,n-1):
        y = y + 100.0 *(X[i+1]-X[i]*X[i])**2.0+ \
          (X[i]-1.0)**2.0
    return(y) 

# function (2)  
# defined for x in [-5.12,5.12]
def Rastrigin(X):
      n = len(X) 
      y = 0.0 
      for i in range(0,n): 
          y = y + X[i]**2.0 - 10.0 * (np.cos(2.0*np.pi*X[i])-1.0)
      return(y)
  
 
# function (3) 
# defined for x in [-600,600]
def  Griewank(X):
    n = len(X)  
    y = 1.0
    tmp = 1.0
    for i in  range(0,n):
       y = y + 0.00025 * (X[i])**2.0 
       tmp = tmp * np.cos(X[i]/np.sqrt(float(i)+1.0))    
    return(y-tmp)
 

# function (4) 
#  defined for x in [-500,500]
def Schwefel(X):
    n = len(X) 
    y =  n * 418.9829  
    for i in range(0,n):
        y=y - X[i] * np.sin(np.sqrt(np.abs(X[i])))
    if ( y < 0.0) :
       print X, y 
    return(y) 
 
# function (5)
# defined for x in [-32,32]
def  Ackley(X):
    n  = len(X)
    y1 = 0.0
    y2 = 0.0
    for i in range(0,n):
       y1 = y1 + X[i]*X[i]
       y2 = y2 + np.cos(2.0*np.pi*X[i])

    y1 = -0.20*np.sqrt(y1/n)
    y2 = y2/n 
    y = -20.0 * np.exp(y1)-np.exp(y2)+20.0+ np.exp(1.0)
    return(y)

# function (6) 
# defined for x in [-10,10]

def  Levy(X):
    n = len(X)
    w=[]
    for i in range(0,n):
        w.append(1.0+(X[i]-1.0)/4.0)

    y2 = 0.0
    y1 = (np.sin(np.pi*w[0]))**2.0
    y2 = 1.0 + (np.sin(2.0*np.pi*w[n-1]))**2.0
    y2 = y2 * (w[n-1]-1.0)**2.0
    y  = y1 + y2

    for i in range(1,n-2):
         y2 = 1.0 + 10.0*(np.sin(np.pi*w[i]+1.0))**2.0
         y = y + y2 *(w[i]-1.0)**2.0
    return(y)

# function (7)
# defined for x in [-5,10]
def  Zakharov(X):
    n  = len(X)
    y1 = 0.0
    y2 = 0.0
    for i in range(0,n):
        y1 = y1 + X[i] * X[i] 
        y2 = y2 + 0.5 *(i+1) * X[i] 
    y = y1 + y2**2.0 + y2**4.0 
    return(y)

 

# function (8)
# defined for x in [-5,
def StyblinskiTang(X):
    n = len(X) 
    
    y = 0.0
    for i in range(0,n):
        y=y+X[i]**4.0 - 16.0*X[i]**2.0 + 5.0 * X[i] 
    y=y/2
    return(y) 

# function (9)
# defined for x in  [-10,10]
def  Alpine (X):
    n = len(X)
    y = 0.0

    for i in range(0,n): 
        y=y+np.abs(X[i]*np.sin(X[i])+0.1*X[i])
    return(y)     


def help():
    print("")
    print("This module defines some of the standard functions")
    print("which can be used for optimization problems like PSO.")
    print("All the function take a n dimensional vector X as input.")
    print("A list of functions with their range is as follows:")
    print("============================================ ==")
    print("S.No.  Function       Ranage    Dimension")
    print("===============================================")
    print("1      Parabola       Any              Any     ")
    print("2      Rosenbrock     [-30,30]         Any     ")
    print("3      Rastrigin      [-5.12,5.12]     Any     ")
    print("4      Griewank       [-600,600]       Any     ")
    print("5      Schwefel       [-100,100]       Any     ")
    print("6      Ackley         [-32,32]         Any     ")
    print("7      Levy           [-10,10]         Any     ")
    print("8      Zakharov       [-5,10]          Any     ")
    print("9      StyblinskiTang [-5,5]           Any     ")
    print("10     Alpine         [-10.10]         Any     ")
    print("===============================================")
    print("")

if __name__ == "__main__":
    X=[1.0,2.0,3.0] 
    C=[0.0,0.0,0.0]
    print Parabola(X,C) 


