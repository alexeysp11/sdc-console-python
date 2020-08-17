"""
Here I can implement both constant and different velocity.
Also here I can implement kf for non-moving car by passing velocity that is 
equal to zero.
"""

import acceleration 
import numpy as np

class Velocity: 
    pass


class ConstantVelocity(Velocity): 
    def __init__(self):
        pass
    
    
    def initialize(dimension=1, accel=False, mock=True, display=True):
        if dimension == 1: 
            if mock == True:
                # mock initial data 
                init_pos = 45.0
                init_guess = 55.0
                velocity = 2.0
                time_sec = 51
            else:
                # input initial data 
                print('INITIAL DATA')
                init_pos = float(input('Truth value: '))
                init_guess = float(input('Initial guess: '))
                velocity = float(input('Velocity (m/s): '))
                time_sec = int(input('Time (sec): ')) + 1
            
            if display == True:
                # print out dummy data
                print(f'Truth value: {init_pos}')
                print(f'Initial guess: {init_guess}')
                print(f'Velocity (m/s): {velocity}')
                print(f'Time (sec): {time_sec}')
            
            truth_value = ConstantVelocity.count_position(init_pos, velocity, accel, time_sec)
            
            return (truth_value, init_guess, time_sec)
        
        if dimension == 2: 
            if mock == True:
                # mock initial data
                init_pos = (163.0, 55.0)
                init_guess = (152.0, 68.0)
                velocity = 2.0
                time_sec = 60
            else:
                # input initial data
                print('INPUT INITIAL DATA')
                truth_value_X = float(input('Truth value X: '))
                truth_value_Y = float(input('Truth value Y: '))
                init_guess_X = float(input('Initial guess X: '))
                init_guess_Y = float(input('Initial guess Y: '))
                velocity = float(input('Velocity (m/s): '))
                time_sec = int(input('Time (sec): '))
                
                # convert initial data into arrays 
                truth_value = (truth_value_X, truth_value_Y)
                init_guess = (init_guess_X, init_guess_Y)
            
            if display == True:
                # print out initial data 
                print('INITIAL DATA:')
                print(f'Real coordinates[0]: {init_pos}')
                print(f'Initial coordinates: {init_guess}')
                print(f'Velocity: {velocity} m/s')
                print(f'Time (sec): {time_sec}')
            
            # allocate space for truth_value
            size = (time_sec, len(init_pos))
            truth_value = np.ones(size)
            truth_value[0, 0], truth_value[0, 1] = init_pos[0], init_pos[1]
            
            # determine truth_value as an array 
            for sec in range(1, time_sec): 
                truth_value[sec, 0] = truth_value[0, 0] + velocity * sec
                truth_value[sec, 1] = truth_value[0, 1] + velocity * sec
            
            return (truth_value, init_guess, time_sec)
    
    
    def count_position(init_pos, velocity, accel, time_sec):
        # allocate space for truth_value
        size = (time_sec, 1)
        truth_value = np.ones(size)
        truth_value[0] = init_pos
        
        accel = acceleration.define_accel(size, accel)
        
        """
        if acceleration is not equal to zero, then we need to redefine 
        velocity because now it is not constant. 
        
        Formula: v = at
        """
        
        # determine truth_value
        for sec in range(1, time_sec): 
            velocity = DifferentVelocity.redefine_velocity(velocity, accel[sec], sec)
            truth_value[sec] = truth_value[sec-1] + velocity + accel[sec] / 2
        
        return truth_value


class DifferentVelocity(Velocity): 
    def redefine_velocity(init_velocity, accel, time):
        velocity = init_velocity + accel * time
        return velocity
