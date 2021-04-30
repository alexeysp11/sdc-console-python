import sys, traceback 

sys.path.append('../sensors')
sys.path.append('../math')

from sensors.sensor import Sensor 
from maths.kalman_filter import KalmanFilter 
from .spa import SignalProcessingAlgorithm
import numpy as np


class ImuKF(SignalProcessingAlgorithm):
    """
    This class allows to model Kalman Filter algorithm for processing 
    data from IMU that consists of GPS, accelerometer.
    """

    def callkf(self, dimension=1, init_data=0):
        """
        Invokes Kalman filter for 1D and 2D and plots graphs.  
        """

        gps_error = 10.0
        accel_error = 0.001
        
        try:
            sensor = Sensor()
            
            # generate GPS observations. 
            gps_obs = sensor.measure(init_data, abs_error=gps_error)
            
            # generate accelerometer observations. 
            accel_obs = sensor.measure(init_data, abs_error=accel_error)
            
            # initialize an instance of KalmanFilter and estimate
            kf = KalmanFilter(gps_obs, error=gps_error)
            est = kf.estimate()
            
            # print out results and plot all. 
            self.mean, self.median, est_error = self.print_out(gps_obs, est, init_data)
            
            self.plot(obs=gps_obs, est=est, est_error=est_error,  
                init_data=init_data, dim=dimension, sensor='imu')
        
        except Exception as e:
            print('Exception: '.upper(), e)
            traceback.print_tb(e.__traceback__)
