"""
Rotation
"""

class Rotation:
    pass 


class ConstRotation(Rotation): 
    def initialize(dim=2, mock=True, display=True):
        if dim == 2:
            if mock == True:
                # mock initial data (in angles)
                truth_yaw = 50.0
                init_yaw = 45
                
                # find out the frequency and error of MEMS gyroscope in reality!
                
                frequency = 2.0
                time_sec = 30
            
            else: 
                # input initial data
                print('INPUT INITIAL DATA')
                truth_yaw = float(input('Truth yaw: '))
                init_yaw = float(input('Initial yaw: '))
                frequency = float(input('Frequency: '))
                time_sec = float(input('Time (sec): '))
                
                # convert initial data into arrays 
                truth_value = (truth_value_X, truth_value_Y)
                init_guess = (init_guess_X, init_guess_Y)
            
            if display == True:
                # print out dummy data
                print('INITIAL DATA:')
                print(f'Truth value of yaw: {truth_yaw}')
                print(f'Initial guess: {init_yaw}')
                print(f'Frequency (Hz): {frequency}')
                print(f'Time (seconds): {time_sec}')
            
            # time delay of accelerometer between measurements
            dt = 1 / frequency
            n_yaw = int(time_sec / dt)
            
            return (truth_yaw, init_yaw, time_sec, n_yaw)
        
        if dim == 3: 
            pass 


class DifferentRotation(Rotation):
    pass 
