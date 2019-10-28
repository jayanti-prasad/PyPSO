import numpy as np
import sys

def get_range():
    D={'Parabola': [-10.0,10.0]}
    D['Rosenbrock'] = [-30.0,30.0]
    D['Rastrigin'] = [-5.12, 5.12]
    D['Grienwank'] = [-600.0,600.0]
    D['Schwefel'] = [-500.0,500.0]
    D['Ackley'] = [-32.0,32.0]
    D['Levy'] = [-10.0,10.0]
    D['Zakharov'] = [-5.0,10.0]
    D['StyblinskiTang']=[-5.0,5.0]
    D['Alpine'] = [-10.0,10.0]
    return D  


def Parabola(X):
   y = 0.0
   for i in range(0, len(X)):
      y = y + X[i] * X[i]
   return y 


def Rosenbrock(X):
    y = 0.0
    for i in range(0,len(X)-1):
        y = y + 100.0 *(X[i+1]-X[i]*X[i])**2.0 + \
          (X[i]-1.0)**2.0
    return(y)

def Rastrigin(X):
    y = 0.0
    for i in range(0, len(X)):
        y = y + X[i]**2.0 - 10.0 * (np.cos(2.0*np.pi*X[i])-1.0)
    return(y)


def  Grienwank(X):
    y = 1.0
    tmp = 1.0
    for i in  range(0,len(X)):
       y = y + 0.00025 * (X[i])**2.0
       tmp = tmp * np.cos(X[i]/np.sqrt(float(i)+1.0))
    return(y-tmp)


def Schwefel(X):
    y = len(X) * 418.9829  
    for i in range(0, len(X)):
        y  = y  - X[i] * np.sin(np.sqrt(np.abs(X[i])))
    print(y)
    return y 


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



def  Zakharov(X):
    y1 = 0.0
    y2 = 0.0
    for i in range(0,len(X)):
        y1 = y1 + X[i] * X[i]
        y2 = y2 + 0.5 *(i+1) * X[i]
    y = y1 + y2**2.0 + y2**4.0
    return(y)


def StyblinskiTang(X):
    y = 0.0
    for i in range(0, len(X)):
       y  = y + (X[i] **4 -16.0 * X[i]**2 + 5.0 * X[i])/2.0
    return y 


def  Alpine (X):
    y = 0 
    for i in range(0, len(X)): 
       y = y + np.abs(X[i]*np.sin(X[i])+0.1*X[i])
    return y

