import os
import sys
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
import benchmark
import argparse

"""
This programs plots positions of PSO particles 
projected on a 2-d space and super-impose those
on the contours of the optimization function'
"""


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="cmod")
    parser.add_argument('-i', '--input-func', help='Input function', required=True)
    parser.add_argument('-o', '--output-dir', help='Output dir', required=True)
    parser.add_argument('-n', '--niter', help='Number of grid points', required=True)

    args = parser.parse_args()
    func_name = args.input_func 
    os.makedirs (args.output_dir, exist_ok=True)

    D = benchmark.get_range()
    func = getattr(benchmark, func_name)
    n =  int(args.niter)
    print("getting data for", func.__name__)

    xmin, xmax = D[func_name][0], D[func_name][1]

    x_vals = np.linspace(xmin, xmax, n)
    y_vals = np.linspace(xmin, xmax, n)
    X1, Y1 = np.meshgrid(x_vals, y_vals)

    Z =  func([np.ravel(X1), np.ravel(Y1)])
    Z = Z.reshape(X1.shape)
 
    df = pd.read_csv(func_name + "_pbest.csv")

    ntimes = np.max(df['iter'].tolist())
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    levels = [0.0, 0.1, 1.0, 10.0, 20.0, 50.0, 100.0]

    for i in range(0, ntimes):
       plt.clf()
       fig_file = args.output_dir + os.sep + "slice_" + str(1000+i) +'.png'
       fig = plt.figure(figsize=(6,5))

       df1 = df.loc[df['iter'] == i] 
       X =  df1['dim_0'].tolist()
       Y =  df1['dim_1'].tolist()
       ax = fig.add_axes([left, bottom, width, height]) 
       cp = ax.contour(X1, Y1, Z, levels)

       ax.clabel(cp, inline=True, fontsize=10)

       plt.plot(X,Y,'b.')
       plt.xlim(xmin,xmax)
       plt.ylim(xmin,xmax)
       plt.title("iter=%4d" % i) 
       plt.savefig(fig_file)
       print("file file:" + fig_file)
