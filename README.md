# Particle Swarm Optimization 

# What it is ? :
- Particle Swarm Optimization or PSO is an agent based optimization method in which a set 
  of computational agents - called particles, exhibit random walks in a higher dimensional
  parameter space to find the global maximum/minimum.

- In order to use the python code provided here you have to do the following:

   - Provide a cost function or optimization functions you want to use. A set of
     standard cost (benchmark) functions are provided  in benchmark.py file.

   - Review and modify the config file (pso.ini) which is also provided. 

# How to run the code ? 

    > `$ python driver_training.py -c pso.ini`
    
# Output of the code 

- The run of the code once over will create two files : func\_pbest.csv and func\_gbest.csv 
  which have the positions of all the particles at all epochs and the position and value
  of the global minimum as it gets updated with iteration.

- There are plotting programs which can be used for post processing.

- For detail you can check <a href="https://jayanti-prasad.github.io/pso.html" target="dynamic"> here </a>
 

