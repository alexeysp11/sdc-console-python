"""
This function should generate observations but not models, models
should process observations.

Add acceleration and non-unform motion to this source file. 

Some parts of this file should be written in velocity.py, 
in this file we just select mode (constant or different velocity, 
uniform or non-uniform acceleration, uniform or non-uniform motion)
and edit properties.

We are going to check which approach is more efficient for estimating car's 
location: with constant process_var (see kf) or adjusted process_var 
(see kf_const_velocity) in models folder. 
In general adjusted algorithm estimates position of a car moving with
constant velocity a little bit more accurate than algorithm with constant 
process_var does. 

In order to make some conclusions about that we are going to calculate measures 
of central tendency (mean and median) of an array of error (difference between 
truth_value and estimated value) for each algorithm.
And we need to repeat this several times, initialize arrays of means 
and medians, calculate mean and median again and compare algorithms, 
so add for cycle. 
Also I can improve this algorithm to find out if result depend on n_iter and 
time_sec. 
"""

import sys, traceback 
from .sensor import Sensor 
from models.kalman_filter import KalmanFilter as kf 
import numpy as np

class GpsKF():
    def callkf(self, kf=kf, dimension=1, init_data=0):
        """
        Invokes Kalman filter for 1D and 2D and plots graphs.  
        """
        # usually error of GPS receiver is about 50 meters
        abs_error = 10.0
        
        try:
            sensor = Sensor()
            
            # generate observations
            obs = sensor.measure(init_data, abs_error=abs_error)
            
            if dimension == 1: 
                # initialize an instance of KalmanFilter and estimate
                kf_1d = kf(obs, error=abs_error)
                est = kf_1d.estimate()
                
                # print out results and plot all. 
                self.mean, self.median, est_error = sensor.print_out(obs, est, 
                    init_data)
                
                sensor.plot(obs=obs, est=est, est_error=est_error,  
                    init_data=init_data, dim=dimension, sensor='gps')
            
            if dimension == 2: 
                # initialize an instance of KalmanFilter and estimate
                kf_2d = kf(obs, error=abs_error)
                est = kf_2d.estimate()
                
                # print out results and plot all. 
                self.mean, self.median, est_error = sensor.print_out(obs, est, 
                    init_data)
                
                sensor.plot(obs=obs, est=est, est_error=est_error,  
                    init_data=init_data, dim=dimension, sensor='gps') 
        
        except Exception as e:
            print('Exception: '.upper(), e)
            traceback.print_tb(e.__traceback__)
