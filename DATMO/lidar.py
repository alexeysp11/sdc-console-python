"""
Lidar observations.

This module gets truth position of obtacles from a map, 
measures and prpcesses it and then sends it to another map. 

LIDAR Lite v2
frequency: 50 Hz
accuracy: 2.5 cm
distance: 40 m

NOTE:
- class Lidar probably should inherit from class Sensor. 
"""

from obstacle import Obstacle
import numpy as np
import math
import matplotlib.pyplot as plt


class Lidar:
    def call_lidar(self): 
        init_data = self.initialize()
        cartesian = self.measure(init_data)
        self.plot(cartesian, init_data)
    
    
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
        borders = obstacle.borders()
        
        return (borders, accuracy, max_angle, frequency, distance, auto)
    
    
    def measure(self, init_data): 
        borders = init_data[0]
        accuracy = init_data[1]
        max_angle = init_data[2]
        frequency = init_data[3]
        distance = init_data[4]
        
        sigma = accuracy / 2
        
        # allocate space to the observations arrays
        obs = np.ones((frequency, max_angle))
        x_obs = np.ones((frequency, max_angle))
        y_obs = np.ones((frequency, max_angle))
        x = np.ones((1, max_angle))
        y = np.ones((1, max_angle))
        
        for i in range(frequency):
            for angle in range(max_angle): 
                """
                1) Get coordinates of obtacles in polar coordinate system, 
                2) Transform these coordinates into Cartesian coordinate system. 
                """
                obs[i, angle] = np.random.normal(borders, sigma, size=(1,1))
                x_obs[i, angle] = obs[i, angle] * np.cos(angle)
                y_obs[i, angle] = obs[i, angle] * np.sin(angle)
                
                """
                Probably I need to define if there is any obstacle
                with following piece of code: 
                
                x_check = distance * math.cos(math.radians(angle))
                y_check = distance * math.sin(math.radians(angle))
                check_line = [x_check][y_check]
                
                # define check_line and obstacles!
                
                point = check_line.intersection(obstacle)
                """
            
            x[:,i] = np.mean(x_obs[:,i])
            y[:,i] = np.mean(y_obs[:,i])
        
        """
        Process coordinates and send them to the map
        """
        return (x, y)
    
    def plot(self, cartesian, init_data): 
        """
        NOTE: 
        - This method displays coordinates of obstacles awful, 
        - Add animation. 
        """
        
        borders = init_data[0]
        auto = init_data[4]
        
        fig = plt.figure()
        
        # real map 
        realmap = fig.add_subplot(121)
        realmap.plot(auto[0], auto[1],'bo', label='auto')
        realmap.plot(borders[:,0], borders[:,1], 'go')
        plt.xlabel('Position X (meters)')
        plt.ylabel('Position Y (meters)')
        plt.title('Real map' , fontweight='bold')
        plt.grid()
        plt.legend()
        
        # estimate map 
        estimatemap = fig.add_subplot(122)
        estimatemap.plot(auto[0], auto[1],'bo', label='auto')
        estimatemap.plot(cartesian[0], cartesian[1], 'go')
        plt.xlabel('Position X (meters)')
        plt.ylabel('Position Y (meters)')
        plt.title('Estimate map' , fontweight='bold')
        plt.grid()
        plt.legend()
        
        plt.show()
