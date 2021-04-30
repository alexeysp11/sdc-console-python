import traceback
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

class Sensor(): 
    def measure(self, init_data, abs_error):
        """
        Adds gaussian noise to array of truth value. 

        Returns: 

        `observations`: noisy observation of a sensor (truth value plus 
        gaussian noise). 
        """
        
        try:
            # initial data 
            truth_value = init_data[0]
            init_guess = init_data[1]
            time_sec = init_data[2] 
            
            if type(truth_value) == float:
                array_size = (time_sec, 1)
            else:
                array_size = truth_value.shape
            
            sigma = abs_error / 2 
            
            # determine observations
            observations = np.ones(array_size)
            observations = np.random.normal(truth_value, sigma, size=array_size)
            
            return observations
        
        except Exception as e:
            print('Exception: '.upper(), e)
            traceback.print_tb(e.__traceback__)
            return None
