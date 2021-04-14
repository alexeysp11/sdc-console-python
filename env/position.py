# Test Kalman filter for non-moving car in 1D and 2D pace. 

"""

FIX THAT: 
- Use callkf functions to reduce in main function (function 
get_initial_data should be defined for 1d and 3d space as well), 
- Use shorter names of methods of PositionKF and names of 
variables because too long names with a lot of underscores seem ugly 
and annoying (truth_value in plotting method), 
- I need some inheritance for plot methods because some pieces of 
code are repeated a lot, 
- Can an error of observations with respect to z axis be about 50 
meters?. 
"""

from models.kf_position import KalmanFilter as kf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tabulate import tabulate


class PositionKF():
    # CALL KALMAN FILTER FOR 1D SPACE 
    def callkf_1d():
        pass
    
    
    # CALL KALMAN FILTER FOR 2D SPACE
    def callkf_2d():
        pass 
    
    
    # CALL KALMAN FILTER FOR 3D SPACE
    def callkf_3d():
        pass 
    
    
    # GET INITIAL DATA (only for 2D)
    def init2d(self):
        """
        Allows to initialize parameters for 2D motion. 
        """
        
        """
        # input initial data
        print('INPUT INITIAL DATA')
        truth_value_X = float(input('Truth value X: '))
        truth_value_Y = float(input('Truth value Y: '))
        init_guess_X = float(input('Initial guess X: '))
        init_guess_Y = float(input('Initial guess Y: '))
        n_iter = int(input('Number of iterations: '))
        
        # convert initial data into arrays 
        truth_value = (truth_value_X, truth_value_Y)
        init_guess = (init_guess_X, init_guess_Y)
        """
        
        # mock initial data
        truth_value, init_guess, n_iter = (63.0, 55.0), (52.0, 68.0), 20
        
        # print out initial data 
        print('INITIAL DATA:')
        print(f'Real coordinates: {truth_value}')
        print(f'Initial coordinates: {init_guess}')
        print(f'Number of iterations: {n_iter}')
        
        return truth_value, init_guess, n_iter


    # GET INITIAL DATA (only for 3D)
    def init3d(self):
        """
        # input initial data
        print('INPUT INITIAL DATA')
        truth_value_X = float(input('Truth value X: '))
        truth_value_Y = float(input('Truth value Y: '))
        init_guess_X = float(input('Initial guess X: '))
        init_guess_Y = float(input('Initial guess Y: '))
        n_iter = int(input('Number of iterations: '))
        
        # convert initial data into arrays 
        truth_value = (truth_value_X, truth_value_Y)
        init_guess = (init_guess_X, init_guess_Y)
        """
        
        # mock initial data
        truth_value, init_guess, n_iter = (63.0, 55.0, 34.0), (52.0, 68.0, 43), 20
        
        # print out initial data 
        print('INITIAL DATA:')
        print(f'Real coordinates: {truth_value}')
        print(f'Initial coordinates: {init_guess}')
        print(f'Number of iterations: {n_iter}')
        
        return truth_value, init_guess, n_iter


    # PRINT OUT ALL DATA 
    def print_out(self, obs, est, kf):
        # reshape for a table (for 1D)
        if type(kf.truth_value) is float:
            obs = obs.reshape((len(obs), 1))
            est = est.reshape((len(est), 1))
        
        # round values for printing out a table!
        obs, est = np.round(obs, 3), np.round(est, 3)

        # making a table
        data = [[obs, est]]
        headers = ['Observations', 'Estimations']
        print('\nDATA PROCESSING:')
        print(tabulate(data, headers=headers))


    # PLOT METHOD FOR 1D SPACE
    def plot1d(self, obs, est, kf):
        # plot estimations 
        plt.figure()
        plt.plot(obs,'k+', label='noisy measurements')
        plt.plot(est,'b-', label='a posteri estimate')
        plt.axhline(kf.truth_value, color='g', label='truth value')
        plt.legend()
        plt.title('Estimate vs. iteration step', fontweight='bold')
        plt.xlabel('Iteration')
        plt.ylabel('Position (meters)')
        plt.show()


    # PLOT METHOD FOR 2D SPACE
    """
    1) 2 diagrams of Estimation vs Data with respect to each axis, 
    2) one diagram which contains both data and predictions with respect to each axis
    """
    def plot2d(self, obs, est, kf):
        # map 
        fig = plt.figure()
        mapping = fig.add_subplot(121)
        mapping.plot(obs[:,0], obs[:,1],'k+', label='noisy measurements')
        mapping.plot(est[:,0], est[:,1],'bo', label='a posteri estimate')
        mapping.plot(kf.truth_value[0], kf.truth_value[1], 'go', label='truth value')
        plt.xlabel('Position X (meters)')
        plt.ylabel('Position Y (meters)')
        plt.title('Map' , fontweight='bold')
        plt.grid()
        plt.legend()
        
        # diagram with respect to X
        pos_X = fig.add_subplot(222)
        pos_X.plot(obs[:,0],'k+', label='noisy measurements')
        pos_X.plot(est[:,0],'b-', label='a posteri estimate')
        pos_X.axhline(kf.truth_value[0], color='g', label='truth value')
        plt.legend()
        plt.title('Estimate vs. iteration step', fontweight='bold')
        plt.ylabel('Position X (meters)')
        plt.grid()
        
        # diagram with respect to Y
        pos_Y = fig.add_subplot(224)
        pos_Y.plot(obs[:,1],'k+', label='noisy measurements')
        pos_Y.plot(est[:,1],'b-', label='a posteri estimate')
        pos_Y.axhline(kf.truth_value[1], color='g', label='truth value')
        plt.legend()
        plt.xlabel('Iteration')
        plt.ylabel('Position Y (meters)')
        plt.grid()
        
        # plot all
        plt.show()


    """
    How can I represent final result of kf data processing in 3d space? 
    1) I can show 2 windows: the first one represents all data with respect to each of 3 axis, and 
    the second one represents 2 graphs (a map in 2d space and the car's trajectory in 3d space), 
    2) I can try to make it in one window. 
    """
    # PLOT METHOD FOR 3D SPACE
    # indexes, plot 3D and show legends correctly!
    def plot3d(self, obs, est, kf):
        # initialize an array of truth_value 2x2 because I had problems with plotting tuple in 3D
        rows = len(kf.truth_value)
        truth_value = np.ones((1, rows))
        for i in range(rows):
            truth_value[0,i] = kf.truth_value[i]
        
        # map XY
        fig = plt.figure()
        mapping = fig.add_subplot(221)
        mapping.plot(obs[:,0], obs[:,1],'k+', label='noisy measurements')
        mapping.plot(est[:,0], est[:,1],'bo', label='a posteri estimate')
        mapping.plot(kf.truth_value[0], kf.truth_value[1], 'go', label='truth value')
        plt.xlabel('Position X (meters)')
        plt.ylabel('Position Y (meters)')
        plt.title('Map' , fontweight='bold')
        plt.grid()
        
        # 3d space 
        trajectory = fig.add_subplot(223, projection='3d')
        trajectory.plot(obs[:,0], obs[:,1], obs[:,2],'k+', label='noisy measurements')
        trajectory.plot(est[:,0], est[:,1], est[:,2],'bo', label='a posteri estimate')
        trajectory.plot(truth_value[:,0], truth_value[:,1], truth_value[:,2], 'go', label='truth value')
        trajectory.set_xlabel('Position X (meters)')
        trajectory.set_ylabel('Position Y (meters)')
        trajectory.set_zlabel('Position Z (meters)')
        plt.title('3D space' , fontweight='bold')
        plt.grid()
        
        # diagram with respect to X
        pos_X = fig.add_subplot(322)
        pos_X.plot(obs[:,0],'k+', label='noisy measurements')
        pos_X.plot(est[:,0],'b-', label='a posteri estimate')
        pos_X.axhline(kf.truth_value[0], color='g', label='truth value')
        plt.title('Estimate vs. iteration step', fontweight='bold')
        plt.ylabel('Position X (meters)')
        plt.grid()
        
        # diagram with respect to Y
        pos_Y = fig.add_subplot(324)
        pos_Y.plot(obs[:,1],'k+', label='noisy measurements')
        pos_Y.plot(est[:,1],'b-', label='a posteri estimate')
        pos_Y.axhline(kf.truth_value[1], color='g', label='truth value')
        plt.xlabel('Iteration')
        plt.ylabel('Position Y (meters)')
        plt.grid()
        
        # diagram with respect to Z
        pos_Y = fig.add_subplot(326)
        pos_Y.plot(obs[:,2],'k+', label='noisy measurements')
        pos_Y.plot(est[:,2],'b-', label='a posteri estimate')
        pos_Y.axhline(kf.truth_value[2], color='g', label='truth value')
        plt.xlabel('Iteration')
        plt.ylabel('Position Z (meters)')
        plt.grid()
        
        # plot all
        plt.show()


# MAIN FUNCTION
def main():
    """
    # CALL KALMAN FILTER FOR 1D SPACE
    # input initial data
    print('INITIAL DATA')
    truth_value = float(input('Truth value: '))
    init_guess = float(input('Initial guess: '))
    n_iter = int(input('Number of iterations: '))
    
    # initialize an instance of KalmanFilter
    kf_1d = kf(truth_value, init_guess, n_iter)
    kftest_1d = PositionKF()

    # estimate, print out results and plot all 
    obs, est = kf_1d.estimate()
    kftest_1d.print_out(obs, est, kf_1d)
    kftest_1d.plot1d(obs, est, kf_1d)
    
    
    # CALL KALMAN FILTER FOR 2D SPACE
    # initialize an instance of PositionKF
    kftest_2d = PositionKF()
    
    # get initial data and initialize an instance of KalmanFilter 
    truth_value, init_guess, n_iter = kftest_2d.init2d()
    kf_2d = kf(truth_value, init_guess, n_iter)
    
    # estimate, print out results and plot all 
    obs, est = kf_2d.estimate()
    kftest_2d.print_out(obs, est, kf_2d)
    kftest_2d.plot2d(obs, est, kf_2d)
    """
    
    # CALL KALMAN FILTER FOR 3D SPACE
    # initialize an instance of PositionKF
    kftest_3d = PositionKF()
    
    # get initial data and initialize an instance of KalmanFilter
    truth_value, init_guess, n_iter = kftest_3d.init3d()
    kf_3d = kf(truth_value, init_guess, n_iter)

    # estimate, print out results and plot all
    obs, est = kf_3d.estimate()
    kftest_3d.print_out(obs, est, kf_3d)
    kftest_3d.plot3d(obs, est, kf_3d)
    

if __name__ == '__main__':
    main()
    