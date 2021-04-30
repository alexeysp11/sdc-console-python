import numpy as np

class KalmanFilter:
    """
    Adaptive Kalman filter that can estimate a state of a car 
    when it's changing motion pattern.  
    """

    def __init__(self, observations, error):
        self.observations = observations
        self.error = error

    def estimate(self):
        # initial parameters 
        observations = self.observations
        abs_error = self.error
        
        time_sec = len(observations)
        array_size = observations.shape
        sigma = abs_error * 2 
        
        # allocate space for arrays
        aposteri_est = np.ones(array_size) * observations[0]
        aposteri_error = np.ones(array_size) * sigma
        apriori_est = np.ones(array_size) * observations[0]
        apriori_error = np.ones(array_size) * sigma
        kalman_gain = np.zeros(array_size)
        mes_var = sigma**2                          # estimate of measurement variance R 
        process_var = np.ones(array_size) * sigma   # process variance Q
        
        # intial guesses
        aposteri_est[0] = observations[0]
        aposteri_error[0] = process_var[0]

        # etimate location for every iteration
        for k in range(1, time_sec):
            # time update
            apriori_est[k] = aposteri_est[k-1] # here you can add accelerometer and tachometer data (apriori_est[k] = aposteri_est[k-1] + tachometer*dt + 1/2*accelerometer * dt**2). 
            
            # get number of columns
            cols = len(aposteri_error[0,:])
            
            # for 1D space
            if cols == 1:
                if k != 1 and (aposteri_error[k-1] < aposteri_error[k-2]): 
                    apriori_error[k] = aposteri_error[k-1] - process_var[k-1]
                else: 
                    apriori_error[k] = aposteri_error[k-1] + process_var[k-1]
                
                # add residuals to observations
                v = observations[k] - apriori_est[k]
                observations[k] = observations[k] + v
                
                # measurement update
                kalman_gain[k] = apriori_error[k]/(apriori_error[k] + mes_var)
                aposteri_est[k] = apriori_est[k] + kalman_gain[k]*(observations[k] - apriori_est[k])
                aposteri_error[k] = (1 - kalman_gain[k]) * apriori_error[k]
            
            # for 2D space 
            if cols == 2:
                if k != 1:
                    # X axis
                    if (aposteri_error[k-1, 0] < aposteri_error[k-2, 0]): 
                        apriori_error[k, 0] = aposteri_error[k-1, 0] - process_var[k-1, 0]
                    else: 
                        apriori_error[k, 0] = aposteri_error[k-1, 0] + process_var[k-1, 0]
                    
                    # Y axis
                    if (aposteri_error[k-1, 1] < aposteri_error[k-2, 1]): 
                        apriori_error[k, 1] = aposteri_error[k-1, 1] - process_var[k-1, 1]
                    else: 
                        apriori_error[k, 1] = aposteri_error[k-1, 1] + process_var[k-1, 1]
                
                else: 
                    apriori_error[k, 0] = aposteri_error[k-1, 0] + process_var[k-1, 0]
                    apriori_error[k, 1] = aposteri_error[k-1, 1] + process_var[k-1, 1]

                # add residuals to observations
                v = observations[k] - apriori_est[k]
                observations[k] = observations[k] + v
                
                # measurement update
                kalman_gain[k, 0] = apriori_error[k, 0]/(apriori_error[k, 0] + mes_var)
                kalman_gain[k, 1] = apriori_error[k, 1]/(apriori_error[k, 1] + mes_var)
                aposteri_est[k, 0] = apriori_est[k, 0] + kalman_gain[k, 0]*(observations[k, 0] - apriori_est[k, 0])
                aposteri_est[k, 1] = apriori_est[k, 1] + kalman_gain[k, 1]*(observations[k, 1] - apriori_est[k, 1])
                aposteri_error[k, 0] = (1 - kalman_gain[k, 0]) * apriori_error[k, 0]
                aposteri_error[k, 1] = (1 - kalman_gain[k, 1]) * apriori_error[k, 1]

        return aposteri_est
