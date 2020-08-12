"""
Test for Kalman filter accelerometer. 

Here we should define uniform and non-uniform acceleration classes, 
then methods of these classes should be invoke in moving_car. 

Non-uniform acceleration can be defined by some law and depending on 
real-time observations. 

I guess that acceleration class can inherit some properties and methods 
from velocity class. 
Because in order to process non-uniform motion, we need to combine both
velocity and acceleration models.
"""

import kf_accelerometer
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

class Accelerartion():
    def initialize(self):
        # input initial data 
        print('INITIAL DATA')
        
        """
        init_pos = float(input('Truth value: '))
        init_guess = float(input('Initial guess: '))
        init_velocity = float(input('Velocity (m/s): '))
        frequency = float(input('Frequency (Hz): '))
        n_iter = int(input('Total number of iterations: ')) + 1
        """
        
        # mock initial data 
        init_pos = 45.0
        init_guess = 55.0
        init_velocity = 2.0
        frequency = 50.0 * 10**3
        n_iter = 21
        
        # print out dummy data
        print(f'Truth value: {init_pos}')
        print(f'Initial guess: {init_guess}')
        print(f'Velocity (m/s): {init_velocity}')
        print(f'Frequency (Hz): {frequency}')
        print(f'Total number of iterations: {n_iter}')
        
        # time delay of accelerometer between measurements
        dt = 1 / frequency
        rows = int(n_iter / dt)
        
        # randomly generate values of acceleration
        #accel = np.ones((rows, 1))
        accel = np.random.random_sample((rows,))
        
        # velocity is going to be an array of array_size shape
        velocity = np.ones((rows, 1))
        velocity[0] = init_velocity
        
        # allocate space for truth_value
        truth_value = np.ones((n_iter, 1))
        truth_value[0] = init_pos
        
        # determine velocity (and truth_value)
        for i in range(1, rows): 
            velocity[i] = velocity[i - 1] + accel[i - 1] * dt
        
        """
        Number of elements in velocity and truth_value arrays differs.
        And bacause of that truth_value depends on velocity and accel, 
        we need to process velocity and accel data.
        
        So every (n_iter*dt)th element of velocity and accel should be 
        consider, but in raality you should process all  accelerometer 
        data and select median or mean of this dataset in some range. 
        """
        
        # process all accelerometer data
        # google how to process accelerometer data!
        proc_velocity = velocity[int(i/dt)]
        proc_accel = accel[int(i/dt)]
        
        # initialize truth_value dataset
        for i in range(1, n_iter): 
            truth_value[i] = truth_value[i-1] + proc_velocity[i-1] + proc_accel[i-1]/2
        
        return truth_value, init_guess, n_iter
    
    
    def initdata_2d(self):
        """
        # input initial data
        print('INPUT INITIAL DATA')
        truth_value_X = float(input('Truth value X: '))
        truth_value_Y = float(input('Truth value Y: '))
        init_guess_X = float(input('Initial guess X: '))
        init_guess_Y = float(input('Initial guess Y: '))
        velocity = float(input('Velocity (m/s): '))
        n_iter = int(input('Number of iterations: '))
        
        # convert initial data into arrays 
        truth_value = (truth_value_X, truth_value_Y)
        init_guess = (init_guess_X, init_guess_Y)
        """
        
        # mock initial data 
        init_pos = (163.0, 55.0)
        init_guess = (152.0, 68.0)
        init_velocity = 2.0
        frequency = 2.0
        n_iter = 61
        
        # print out dummy data
        print('INITIAL DATA:')
        print(f'Truth value: {init_pos}')
        print(f'Initial guess: {init_guess}')
        print(f'Velocity (m/s): {init_velocity}')
        print(f'Frequency (Hz): {frequency}')
        print(f'Total number of iterations: {n_iter}')
        
        # time delay of accelerometer between measurements
        dt = 1 / frequency
        rows = int(n_iter / dt)
        
        # randomly generate values of acceleration
        #accel = np.ones((rows, 1))
        accel = np.random.random_sample((rows, len(init_pos)))
        #print(f'acceleration: \n{accel}'.upper())
        
        # velocity is going to be an array of array_size shape
        velocity = np.ones((rows, len(init_pos)))
        velocity[0] = init_velocity
        
        # allocate space for truth_value
        truth_value = np.ones((n_iter, len(init_pos)))
        truth_value[0] = init_pos
        
        # determine velocity (and truth_value)
        for i in range(1, rows): 
            velocity[i] = velocity[i - 1] + accel[i - 1] * dt
        
        """
        Number of elements in velocity and truth_value arrays differs.
        And bacause of that truth_value depends on velocity and accel, 
        we need to process velocity and accel data.
        So every (n_iter*dt)th element of velocity and accel should be consider. 
        """
        for i in range(1, n_iter): 
            truth_value[i] = truth_value[i-1] + velocity[int(i/dt)] + accel[int(i/dt)]/2
        
        return truth_value, init_guess, n_iter


    def print_out(self, obs, est, kf):
        # reshape for a table (for 1D)
        if type(kf.truth_value) is float:
            obs = obs.reshape((len(obs), 1))
            est = est.reshape((len(est), 1))
        
        # round values for printing out a table
        truth_value = np.round(kf.truth_value, 3)
        obs = np.round(obs, 3)
        est = np.round(est, 3)

        # making a table
        # add accel and velocity to the table! 
        list_for_table = [[truth_value, est, obs]]
        headers_table = ['Truth value', 'Estimations', 'Observations']
        print('\nDATA PROCESSING:')
        print(tabulate(list_for_table, headers=headers_table))
        
        
        # PRINTING OUT DATA INTO DATABASE OR EXCEL FILE
        


    # PLOT METHOD FOR 1D SPACE
    def plot_1d(self, obs, est, kf):
        # plot estimations 
        plt.figure()
        plt.plot(obs,'k+', label='noisy measurements')
        plt.plot(est,'b-', label='a posteri estimate')
        plt.plot(kf.truth_value, color='g', label='truth value')
        plt.legend()
        plt.title('Estimate vs. iteration step', fontweight='bold')
        plt.xlabel('Iteration')
        plt.ylabel('Position (meters)')
        plt.grid()
        plt.show()


    # PLOT METHOD FOR 2D SPACE
    """
    1) 2 diagrams of Estimation vs Data with respect to each axis, 
    2) one diagram which contains both data and predictions with 
    respect to each axis
    """
    def plot_2d(self, obs, est, kf):
        # map 
        fig = plt.figure()
        mapping = fig.add_subplot(121)
        mapping.plot(obs[:,0], obs[:,1],'k+', label='noisy measurements')
        mapping.plot(est[:,0], est[:,1],'bo', label='a posteri estimate')
        mapping.plot(kf.truth_value[:,0], kf.truth_value[:,1], 'g', label='truth value')
        plt.xlabel('Position X (meters)')
        plt.ylabel('Position Y (meters)')
        plt.title('Map' , fontweight='bold')
        plt.grid()
        plt.legend()
        
        # diagram with respect to X
        pos_X = fig.add_subplot(222)
        pos_X.plot(obs[:,0],'k+', label='noisy measurements')
        pos_X.plot(est[:,0],'b-', label='a posteri estimate')
        pos_X.plot(kf.truth_value[:,0], color='g', label='truth value')
        plt.legend()
        plt.title('Estimate vs. iteration step', fontweight='bold')
        plt.ylabel('Position X (meters)')
        plt.grid()
        
        # diagram with respect to Y
        pos_Y = fig.add_subplot(224)
        pos_Y.plot(obs[:,1],'k+', label='noisy measurements')
        pos_Y.plot(est[:,1],'b-', label='a posteri estimate')
        pos_Y.plot(kf.truth_value[:,1], color='g', label='truth value')
        plt.legend()
        plt.xlabel('Iteration')
        plt.ylabel('Position Y (meters)')
        plt.grid()
        
        # plot all
        plt.show()


class UniformAccel(Accelerartion):
    pass 


class NonUniformAccel(Accelerartion):
    pass 


def main():
    
    # CALL KALMAN FILTER FOR 1D SPACE
    # input initial data
    kftest_1d = Accelerartion()
    
    # get initial data and initialize an instance of KalmanFilter 
    truth_value, init_guess, n_iter = kftest_1d.initdata_1d()
    kf_1d = kf_accelerometer.KalmanFilter(truth_value, init_guess, n_iter)

    # estimate, print out results and plot all 
    obs, est = kf_1d.estimate()
    kftest_1d.print_out(obs, est, kf_1d)
    kftest_1d.plot_1d(obs, est, kf_1d)
    
    
    # CALL KALMAN FILTER FOR 2D SPACE
    # initialize an instance of Accelerartion
    kftest_2d = Accelerartion()
    
    # get initial data and initialize an instance of KalmanFilter 
    truth_value, init_guess, n_iter = kftest_2d.initdata_2d()
    kf_2d = kf_accelerometer.KalmanFilter(truth_value, init_guess, n_iter)
    
    # estimate, print out results and plot all 
    obs, est = kf_2d.estimate()
    kftest_2d.print_out(obs, est, kf_2d)
    kftest_2d.plot_2d(obs, est, kf_2d)


if __name__ == '__main__':
    main()
    