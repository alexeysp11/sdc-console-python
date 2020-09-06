"""
Here I can implement both constant and different velocity.
Also here I can implement kf for non-moving car by passing velocity that is 
equal to zero.
"""

import acceleration 
import numpy as np


class Velocity: 
    def initialize(dimension=1, init_velocity=0.0, mode='p', accel=False, mock=True):
        if dimension == 1: 
            if mock == True:
                init_pos = 45.0
                init_guess = 55.0
                velocity = init_velocity
                time_sec = 50

                print(f'Truth value: {init_pos}')
                print(f'Initial guess: {init_guess}')
                print(f'Velocity (m/s): {velocity}')
                print(f'Time (sec): {time_sec}')
            
            else:
                print('Initial data'.upper())
                init_pos = float(input('Truth value: '))
                init_guess = float(input('Initial guess: '))
                
                if mode != 'p':
                    velocity = float(input('Velocity (m/s): '))
                else: 
                    velocity = 0.0
                    print(f'Velocity (m/s): {velocity}')
                
                time_sec = int(input('Time (sec): ')) + 1
            
            truth_value = Velocity.count_position(init_pos, velocity, accel, time_sec)
        
        if dimension == 2: 
            if mock == True:
                init_pos = (163.0, 55.0)
                init_guess = (152.0, 68.0)
                velocity = init_velocity
                time_sec = 60

                print(f'Real coordinates[0]: {init_pos}')
                print(f'Initial coordinates: {init_guess}')
                print(f'Velocity: {velocity} m/s')
                print(f'Time (sec): {time_sec}')
            
            else:
                print('Initial data'.upper())
                truth_value_X = float(input('Truth value X: '))
                truth_value_Y = float(input('Truth value Y: '))
                init_guess_X = float(input('Initial guess X: '))
                init_guess_Y = float(input('Initial guess Y: '))
                
                if mode != 'p':
                    velocity = float(input('Velocity (m/s): '))
                else: 
                    velocity = 0.0
                    print(f'Velocity (m/s): {velocity}')
                
                time_sec = int(input('Time (sec): '))
                
                # convert initial data into arrays 
                init_pos = (truth_value_X, truth_value_Y)
                init_guess = (init_guess_X, init_guess_Y)
            
            truth_value = Velocity.count_position(init_pos, velocity, accel, time_sec)
        
        return (truth_value, init_guess, time_sec)
    
    
    def count_position(init_pos, velocity, accel, time_sec):
        if type(init_pos) == float:
            # allocate space for truth_value
            size = (time_sec, 1)
            truth_value = np.ones(size)
            truth_value[0] = init_pos
        else:
            # allocate space for truth_value
            size = (time_sec, len(init_pos))
            truth_value = np.ones(size)
            truth_value[0, 0] = init_pos[0]
            truth_value[0, 1] = init_pos[1]
        
        """
        acceleration.define_accel takes accel as a bool variable 
        but returns it as an array of floats.
        """
        accel = acceleration.define_accel(size, accel)
        
        # determine truth_value
        for sec in range(1, time_sec): 
            # redefine current velocity in 1D with following formula: v = at
            velocity = DifferentVelocity.redefine_velocity(velocity, accel[sec], sec)
            
            # get current position
            if type(init_pos) == float:
                # if 1D
                truth_value[sec] = truth_value[sec-1] + velocity + accel[sec] / 2
            else:
                # if 2D
                truth_value[sec, 0] = truth_value[0, 0] + velocity * sec
                truth_value[sec, 1] = truth_value[0, 1] + velocity * sec
        
        return truth_value


class DifferentVelocity(Velocity): 
    def redefine_velocity(init_velocity, accel, time):
        if accel == type(float):
            # if 1D
            velocity = init_velocity + accel 
        else: 
            # if 2D
            velocity[0] = init_velocity + accel[0] 
            velocity[1] = init_velocity + accel[1] 
        
        return velocity
