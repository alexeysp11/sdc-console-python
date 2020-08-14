"""
Lidar observations.

This module gets truth position of obtacles from a map, 
measures and prpcesses it and then sends it to another map. 

LIDAR Lite v2
frequency: 50 Hz
accuracy: 2.5 cm
distance: 40 m
"""


from sensor import Sensor
from obstacle import Obstacle
import numpy as np
import math


class Lidar:
    def call_lidar(self): 
        sensor = Sensor()
        
        init_data = self.initialize()
        cartesian = sensor.measure(init_data)
        sensor.plot(init_data)
    
    
    def initialize(self, mock=True, display=True):
        if mock == True:
            frequency = 50
            accuracy = 0.025 
            distance = 40 
            min_angle = 0
            max_angle = 360
            auto = np.array([0,0])
        else: 
            # input initial data 
            print('INITIAL DATA')
            frequency = float(input('frequency: '))
            accuracy = float(input('accuracy: '))
            distance = float(input('distance (m): '))
            max_angle = int(input('max_angle (degrees): '))
        
        if display == True:
            # print out dummy data
            print(f'frequency: {frequency}')
            print(f'accuracy: {accuracy}')
            print(f'distance (m): {distance}')
            print(f'max_angle (degrees): {max_angle}')
            print(f'coordinates of auto: {auto}')
        
        obstacle = Obstacle()
        env, auto = obstacle.borders()
        
        return (env, accuracy, max_angle, frequency, distance, auto)
