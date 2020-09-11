"""
Call IMU (GPS, gyro, accelerometer), DATMO (LIDAR, radar), 
Neural Networks and Fuzzy controller.
"""

import sys, traceback
sys.path.append('../RTLS')
sys.path.append('../DATMO')
sys.path.append('../fuzzy_controller')
sys.path.append('../computer_vision')
import environment
import input_data
from sensors.imu import ImuKF
from sensors.gps import GpsKF
from sensors.gyro import GyroKF
from sensors.accelerometer import Accelerometer
from lidar import Lidar
from call_fc import CallFuzzy
from MNIST import mnist_default, mnist_custom
from road_signs import signs_default


def imu(mode):
    try:
        velocity, is_accel = environment.setting(mode)
        
        imu_1d = ImuKF()
        init_data = input_data.custom_or_default_data(dimension=1, 
                                                      init_velocity=velocity, 
                                                      mode=mode,
                                                      is_accel=is_accel)
        imu_1d.callkf(dimension=1, init_data=init_data)
        
        imu_2d = ImuKF()
        init_data = input_data.custom_or_default_data(dimension=2, 
                                                      init_velocity=velocity, 
                                                      mode=mode,
                                                      is_accel=is_accel)
        imu_2d.callkf(dimension=2, init_data=init_data)
    
    except Exception as e:
        print('Exception: '.upper(), e)
        traceback.print_tb(e.__traceback__)


def gps(mode):
    try:
        velocity1d, is_accel = environment.setting(mode, 1)
        velocity2d, is_accel = environment.setting(mode, 2)
        
        kf_1d = GpsKF()
        init_data = input_data.custom_or_default_data(dimension=1, 
                                                      init_velocity=velocity1d, 
                                                      mode=mode,
                                                      is_accel=is_accel)
        kf_1d.callkf(dimension=1, init_data=init_data)
        
        kf_2d = GpsKF()
        init_data = input_data.custom_or_default_data(dimension=2, 
                                                      init_velocity=velocity2d, 
                                                      mode=mode,
                                                      is_accel=is_accel)
        kf_2d.callkf(dimension=2, init_data=init_data)
    
    except Exception as e:
        print('Exception: '.upper(), e)
        traceback.print_tb(e.__traceback__)


def gyro(mode):
    if mode == 'c':
        is_const_rotation = True
    elif mode == 'nu':
        is_const_rotation = False

    try:
        gyro_2d = GyroKF()
        gyro_2d.callkf(dim=2, is_const_rotation=is_const_rotation)
    
    except Exception as e:
        print('Exception: '.upper(), e)
        traceback.print_tb(e.__traceback__)


def accel():
    try:
        accel = Accelerometer()
        accel.run()
    
    except Exception as e:
        print('Exception: '.upper(), e)
        traceback.print_tb(e.__traceback__)


def lidar():
    try:
        lidar = Lidar()
        lidar.call_lidar()
    
    except Exception as e:
        print('Exception: '.upper(), e)
        traceback.print_tb(e.__traceback__)


def neural_network(mode, default):
    try:
        """
        There is exception handling in if/else block too (programmer can set 
        mode or defualt variables in the wrong way, and I don't know how to 
        handle this exception not in if/else statement).
        
        So either watch carefully if the name of the file or the method 
        changes or think out how to use try/except in this situation.
        """
        
        if mode == 'mnist' and default == True:
            mnist_default.run()
        elif mode == 'mnist' and default == False:
            mnist_custom.run()
        elif mode == 'signs' and default == True:
            signs_default.run()
        else:
            print('Info for developer:'.upper())
            print('''Incorrect mode or default values in: 
            neural_network(mode, default) in invoke.py''')
    
    except Exception as e:
        print('Exception: '.upper(), e)
        traceback.print_tb(e.__traceback__)


def fuzzy():
    try:
        fc = CallFuzzy()
        fc.call()
    
    except Exception as e:
        print('Exception: '.upper(), e)
        traceback.print_tb(e.__traceback__)


def test():
    pass
