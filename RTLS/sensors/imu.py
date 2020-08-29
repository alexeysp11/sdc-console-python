"""
In this source file we just invoke GPS, gyro and accelerometer and then 
process data from them. 
"""

import sys 
from .sensor import Sensor 
from models.kalman_filter import KalmanFilter as kf 
import numpy as np


class ImuKF:
    def callkf(self, kf=kf, plot=True, dimension=1, init_data=0):
        pass