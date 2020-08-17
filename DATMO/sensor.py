"""
In this file we can determine a class of sensors which contain all of 
attributes and methods of any sensor (such as radar, lidar etc).

Notice that class Sensor inherit from class Intersection because all 
sensors like lidar and radar always find point of intersection with 
obstacles.
"""

from intersection import Intersection
import numpy as np
import math
import matplotlib.pyplot as plt


class Sensor: 
    def measure(self, init_data): 
        env = init_data[0]
        accuracy = init_data[1]
        max_degree = init_data[2]
        frequency = init_data[3]
        distance = init_data[4]
        auto = init_data[5]
        
        sigma = accuracy / 2
        
        # allocate space to the observations arrays
        obs = np.ones((frequency, max_degree))
        x_obs = np.ones((frequency, max_degree))
        y_obs = np.ones((frequency, max_degree))
        x = np.ones((1, max_degree))
        y = np.ones((1, max_degree))
        
        for i in range(frequency):
            for degree in range(max_degree): 
                """
                1) Get coordinates of obtacles in polar coordinate system, 
                2) Transform these coordinates into Cartesian coordinate system. 
                """
                #obs[i, degree] = np.random.normal(env, sigma, size=(1,1))
                
                """
                Probably I need to define if there is any obstacle
                with following piece of code: 
                """
                
                x_check = distance * math.cos(math.radians(degree)) + auto[0]
                y_check = distance * math.sin(math.radians(degree)) + auto[1]
                check_line = np.array([auto, [x_check, y_check]])
                
                # define two points of obstacles array!
                self.simple_line(env, check_line)
            
            # plot observations
            
            x[:,i] = np.mean(x_obs[:,i])
            y[:,i] = np.mean(y_obs[:,i])
        
        """
        Process coordinates and send them to the map
        """
        return (x, y)
    
    
    def simple_line(self, env, check_line): 
        """
        Return two points that define one segment of an obstacle
        """
        
        for multiline in env: 
            length = len(multiline[:,0])
            dim = len(multiline[0,:])
            
            points = np.ones((length-1, dim))
            
            for i in range(1, length):
                start = multiline[i-1]
                end = multiline[i]
                line = np.array([start, end])

                points[i-1] = Intersection.line_intersection(check_line, line)
            
            print(f'points: \n{points}')
    
    
    def plot(self, init_data): 
        """
        NOTE: 
        - Add animation. 
        """
        
        # unpack init_data
        env = init_data[0]
        auto = init_data[5]
        upper_line, lower_line = env[0], env[1]
        
        fig = plt.figure()
        
        realmap = fig.add_subplot(121)
        realmap.plot(upper_line[:,0], upper_line[:,1], 'k-', label='borders')
        realmap.plot(lower_line[:,0], lower_line[:,1], 'k-')
        realmap.plot(auto[0], auto[1], 'bo', label='auto')
        plt.xlabel('Position X (meters)')
        plt.ylabel('Position Y (meters)')
        plt.title('Real map' , fontweight='bold')
        plt.grid()
        
        """
        estimatemap = fig.add_subplot(122)
        estimatemap.plot(upper_line[:,0], upper_line[:,1], 'k-', label='borders')
        estimatemap.plot(lower_line[:,0], lower_line[:,1], 'k-')
        estimatemap.plot(auto[0], auto[1], 'bo', label='auto')
        plt.xlabel('Position X (meters)')
        plt.ylabel('Position Y (meters)')
        plt.title('Map of observations' , fontweight='bold')
        plt.grid()
        """
        """
        x = []
        y = []
        
        index = count()
        
        ani = FuncAnimation(plt.gcf(), self.animate, interval=1000)
        """
        
        plt.legend()
        plt.show()
    
    
    def animate(i):
        x.append(next(index))
        y.append(random.randint(0, 5))
        
        plt.cla()
        plt.plot(x, y)
