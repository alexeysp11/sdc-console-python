"""
In this file we can determine a class of sensors which contain all of 
attributes and methods of any sensor (such as GPS, gyro etc).
"""

import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

class Sensor(): 
    def measure(self, init_data, abs_error):
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
            print('Info for developer'.upper())
            print(e)
            return None
    
    
    def plot(self, obs, est, init_data, dim, sensor, animation=False):
        # add animation and conclusions for overall medians!
        # define labels of each axis for each sensor!
        if sensor == 'gps': 
            truth_label = 'truth value'
            ylabel = 'Position (meters)'
        if sensor == 'gyro': 
            truth_label = 'truth yaw'
            ylabel = 'Rotation (degrees)'
        
        try:
            fig = plt.figure()
            
            truth_value = init_data[0]
            
            if (dim == 1 and sensor == 'gps') or (dim == 2 and sensor == 'gyro'): 
                plt.plot(obs,'k+', label='noisy measurements')
                plt.plot(est,'b-', label='a posteri estimate')
                
                if type(truth_value) == float:
                    plt.axhline(truth_value, color='g', label=truth_label)
                else:
                    plt.plot(truth_value, color='g', label=truth_label)
                
                plt.legend()
                plt.title(f'{sensor} data processing'.upper(), fontweight='bold')
                plt.xlabel('Time (seconds)')
                plt.ylabel(ylabel)
                plt.grid()
            
            if (dim == 2 and sensor == 'gps') or (dim == 3 and sensor == 'gyro'): 
                """
                In order to drawing plots for 2d space location estimating, we plot: 
                1) 2 diagrams of Estimation vs Data with respect to each 
                axis, 
                2) one diagram which represents a map with car's 
                trajectory in 2d space. 
                """
                
                # map 
                mapping = fig.add_subplot(121)
                mapping.plot(obs[:,0], obs[:,1],'k+', label='noisy measurements')
                mapping.plot(est[:,0], est[:,1],'bo', label='a posteri estimate')
                
                if len(truth_value[:,0]) == 1:
                    # if the car is not moving
                    mapping.plot(truth_value[:,0], truth_value[:,1], 'go', label='truth value')
                else:
                    mapping.plot(truth_value[:,0], truth_value[:,1], 'g', label='truth value')
                
                plt.xlabel('Position X (meters)')
                plt.ylabel('Position Y (meters)')
                plt.title('2d map'.upper(), fontweight='bold')
                plt.legend()
                plt.grid()
                
                # diagram with respect to X
                pos_X = fig.add_subplot(222)
                pos_X.plot(obs[:,0],'k+')
                pos_X.plot(est[:,0],'b-')
                pos_X.plot(truth_value[:,0], color='g')
                plt.title(f'{sensor} data processing'.upper(), fontweight='bold')
                plt.ylabel('Position X (meters)')
                plt.grid()
                
                # diagram with respect to Y
                pos_Y = fig.add_subplot(224)
                pos_Y.plot(obs[:,1],'k+')
                pos_Y.plot(est[:,1],'b-')
                pos_Y.plot(truth_value[:,1], color='g')
                plt.xlabel('Time (seconds)')
                plt.ylabel('Position Y (meters)')
                plt.grid()
            
            plt.show()
        
        except Exception as e:
            print('Info for developer'.upper())
            print(e)
    
    
    def print_out(self, obs, est, init_data, table=True):
        try:
            truth_value = init_data[0]
            
            # reshape for a table (for 1D)
            if type(truth_value) is float:
                obs = obs.reshape((len(obs), 1))
                est = est.reshape((len(est), 1))
            
            # round values for printing out a table!
            obs = np.round(obs, 3)
            est = np.round(est, 3)
            
            # calculate error of estimations
            error = np.round(truth_value - est, 3)
            
            if table == True:
                # making a table
                if type(truth_value) == float: 
                    data = [[est, error, obs]]
                    
                    headers = ['Estimations', 'Error', 'Observations']
                    
                    print('\nDATA PROCESSING:')
                    print(tabulate(data, headers=headers))
                
                elif len(truth_value) <= 20:
                    data = [[truth_value, est, error, obs]]
                    
                    headers = ['Truth value', 'Estimations', 'Error', 'Observations']
                    
                    print('\nDATA PROCESSING:')
                    print(tabulate(data, headers=headers))
            
            # get number of columns
            cols = len(error[0,:])
            
            # for 1D 
            if cols == 1:
                # calculate and print out measures of central tendency
                median = np.round(np.median(abs(error)))
                mean = np.round(np.mean(abs(error)))
                print('Measures of central tendency of error:')
                print(f'median = {median}, mean = {mean}')
            
            # for 2D 
            if cols == 2: 
                # calculate and print out measures of central tendency
                median_X = np.round(np.median(abs(error[:,0])), 3)
                median_Y = np.round(np.median(abs(error[:,1])), 3)
                mean_X = np.round(np.mean(abs(error[:,0])), 3)
                mean_Y = np.round(np.mean(abs(error[:,1])), 3)
                print('Measures of central tendency of error:')
                print(f'median_X = {median_X}, mean_X = {mean_X}')
                print(f'median_Y = {median_Y}, mean_Y = {mean_Y}')
                
                mean = np.array([[mean_X, mean_Y]])
                median = np.array([[median_X, median_Y]])
            
            print()

            return mean, median
        
        except Exception as e:
            print('Info for developer'.upper())
            print(e)
            return None, None
