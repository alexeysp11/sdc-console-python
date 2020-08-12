# Kalman filter for moving car in 1D and 2D space 

import numpy as np

class KalmanFilter:
    def __init__(self, observations):
        self.observations = observations

    def estimate(self):
        # initial parameters 
        observations = self.observations
        time_sec = len(observations)
        array_size = observations.shape
        abs_error = 50
        sigma = abs_error / 2 
        
        # process variance Q
        process_var = sigma 

        # allocate space for arrays
        aposteri_est = np.ones(array_size) * observations[0]
        aposteri_error = np.ones(array_size) * sigma
        apriori_est = np.ones(array_size) * observations[0]
        apriori_error = np.ones(array_size) * sigma
        kalman_gain = np.zeros(array_size)
        mes_var = sigma**2 # estimate of measurement variance R 

        # intial guesses
        aposteri_est[0] = self.observations[0]
        aposteri_error[0] = sigma

        # etimate location for every iteration
        for k in range(1, time_sec):
            # time update
            apriori_est[k] = aposteri_est[k-1]
            apriori_error[k] = aposteri_error[k-1] + process_var

            # measurement update
            kalman_gain[k] = apriori_error[k]/(apriori_error[k] + mes_var)
            aposteri_est[k] = apriori_est[k] + kalman_gain[k]*(observations[k] - apriori_est[k])
            aposteri_error[k] = (1 - kalman_gain[k]) * apriori_error[k]

        return aposteri_est
