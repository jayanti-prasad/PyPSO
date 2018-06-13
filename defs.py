#!/usr/bin/python 

def   print_summary(summary_file,ndim,psofunc,xmin,xmax,\
      niter,seed,vlimits,constr,refwall,wvary,gaussian,eta,YGbest):

      fp=open(summary_file,"w")
      fp.write("===================================================\n")
      fp.write("PSO run summary \n")
      fp.write("User Inputs:\n")
      fp.write("Optimization function : %s\n" % psofunc)
      fp.write("Xmin                  : %10.6f\n"% xmin)
      fp.write("Xmax                  : %10.6f\n"% xmax)
      fp.write("niter                 : %d \n" % niter)
      fp.write("seed                  : %d \n" % seed) 
      fp.write("ndim                  : %d \n" % ndim)
      fp.write("constriction          : %d \n" % constr)
      fp.write("Maximum velocity      : %d \n" % vlimits)
      fp.write("Inertia weight var    : %d \n" % wvary) 
      fp.write("Reflecting Wall       : %d \n" % refwall)
      fp.write("Gaussian              : %d \n" %gaussian)
      fp.write("YGbest                : %10.6e\n"% YGbest)
      fp.write("eta                   : %8.4f\n"% eta)
      fp.write("===================================================\n")
      fp.close()
