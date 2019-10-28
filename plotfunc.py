import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import benchmark
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
plt.rcParams.update({'font.size': 6})


if __name__ == "__main__":

    D = benchmark.get_range()
    print("Benchmark functions:", D.keys())

    func = getattr(benchmark, sys.argv[1])
    n =  int(sys.argv[2])

    print("getting data for", func.__name__)
    xmin, xmax = D[sys.argv[1]][0], D[sys.argv[1]][1] 
 
    x = y = np.arange(xmin, xmax,(xmax-xmin)/n)
    X, Y = np.meshgrid(x, y)
    zs = np.array(func([np.ravel(X), np.ravel(Y)]))
    Z = zs.reshape(X.shape)
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')


    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

    # Customize the z axis.
    #ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%5.2e'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.8,aspect=5)

    plt.savefig("images" + os.sep + sys.argv[1] + '.png')
                     


