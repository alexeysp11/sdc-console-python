"""
In this file we can determine a class of sensors which contain all of 
attributes and methods of any sensor (such as radar, lidar etc).

Notice that class Sensor inherit from class Intersection because all 
sensors like lidar and radar always find point of intersection with 
obstacles.
"""

import numpy as np
import math
import matplotlib.pyplot as plt


class Intersection: 
    def slope(self, P1, P2):
        # dy/dx
        # (y2 - y1) / (x2 - x1)
        slope = (P2[1] - P1[1]) / (P2[0] - P1[0])
        
        return slope


    def y_intercept(self, P1, slope):
        # y = mx + b
        # b = y - mx
        # b = P1[1] - slope * P1[0]
        return P1[1] - slope * P1[0]


    def line_intersect(self, m1, b1, m2, b2):
        if m1 == m2:
            return None
        # y = mx + b
        # Set both lines equal to find the intersection point in the x direction
        # m1 * x + b1 = m2 * x + b2
        # m1 * x - m2 * x = b2 - b1
        # x * (m1 - m2) = b2 - b1
        # x = (b2 - b1) / (m1 - m2)
        x = (b2 - b1) / (m1 - m2)
        # Now solve for y -- use either line, because they are equal here
        # y = mx + b
        y = m1 * x + b1
        return [x, y]
    
    
    def find_intersection(self, auto, check_line, env_line):
        """
        Take coordinates of lines and find lines intersection point,
        then check if it is in intervals:
        I1 = [min(X1,X2), max(X1,X2)]
        I2 = [min(X3,X4), max(X3,X4)]
        """
        
        A1 = auto
        A2 = check_line
        B1 = env_line[0]
        B2 = env_line[1]
        
        print(f'A1 = {A1}, A2 = {A2}, B1 = {B1}, B2 = {B2}')
        
        """
        Slope: (y2 - y1) / (x2 - x1).
        If x2 - x1 = 0, then equation: x = b
        """
        
        slope_A = self.slope(A1, A2)
        slope_B = self.slope(B1, B2)
        y_int_A = self.y_intercept(A1, slope_A)
        y_int_B = self.y_intercept(B1, slope_B)
        point = self.line_intersect(slope_A, y_int_A, slope_B, y_int_B)
        
        print(f'point: {point}')
        
        """
        Check if point of intersection is in interval.
        """
        
        return point


class Sensor(Intersection): 
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
                check_line = [x_check, y_check]
                
                # define two points of obstacles array!
                self.simple_line(env, auto, check_line)
            
            # plot observations
            
            x[:,i] = np.mean(x_obs[:,i])
            y[:,i] = np.mean(y_obs[:,i])
        
        """
        Process coordinates and send them to the map
        """
        return (x, y)
    
    
    def simple_line(self, env, auto, check_line): 
        """
        Return two points that define one segment of an obstacle
        """
        
        for multiline in env: 
            length = len(multiline[:,0])
            dim = len(multiline[0,:])
            print(length)
            
            points = np.ones((length-1, dim))
            
            for i in range(1, length):
                start = multiline[i-1]
                end = multiline[i]
                line = [start, end]

                points[i] = self.find_intersection(auto, check_line, line)
    
    def plot(self, init_data): 
        """
        NOTE: 
        - This method displays coordinates of obstacles awful, 
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
        
        x = []
        y = []
        
        index = count()
        
        ani = FuncAnimation(plt.gcf(), self.animate, interval=1000)
        
        plt.legend()
        plt.show()
    
    
    def animate(i):
        x.append(next(index))
        y.append(random.randint(0, 5))
        
        plt.cla()
        plt.plot(x, y)
