import os
import sys
import argparse
import configparser
import config_pso  
import numpy as np 
from ParticleSwarm import Swarm, get_row  
import pandas as pd


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="cmod")
    parser.add_argument('-c', '--config', help='Config file path', required=True)
    parser.add_argument('-n', '--niter', help='Number of iterations', required=True)

    args = parser.parse_args()
    cfg_parser = configparser.ConfigParser()
    cfg_parser.read(args.config)
    cfg = config_pso.Config(cfg_parser)

    
    for section_name in cfg_parser:
        cfg.logger.info('Section:' +  section_name)
        section = cfg_parser[section_name]
        for name in section:
            cfg.logger.info('  {} = {}'.format(name, section[name]))
        cfg.logger.info("")

    fname = cfg.cost_function().__name__ 
    cfg.logger.info("optimizing for:" + fname)

    S = Swarm(cfg) 
 
    S.initilize() 

    columns= ["iter","g_best"] + ["dim_"+str(i) for i in range(0, cfg.num_dim())]

    dF = pd.DataFrame(columns=columns, dtype=float)

    df = pd.DataFrame()
    for i in range(0, int(args.niter)):
        S.move()
        df1 = S.update(i)
        df = pd.concat([df, df1], ignore_index=True)
        dF.loc[i]  = [i] + get_row(S.best, S.g_best)  
        cfg.logger.info(str(i) + ":" +str("%12.6E" % S.best) +":" +str(S.g_best))

    dF.to_csv(fname+"_gbest.csv")
    df.to_csv(fname+"_pbest.csv")

