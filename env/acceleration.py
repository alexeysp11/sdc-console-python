"""
This file will imitate acceleration of a car and send its attributes 
to the motion file and KF models. 
"""

import numpy as np
import random

def define_accel(size, accel): 
    start = -1
    stop = 1
    
    time_sec = size[0]
    
    if accel == True:
        accel = np.zeros(size)
        for i in range(time_sec):
            accel[i] = random.uniform(start, stop)
    else: 
        accel = np.zeros(size)
    
    return accel