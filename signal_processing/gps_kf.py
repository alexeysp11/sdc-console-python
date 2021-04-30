import sys, traceback 

sys.path.append('../sensors')
sys.path.append('../maths')

from sensors.sensor import Sensor 
from maths.kalman_filter import KalmanFilter 
from .spa import SignalProcessingAlgorithm
import numpy as np


class GpsKF(SignalProcessingAlgorithm):
    def callkf(self, dimension=1, init_data=0):
        """
        Invokes Kalman filter for 1D and 2D and plots graphs.  
        """
        
        # usually error of GPS receiver is about 50 meters
        abs_error = 10.0
        
        try:
            sensor = Sensor()
            
            # generate GPS observations. 
            obs = sensor.measure(init_data, abs_error=abs_error)
            
            # initialize an instance of KalmanFilter and estimate
            kf = KalmanFilter(obs, error=abs_error)
            est = kf.estimate()
            
            # print out results and plot all. 
            self.mean, self.median, est_error = self.print_out(obs, est, 
                init_data)
            
            self.plot(obs=obs, est=est, est_error=est_error,  
                init_data=init_data, dim=dimension, sensor='gps')
        
        except Exception as e:
            print('Exception: '.upper(), e)
            traceback.print_tb(e.__traceback__)
