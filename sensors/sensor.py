import traceback
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

class Sensor(): 
    def measure(self, init_data=np.zeros((3,1)), abs_error=0.0, unit='position', dt=1.0):
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

            time_array = np.arange(0, time_sec, dt)
            
            # assign truth value
            if type(truth_value[0]) == float:
                init_value = truth_value[0]
                truth_value = np.ones((int(time_sec/dt), 1))
            else:
                cols = len(truth_value[0][0,:])
                if unit == 'position':
                    init_value = truth_value[0]
                elif unit == 'velocity':
                    init_value = truth_value[1]
                elif unit == 'acceleration':
                    init_value = truth_value[2]
                truth_value = np.ones((int(time_sec/dt), cols))
            
            # reassign truth values
            k = 0
            for i in range(len(init_value)):
                for j in range(int(1/dt)):
                    if i == len(init_value)-1 or j == int(1/dt)-1:
                        truth_value[k] = init_value[i]
                    elif j == int(1/dt): 
                        truth_value[k] = init_value[i]
                    else:
                        truth_value[k] = init_value[i] + (init_value[i+1] - init_value[i]) * dt * j
                    k += 1
            
            sigma = abs_error / 2 
            
            # determine observations
            array_size = truth_value.shape
            observations = np.ones(array_size)
            observations = np.random.normal(truth_value, sigma, size=array_size)
            
            return observations, time_array
        
        except Exception as e:
            print('Exception: '.upper(), e)
            traceback.print_tb(e.__traceback__)
            return None
