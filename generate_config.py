
import model as model 
import simulation as sim 
from experimental_setup import generate_config_csvs
import numpy as np 
import pandas as pd

def generate_config_files(no_folders ):
    config = {}
    config['num_CCs'] = 100
    config['num_groups']= 9900 # if n = num_CCs, should be n(n-1)
    config['num_users'] = 49500 # should be a multiple of num_groups
    config['num_steps'] = 100
    config['record_at_timesteps'] = '"[2,5,10,20,50, 100]"'
    config['time_agg'] = '"[1001]"'
    config['rs_model'] = 'Comparison_random'
    config['uniform']= True 
    config['probability'] = 1

    config['alpha'] = 1
    changing = {}
    # we need a list of changing varaibles because lists are not hashable --> useful for dict
    changing_var_lists = [['random_seed']]
    #changing_var_lists = [['random_seed'], ['time_perm']]

    gen = np.random.RandomState(97)
    changing[0] = [[x] for x in gen.randint(1000000, size=1)]

    base_config = config 
    generate_config_csvs(base_config, changing, changing_var_lists, path='Simulation_results',
                            no_folders=1, start_config_no=-1, regenerate_seeds=False)