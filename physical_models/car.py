import numpy as np
import random

class Car: 
    def initialize(self, dimension=1, init_velocity=0.0, mode='p', 
        is_accel=False, is_mock=True):
        """
        Initializes state of a car (position, velocity, acceleration) and initial
        guesses about where a car is located. 
        Then this method prints it all in the console. 

        Returns: 

        `(truth_value, init_guess, time_sec)`
        """

        if dimension == 1: 
            # if we use default values
            if is_mock == True:
                init_pos = 45.0
                init_guess = 55.0
                velocity = init_velocity
                time_sec = 50

                print(f'Truth value: {init_pos}')
                print(f'Initial guess: {init_guess}')
                print(f'Velocity (m/s): {velocity}')
                print(f'Time (sec): {time_sec}')
            
            # if we enter our own values
            else:
                print('Initial data'.upper())
                
                # input truth value
                while (True):
                    try:
                        init_pos = float(input('Truth value: '))
                        if type(init_pos) == float: 
                            break
                    except Exception as e:
                        print('Exception: '.upper(), e)
                
                # input initial guess
                while (True):
                    try:
                        init_guess = float(input('Initial guess: '))
                        if type(init_guess) == float: 
                            break
                    except Exception as e:
                        print('Exception: '.upper(), e)
                
                # if the car doesn't stay (e.g. it moves)
                if mode != 'p':
                    # input velocity
                    while (True):
                        try:
                            velocity = float(input('Velocity (m/s): '))
                            if type(velocity) == float: 
                                break
                        except Exception as e:
                            print('Exception: '.upper(), e)
                
                # if the car stays (e.g. it doesn't moves)
                else: 
                    velocity = 0.0
                    print(f'Velocity (m/s): {velocity}')
                
                # input time initerval
                while (True):
                    try:
                        time_sec = int(input('Time (sec): ')) + 1
                        if type(time_sec) == int: 
                            break
                    except Exception as e:
                        print('Exception: '.upper(), e)

            truth_value = self.count_position(init_pos, velocity, is_accel, time_sec)
        
        if dimension == 2: 
            # if we use default values
            if is_mock == True:
                init_pos = (163.0, 55.0)
                init_guess = (152.0, 68.0)
                velocity = init_velocity
                time_sec = 60

                print(f'Real coordinates (at the beginning): {init_pos}')
                print(f'Initial coordinates: {init_guess}')
                print(f'Velocity_x: {velocity[0]} m/s')
                print(f'Velocity_y: {velocity[1]} m/s')
                print(f'Time (sec): {time_sec}')
            
            # if we enter our own values
            else:
                print('Initial data'.upper())

                # input truth value with respect to X axis
                while (True):
                    try:
                        truth_value_X = float(input('Truth value X: '))
                        if type(truth_value_X) == float: 
                            break
                    except Exception as e:
                        print('Exception: '.upper(), e)
                
                # input truth value with respect to Y axis
                while (True):
                    try:
                        truth_value_Y = float(input('Truth value Y: '))
                        if type(truth_value_Y) == float: 
                            break
                    except Exception as e:
                        print('Exception: '.upper(), e)
                
                # input init guess with respect to X axis
                while (True):
                    try:
                        init_guess_X = float(input('Initial guess X: '))
                        if type(init_guess_X) == float: 
                            break
                    except Exception as e:
                        print('Exception: '.upper(), e)
                
                # input init guess with respect to Y axis
                while (True):
                    try:
                        init_guess_Y = float(input('Initial guess Y: '))
                        if type(init_guess_Y) == float: 
                            break
                    except Exception as e:
                        print('Exception: '.upper(), e)
                
                velocity = [0.0, 0.0]
                
                # if the car doesn't stay (e.g. it moves)
                if mode != 'p':
                    # input velocity with respect to X axis
                    while (True):
                        try:
                            velocity[0] = float(input('Velocity X (m/s): '))
                            if type(velocity[0]) == float: 
                                break
                        except Exception as e:
                            print('Exception: '.upper(), e)
                    
                    # input velocity with respect to Y axis
                    while (True):
                        try:
                            velocity[1] = float(input('Velocity Y (m/s): '))
                            if type(velocity[1]) == float: 
                                break
                        except Exception as e:
                            print('Exception: '.upper(), e)

                # if the car stays (e.g. it doesn't moves), 
                # then its velovity should be equal zero
                else: 
                    print(f'Velocity (m/s): {velocity}')
                
                # input time initerval
                while (True):
                    try:
                        time_sec = int(input('Time (sec): '))
                        if type(time_sec) == int: 
                            break
                    except Exception as e:
                        print('Exception: '.upper(), e)

                # convert initial data into arrays 
                init_pos = (truth_value_X, truth_value_Y)
                init_guess = (init_guess_X, init_guess_Y)
            
            truth_value = self.count_position(init_pos, velocity, is_accel, time_sec)
        
        return (truth_value, init_guess, time_sec)


    def default_velocity(self, mode, dim): 
        """
        Set default configurations of car's velocity.

        Takes `mode` as an input parameter that indicates car's motion pattern
        (for example, constant position `p`, constant speed `v` or random 
        acceleration `a`). 

        Takes `dim` as an input parameter that indicates dimension (1D or 2D). 

        Returns: 
        
        `velocity` : current velocity of a car. 
        
        `is_accel` : is random acceleration enabled (is `True` only when `mode == 'a'`). 
        """

        if mode == 'p':
            if dim == 1:
                velocity = 0.0
            else:
                velocity = [0.0, 0.0]
            is_accel = False
        
        elif mode == 'v':
            if dim == 1:
                velocity = 2.0
            else:
                velocity = [2.0, 1.5]
            is_accel = False
        
        elif mode == 'a':
            if dim == 1:
                velocity = 2.5
            else: 
                velocity = [2.5, 4.5]
            is_accel = True

        return velocity, is_accel

    
    def count_position(self, init_pos, velocity, is_accel, time_sec):
        """
        Calculates truth position of a car. 

        Takes initial position `init_pos` (position at 0th second), 
        an array of truth velocity `velocity`, boolean variabe `is_accel`
        that indicates if a car can randomly change its speed (by addition 
        gaussian noise to acceleration array) and time of execution `time_sec` 
        as input parameters.
        """

        dt = 1

        if type(init_pos) == float:
            size = (time_sec, 1)                # allocate space for truth_value
            truth_value = np.ones(size)
            truth_value[0] = init_pos
        else:
            size = (time_sec, len(init_pos))    # allocate space for truth_value
            truth_value = np.ones(size)
            truth_value[0, 0] = init_pos[0]
            truth_value[0, 1] = init_pos[1]
        
        # assign acceleration array. 
        accel = self.define_accel(size, is_accel)

        # determine truth_value (truth position). 
        for sec in range(1, time_sec): 
            # redefine current velocity with following formula: v = at. 
            velocity = self.redefine_velocity(velocity, accel[sec], sec)
            
            # get current position
            if type(init_pos) == float:     # if 1D. 
                truth_value[sec] = truth_value[sec-1] + (velocity * dt) + (accel[sec] * dt**2) / 2
            else:                           # if 2D. 
                truth_value[sec, 0] = truth_value[sec-1, 0] + (velocity[0] * dt) + (accel[sec, 0] * dt**2) / 2
                truth_value[sec, 1] = truth_value[sec-1, 1] + (velocity[1] * dt) + (accel[sec, 1] * dt**2) / 2
        
        return truth_value


    def define_accel(self, size, is_rand): 
        """
        Assign an array of accelerations as random values from -1 to 1. 
        """

        start = -1
        stop = 1
        time_sec = size[0]
        
        if is_rand == True:
            accel = np.zeros(size)
            for i in range(time_sec):
                if size[1] == 1:
                    # if 1D
                    accel[i] = random.uniform(start, stop)
                else:
                    #if 2D
                    accel[i, 0] = random.uniform(start, stop)
                    accel[i, 1] = random.uniform(start, stop)
        else: 
            accel = np.zeros(size)
        
        return accel


    def redefine_velocity(self, init_velocity, accel, time):
        dt = 1
        if len(accel) == 1:
            # if 1D
            velocity = init_velocity + accel * dt
        else:
            # if 2D
            velocity = [0.0, 0.0]
            velocity[0] = init_velocity[0] + accel[0] * dt
            velocity[1] = init_velocity[1] + accel[1] * dt
        return velocity