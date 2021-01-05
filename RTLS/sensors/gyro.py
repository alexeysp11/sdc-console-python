"""
GYROSCOPE

In this source file I use terms like roll, yaw and pitch, so you can 
read the following article: 
https://en.wikipedia.org/wiki/Aircraft_principal_axes

Also this module can require angular velocity. 

NOTE: 
- It is necessary to find out an error of gyroscope in reality, 
- Add rotating model. 
"""

import sys 
from .sensor import Sensor 
sys.path.append('../../env')
from rotation import Rotation 
from models.kalman_filter import KalmanFilter as kf 
import numpy as np


class GyroKF():
    """
    We have `yaw` angle of some non-moving car, so
    here we pre-process gyro data before we pass it to the `KalmanFilter` 
    processing algorithm. 
    
    I decided that in this method I just initialize truth_yaw, 
    init_yaw, frequency and time_sec, so kf will generate measured 
    rotations accordingly to frequency and truth_yaw. 
    """
    
    def callkf(self, dim=2, is_const_rotation=True):
        abs_error = 15
        
        try:
            sensor = Sensor()
            
            # get initial data
            init_data = Rotation.initialize(dim=dim, is_const_rotation=is_const_rotation)
            
            obs = sensor.measure(init_data, abs_error)
            
            if dim == 2:
                # initialize an instance of KalmanFilter 
                kf2d = kf(obs, abs_error)

                # estimate, print out results and plot all  
                est = kf2d.estimate()
                mean, median = sensor.print_out(obs, est, init_data)
                sensor.plot(obs, est, init_data, dim=dim, sensor='gyro')
            
            if dim == 3:
                # initialize an instance of GyroKF
                kftest_2d = GyroKF()
                
                # get initial data and set it into a tuple 
                truth_value, init_guess, n_iter = kftest_2d.initdata_2d()
                kf_2d = kf(truth_value, init_guess, n_iter)
                
                # estimate 
                obs, est = kf_2d.estimate()
                kftest_2d.print_out(obs, est, kf_2d)
                kftest_2d.plot_2d(obs, est, kf_2d)
        
        except Exception as e:
            print('Exception: '.upper(), e)
            traceback.print_tb(e.__traceback__)
