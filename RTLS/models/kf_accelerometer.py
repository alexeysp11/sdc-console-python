# Kalman filter for accelerometer in 1D and 2D space 

import numpy as np


class KalmanFilter:
    def __init__(self, truth_value, init_guess, n_iter):
        # truth_value probably should be an array! 
        self.truth_value = truth_value
        self.init_guess = init_guess
        self.n_iter = n_iter 


    def estimate(self):
        # this algorithm works badly with moving car with acceleration! 
        
        n_iter = self.n_iter 
        array_size = self.truth_value.shape
        
        """
        # if 1D space (type is float)
        if type(self.truth_value) is float:
            array_size = (n_iter,)
        
        # if 2D space (type is tuple) 
        if type(self.truth_value) is tuple:
            n_dimension = len(self.truth_value)
            array_size = (n_iter, n_dimension) 
        """
        
        truth_value = self.truth_value
        abs_error = 50
        sigma = abs_error / 2 
        
        # determine observations
        observations = np.ones(array_size)
        observations = np.random.normal(truth_value, sigma, size=array_size)
        
        # process variance Q
        process_var = sigma * 5

        # ALLOCATE SPACE FOR ARRAYS
        aposteri_est = np.ones(array_size) * truth_value
        aposteri_error = np.ones(array_size) * sigma
        apriori_est = np.ones(array_size) * truth_value
        apriori_error = np.ones(array_size) * sigma
        kalman_gain = np.zeros(array_size)
        mes_var = sigma**2 # estimate of measurement variance R 

        # intial guesses
        aposteri_est[0] = self.init_guess
        aposteri_error[0] = sigma

        # etimate location for every iteration
        for k in range(1, n_iter):
            # time update
            apriori_est[k] = aposteri_est[k-1]
            apriori_error[k] = aposteri_error[k-1] + process_var

            # measurement update
            kalman_gain[k] = apriori_error[k]/(apriori_error[k] + mes_var)
            aposteri_est[k] = apriori_est[k] + kalman_gain[k]*(observations[k] - apriori_est[k])
            aposteri_error[k] = (1 - kalman_gain[k]) * apriori_error[k]

        return observations, aposteri_est
