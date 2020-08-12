# Kalman filter for gyroscope in 1D and 2D space 

import numpy as np

class KalmanFilter:
    # truth_value probably should be an array! 
    def __init__(self, truth_yaw, init_yaw, time_sec, n_yaw):
        self.truth_yaw = truth_yaw
        self.init_yaw = init_yaw
        self.time_sec = time_sec # because 20 iterations and 1 inital guess
        self.n_yaw = n_yaw


    def estimate(self):
        n_yaw = self.n_yaw 
        #array_size = self.truth_yaw.shape
        
        # if 1D space (type is float)
        if type(self.truth_yaw) is float:
            array_size = (n_yaw,)
        
        # if 2D space (type is tuple) 
        if type(self.truth_yaw) is tuple:
            n_dimension = len(self.truth_yaw)
            array_size = (n_yaw, n_dimension) 
        
        truth_yaw = self.truth_yaw
        abs_error = 15
        sigma = abs_error / 2 
        
        # determine observations
        observations = np.ones(array_size)
        observations = np.random.normal(truth_yaw, sigma, size=array_size)
        
        # process variance Q
        process_var = sigma / 20

        # allocate space for arrays
        aposteri_est = np.ones(array_size) * truth_yaw
        aposteri_error = np.ones(array_size) * sigma
        apriori_est = np.ones(array_size) * truth_yaw
        apriori_error = np.ones(array_size) * sigma
        kalman_gain = np.zeros(array_size)
        mes_var = sigma**2 # estimate of measurement variance R 

        # intial guesses
        aposteri_est[0] = self.init_yaw
        aposteri_error[0] = sigma

        # etimate location for every iteration
        for k in range(1, n_yaw):
            # time update
            apriori_est[k] = aposteri_est[k-1]
            apriori_error[k] = aposteri_error[k-1] + process_var

            # measurement update
            kalman_gain[k] = apriori_error[k]/(apriori_error[k] + mes_var)
            aposteri_est[k] = apriori_est[k] + kalman_gain[k]*(observations[k] - apriori_est[k])
            aposteri_error[k] = (1 - kalman_gain[k]) * apriori_error[k]

        return observations, aposteri_est
