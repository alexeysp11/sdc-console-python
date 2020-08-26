"""
Call IMU (GPS, gyro, accelerometer), DATMO (LIDAR, radar), 
Neural Networks and Fuzzy controller.
"""

import sys
sys.path.append('../RTLS')
sys.path.append('../DATMO')
import input_data
from sensors.gps import GpsKF
from sensors.gyro import GyroKF
from lidar import Lidar


def gps(mode):
    if mode == 'p':
        velocity = 0.0
        accel = False
    elif mode == 'v':
        velocity = 2.0
        accel = False
    elif mode == 'a':
        velocity = 2.5
        accel = True

    kf_1d = GpsKF()
    init_data = input_data.custom_or_default_data(dimension=1, init_velocity=velocity, accel=accel)
    kf_1d.callkf(dimension=1, init_data=init_data)
    
    kf_2d = GpsKF()
    init_data = input_data.custom_or_default_data(dimension=2, init_velocity=velocity, accel=accel)
    kf_2d.callkf(dimension=2, init_data=init_data)


def gyro(mode):
    if mode == 'c':
        const_rotation = True
    elif mode == 'nu':
        const_rotation = False

    gyro_2d = GyroKF()
    gyro_2d.callkf(dim=2, const_rotation=const_rotation)


def lidar():
    lidar = Lidar()
    lidar.call_lidar()
