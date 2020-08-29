"""
Call IMU (GPS, gyro, accelerometer), DATMO (LIDAR, radar), 
Neural Networks and Fuzzy controller.
"""

import sys
sys.path.append('../RTLS')
sys.path.append('../DATMO')
sys.path.append('../fuzzy_controller')
sys.path.append('../computer_vision')
import env
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
        velocity, accel = env.setting(mode)
        
        imu_1d = ImuKF()
        init_data = input_data.custom_or_default_data(dimension=1, 
                                                      init_velocity=velocity, 
                                                      mode=mode,
                                                      accel=accel)
        imu_1d.callkf(dimension=1, init_data=init_data)
        
        imu_2d = ImuKF()
        init_data = input_data.custom_or_default_data(dimension=2, 
                                                      init_velocity=velocity, 
                                                      mode=mode,
                                                      accel=accel)
        imu_2d.callkf(dimension=2, init_data=init_data)
    
    except Exception as e:
        print('Info for developer:'.upper())
        print(e)


def gps(mode):
    try:
        velocity, accel = env.setting(mode)
        
        kf_1d = GpsKF()
        init_data = input_data.custom_or_default_data(dimension=1, 
                                                      init_velocity=velocity, 
                                                      mode=mode,
                                                      accel=accel)
        kf_1d.callkf(dimension=1, init_data=init_data)
        
        kf_2d = GpsKF()
        init_data = input_data.custom_or_default_data(dimension=2, 
                                                      init_velocity=velocity, 
                                                      mode=mode,
                                                      accel=accel)
        kf_2d.callkf(dimension=2, init_data=init_data)
    
    except Exception as e:
        print('Info for developer:'.upper())
        print(e)


def gyro(mode):
    if mode == 'c':
        const_rotation = True
    elif mode == 'nu':
        const_rotation = False

    try:
        gyro_2d = GyroKF()
        gyro_2d.callkf(dim=2, const_rotation=const_rotation)
    
    except Exception as e:
        print('Info for developer:'.upper())
        print(e)

def accel():
    try:
        accel = Accelerometer()
        accel.run()
    
    except Exception as e:
        print('Info for developer:'.upper())
        print(e)

def lidar():
    try:
        lidar = Lidar()
        lidar.call_lidar()
    
    except Exception as e:
        print('Info for developer:'.upper())
        print(e)


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
        print('Info for developer:'.upper())
        print(e)


def fuzzy():
    try:
        fc = CallFuzzy()
        fc.call()
    
    except Exception as e:
        print('Info for developer:'.upper())
        print(e)


def test():
    pass
