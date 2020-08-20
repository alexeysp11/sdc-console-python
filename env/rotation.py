"""
Rotation
"""

import numpy as np
import random

class Rotation:
    pass 


class ConstRotation(Rotation): 
    def initialize(dim=2, const_rotation=True, mock=True, display=True):
        if dim == 2:
            if mock == True:
                # mock initial data (in angles)
                truth_yaw = 50.0
                init_yaw = 45
                
                # find out the frequency and error of MEMS gyroscope in reality!
                
                frequency = 2.0
                time_sec = 30
            
            else: 
                # input initial data
                print('INPUT INITIAL DATA')
                truth_yaw = float(input('Truth yaw: '))
                init_yaw = float(input('Initial yaw: '))
                frequency = float(input('Frequency: '))
                time_sec = float(input('Time (sec): '))
                
                # convert initial data into arrays 
                truth_value = (truth_value_X, truth_value_Y)
                init_guess = (init_guess_X, init_guess_Y)
            
            if display == True:
                # print out dummy data
                print('INITIAL DATA:')
                print(f'Truth value of yaw: {truth_yaw}')
                print(f'Initial guess: {init_yaw}')
                print(f'Frequency (Hz): {frequency}')
                print(f'Time (seconds): {time_sec}')
            
            # time delay of accelerometer between measurements
            dt = 1 / frequency
            n_yaw = int(time_sec / dt)
            shape = (time_sec, 1)

            if const_rotation == False: 
                truth_yaw = DifferentRotation.define_dif_rotation(truth_yaw, shape)
            
            return (truth_yaw, init_yaw, time_sec, n_yaw)
        
        if dim == 3: 
            pass 


class DifferentRotation(Rotation):
    def define_dif_rotation(first_truth_yaw, shape):
        truth_yaw = np.ones(shape)
        truth_yaw[0] = first_truth_yaw
        
        time_sec = shape[0]
        
        start = -1
        stop = 1

        for i in range(1, time_sec):
            truth_yaw[i] = truth_yaw[i-1] + random.uniform(start, stop)

        return truth_yaw
