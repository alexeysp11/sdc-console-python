"""
This file will imitate acceleration of a car and send its attributes 
to the motion file and KF models. 
"""

import numpy as np
import random

def define_accel(size, is_accel): 
    start = -1
    stop = 1
    
    time_sec = size[0]
    
    if is_accel == True:
        accel = np.zeros(size)
        
        for i in range(time_sec):
            if size[1] == 1:
                # if 1D
                accel[i] = random.uniform(start, stop)
            else:
                #if 2D
                accel[i, 0] = random.uniform(start, stop)
                accel[i, 1] = random.uniform(start, stop)
    
    else: 
        accel = np.zeros(size)
    
    return accel