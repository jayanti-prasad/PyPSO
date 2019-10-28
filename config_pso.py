import sys
import os
from pathlib import Path
import logging
import logging.handlers
import benchmark

def get_logger(logger_name, log_dir, log_file, log_level='DEBUG', log_to_console=True):

    root_logger = logging.getLogger(logger_name)
    root_logger.setLevel(log_level)
    handler = logging.handlers.RotatingFileHandler(log_dir + os.sep + log_file, maxBytes=10000000, backupCount=10,
                                                   encoding='utf-8')
    formatter = logging.Formatter('%(name)s - %(asctime)s -%(levelname)s - %(message)s')
    handler.setFormatter(formatter)  # Pass handler as a parameter, not assign
    root_logger.addHandler(handler)
    if log_to_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        root_logger.addHandler(console_handler)
    return root_logger


class Config :
    def __init__(self, cfg_parser, log=None):
        self.cfg_parser = cfg_parser

        self.logger = get_logger(self.log_name(),\
               self.log_dir(), self.log_file(), self.log_level())


    def workspace_dir(self):
        dir_val = self.cfg_parser.get("settings","workspace_dir")
        os.makedirs (dir_val, exist_ok=True)
        return dir_val
 
    def cost_function (self):
         func_name = self.cfg_parser.get('settings', 'cost_function') 
         return getattr(benchmark, func_name)

    def num_processes(self):
        return  self.cfg_parser.getint('settings', 'num_processes')

    def num_dim(self):
        return  self.cfg_parser.getint('settings', 'num_dim')

    def num_part(self):
        return  self.cfg_parser.getint('settings', 'num_part')

    def weight_inertia(self):
        return  self.cfg_parser.getfloat('settings', 'weight_inertia')

    def weight_self_learning(self):
        return  self.cfg_parser.getfloat('settings', 'weight_self_learning')

    def weight_social_learning(self):
        return  self.cfg_parser.getfloat('settings', 'weight_social_learning')

    def vel_max(self):
        return  self.cfg_parser.getfloat('settings', 'vel_max')

    def random_seed(self):
        return  self.cfg_parser.getint('settings', 'random_seed')

    def log_dir (self):
        dir_val =  self.workspace_dir () + os.sep + "log"
        os.makedirs (dir_val, exist_ok=True)
        return dir_val

    def log_level(self):
        return self.cfg_parser.get('log', 'log_level')

    def log_file(self):
        return self.cfg_parser.get('log', 'log_file')

    def log_name(self):
        return self.cfg_parser.get('log', 'log_name')

    def x_max(self):
        return  self.cfg_parser.getfloat('parameters', 'x_max')

    def x_min(self):
        return  self.cfg_parser.getfloat('parameters', 'x_min')


