import sys, traceback
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

sys.path.append('../sensors')
sys.path.append('../math')

from sensors.sensor import Sensor 
from maths.kalman_filter import KalmanFilter 


class SignalProcessingAlgorithm: 
    def gps_kf(self, dimension=1, init_data=0):
        """
        Invokes Kalman filter for 1D and 2D and plots graphs.  
        """
        
        abs_error = 10.0
        
        try:
            sensor = Sensor()
            kf = KalmanFilter(error=abs_error)
            
            # generate GPS observations. 
            obs, time = sensor.measure(init_data, abs_error=abs_error, unit='position')
            
            # estimate position using Kalman filter  
            est = kf.estimate(obs)
            
            # print out results and plot all. 
            self.mean, self.median, est_error = self.print_out(obs, est, 
                init_data)
            
            self.plot(obs=obs, est=est, est_error=est_error, time=time,  
                init_data=init_data, dim=dimension, sensor='gps')
        
        except Exception as e:
            print('Exception: '.upper(), e)
            traceback.print_tb(e.__traceback__)


    def imu_kf(self, dimension=1, init_data=0):
        """
        Invokes Kalman filter for 1D and 2D and plots graphs.  
        """

        dt_gps = 1.0
        dt_speed = 1.0
        dt_accel = 1.0
        gps_error = 50.0
        
        try:
            sensor = Sensor()
            kf = KalmanFilter(error=gps_error)
            
            # generate GPS observations. 
            gps_obs, time = sensor.measure(init_data, abs_error=gps_error, unit='position', dt=dt_gps)
            
            # estimate position using GPS data
            est_gps = kf.estimate(observations=gps_obs)
            
            # generate speedometer and accelerometer observations. 
            speed_obs, time = sensor.measure(init_data, abs_error=0.1, unit='velocity', dt=dt_speed)
            accel_obs, time = sensor.measure(init_data, abs_error=0.01, unit='acceleration', dt=dt_accel)

            # correct postion observations
            gps_rows = len(est_gps[:,0])
            speed_rows = len(speed_obs[:,0])
            accel_rows = len(accel_obs[:,0])
            corrected_position = np.ones((accel_obs.shape))
            k = 0
            for i in range(gps_rows): 
                for j in range(int(accel_rows/gps_rows)): 
                    corrected_position[k] = est_gps[i]
                    k += 1
            k = 0
            for i in range(speed_rows): 
                for j in range(int(accel_rows/speed_rows)): 
                    corrected_position[k] += speed_obs[i] * dt_speed
                    k += 1
            for i in range(accel_rows): 
                corrected_position[i] += accel_obs[i] * dt_accel**2 / 2
            
            # estimate corrected position data
            est = kf.estimate(observations=corrected_position)
            
            # print out results. 
            self.mean, self.median, est_error = self.print_out(corrected_position, est, init_data, dt_accel)
            
            # plot results
            self.plot(obs=corrected_position, est=est, est_error=est_error, 
                time=time, init_data=init_data, dim=dimension, sensor='multisensor')
        except Exception as e:
            print('Exception: '.upper(), e)
            traceback.print_tb(e.__traceback__)
    

    def state_observer():
        pass 


    def print_out(self, obs, est, init_data, dt=1.0, table=True):
        """
        Calculates and print out measures of central tendency (median, mean)
        and print them out. 

        Returns: 

        `mean`: mean value of camputational error.
        
        `median`: mean value of camputational error.

        `error`: array of difference between estimations and truth value. 
        """

        try:
            init_value = init_data[0]
            init_value = init_value[0]
            
            # reshape for a table (for 1D)
            if type(init_value) is float:
                obs = obs.reshape((len(obs), 1))
                est = est.reshape((len(est), 1))
            
            # round values for printing out a table!
            obs = np.round(obs, 3)
            est = np.round(est, 3)

            # assign truth value
            truth_value = np.ones((est.shape))
            k = 0
            for i in range(len(init_value)):
                for j in range(int(1/dt)):
                    if i == len(init_value)-1 or j == int(1/dt)-1:
                        truth_value[k] = init_value[i]
                    elif j == int(1/dt): 
                        truth_value[k] = init_value[i]
                    else:
                        truth_value[k] = init_value[i] + (init_value[i+1] - init_value[i]) * dt * j
                    k += 1
            
            # calculate error of estimations
            error = np.round(truth_value - est, 3)
            
            # make a table
            if table == True:
                if type(truth_value) == float: 
                    data = [[est, error, obs]]
                    headers = ['Estimations', 'Error', 'Observations']
                    print('\nDATA PROCESSING:')
                    print(tabulate(data, headers=headers))
                elif len(truth_value) <= 20:
                    data = [[truth_value, est, error, obs]]
                    headers = ['Truth value', 'Estimations', 'Error', 'Observations']
                    print('\nDATA PROCESSING:')
                    print(tabulate(data, headers=headers))
            
            # get number of columns
            cols = len(error[0,:])
            
            # final info about algorithm accuracy
            if cols == 1:   # for 1D 
                # calculate measures of central tendency
                median = np.round(np.median(abs(error)))
                mean = np.round(np.mean(abs(error)))
                # print out info 
                print('Measures of central tendency of error:')
                print(f'median = {median}, mean = {mean}')
            if cols == 2:   # for 2D 
                # calculate measures of central tendency
                median_X = np.round(np.median(abs(error[:,0])), 3)
                median_Y = np.round(np.median(abs(error[:,1])), 3)
                mean_X = np.round(np.mean(abs(error[:,0])), 3)
                mean_Y = np.round(np.mean(abs(error[:,1])), 3)
                mean = np.array([[mean_X, mean_Y]])
                median = np.array([[median_X, median_Y]])
                # print out info
                print('Measures of central tendency of error:')
                print(f'median_X = {median_X}, mean_X = {mean_X}')
                print(f'median_Y = {median_Y}, mean_Y = {mean_Y}')
            print()

            return mean, median, error
        except Exception as e:
            print('Exception: '.upper(), e)
            traceback.print_tb(e.__traceback__)
            return None, None


    def plot(self, obs, est, est_error, time, init_data, dim, sensor, animation=False):
        """
        Responsible for visual representation of position estimation. 

        For 1D space, plots position vs time relationship and histograms 
        of measurement and estimation errors distribution. 
        
        For 2D space, plots 2D map, position vs time relationship and 
        histograms of measurement and estimation errors distribution. 
        """

        # define labels of each axis for each sensor. 
        if (sensor == 'gps' or sensor == 'multisensor'): 
            truth_label = 'truth value'
            ylabel = 'Position (meters)'
        if sensor == 'gyro': 
            truth_label = 'truth yaw'
            ylabel = 'Rotation (degrees)'
        
        # plot map, position vs time relationship and histograms of error 
        # distribution. 
        try:
            fig = plt.figure()
            init_value = init_data[0]
            init_value = init_value[0]
            dt = time[1] - time[0]

            # assign truth value
            truth_value = np.ones((est.shape))
            k = 0
            for i in range(len(init_value)):
                for j in range(int(1/dt)):
                    if i == len(init_value)-1 or j == int(1/dt)-1:
                        truth_value[k] = init_value[i]
                    elif j == int(1/dt): 
                        truth_value[k] = init_value[i]
                    else:
                        truth_value[k] = init_value[i] + (init_value[i+1] - init_value[i]) * dt * j
                    k += 1
            
            if (dim == 1 and (sensor == 'gps' or sensor == 'multisensor')) or (dim == 2 and sensor == 'gyro'): 
                plt.plot(obs,'k+', label='noisy measurements')
                plt.plot(est,'b-', label='a posteri estimate')
                
                if type(truth_value) == float:
                    plt.axhline(truth_value, color='g', label=truth_label)
                else:
                    plt.plot(truth_value, color='g', label=truth_label)
                
                plt.legend()
                plt.title(f'{sensor} data processing'.upper(), fontweight='bold')
                plt.xlabel('Time (seconds)')
                plt.ylabel(ylabel)
                plt.grid()
            
            if (dim == 2 and (sensor == 'gps' or sensor == 'multisensor')) or (dim == 3 and sensor == 'gyro'): 
                """
                In order to drawing plots for 2d space location estimating, we plot: 
                1) 2 diagrams of Estimation vs Data with respect to each 
                axis, 
                2) one diagram which represents a map with car's 
                trajectory in 2d space. 
                """
                
                # 2D map 
                mapping = fig.add_subplot(121)
                mapping.plot(obs[:,0], obs[:,1],'k+', label='noisy measurements')
                mapping.plot(est[:,0], est[:,1],'bo', label='a posteri estimate')

                is_moving_X = False
                is_moving_Y = False
                observation_num = len(truth_value[:,0])

                # check if position of a car does not change (for plotting a 
                # point not a line in the case). 
                for i in range(observation_num):
                    # check if it is the last element. 
                    if i == (observation_num - 1): 
                        break
                    
                    # check if a car is moving on the x axis. 
                    if truth_value[i,0] != truth_value[i+1,0]: 
                        is_moving_X = True
                    
                    # check if a car is moving on the y axis. 
                    if truth_value[i,1] != truth_value[i+1,1]: 
                        is_moving_Y = True
                
                # if a car is not moving, position of a car should be represented by point. 
                if (is_moving_X == False) and (is_moving_Y == False):  
                    mapping.plot(truth_value[:,0], truth_value[:,1], 'go', label='truth value')
                else:
                    mapping.plot(truth_value[:,0], truth_value[:,1], 'g', label='truth value')
                
                plt.xlabel('Position X (meters)')
                plt.ylabel('Position Y (meters)')
                plt.title('2d map'.upper(), fontweight='bold')
                plt.legend()
                plt.grid()
                
                # diagram with respect to X
                pos_X = fig.add_subplot(222)
                pos_X.plot(time, obs[:,0],'k+')
                pos_X.plot(time, est[:,0],'b-')
                pos_X.plot(time, truth_value[:,0], color='g')
                plt.title(f'{sensor} data processing'.upper(), fontweight='bold')
                plt.ylabel('Position X (meters)')
                plt.grid()
                
                # diagram with respect to Y
                pos_Y = fig.add_subplot(224)
                pos_Y.plot(time, obs[:,1],'k+')
                pos_Y.plot(time, est[:,1],'b-')
                pos_Y.plot(time, truth_value[:,1], color='g')
                plt.xlabel('Time (seconds)')
                plt.ylabel('Position Y (meters)')
                plt.grid()

            # histograms of error distribution. 
            histograms = plt.figure()
            if (dim == 1 and (sensor == 'gps' or sensor == 'multisensor')) or (dim == 2 and sensor == 'gyro'): 
                plt.hist(est_error, edgecolor = 'black')
                plt.xlabel('Error (meters)')
                plt.ylabel('Number of examples')
                plt.title(f'Error histogram ({sensor})'.upper(), fontweight='bold')
            elif (dim == 2 and (sensor == 'gps' or sensor == 'multisensor')) or (dim == 3 and sensor == 'gyro'): 
                histograms.suptitle(f'Error histograms ({sensor})'.upper(), fontweight='bold')

                hist_X = histograms.add_subplot(121)
                hist_X.hist(est_error[:,0], edgecolor = 'black')
                hist_X.set_ylabel('Number of examples')
                hist_X.set_xlabel ('Error along X axis (meters)')

                hist_Y = histograms.add_subplot(122)
                hist_Y.hist(est_error[:,1], edgecolor = 'black')
                hist_Y.set_ylabel ('Number of examples')
                hist_Y.set_xlabel ('Error along Y axis (meters)')
            plt.show()
        except Exception as e:
            print('Exception: '.upper(), e)
            traceback.print_tb(e.__traceback__)
