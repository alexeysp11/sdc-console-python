import sys, traceback

sys.path.append('../console')
sys.path.append('../physical_models')
sys.path.append('../signal_processing')
sys.path.append('../control_algorithms')
sys.path.append('../computer_vision')

from console.console import Console as console
from physical_models.car import Car
from signal_processing.imu_kf import ImuKF
from signal_processing.gps_kf import GpsKF
from control_algorithms.fuzzy_driver import FuzzyDriver
#from MNIST.handwritten_digits import HandwrittenDigits
#from road_signs import signs_default

class Invoke: 
    """
    Calls Kalman Filter for GPS, IMU (that consists of GPS, gyro, 
    accelerometer) and Fuzzy controller.
    """

    def imu(mode):
        try:
            car = Car()
            dim = 2 

            # assign initial velocity for 1D. 
            velocity, is_accel = car.default_velocity(mode, dim=dim)

            # ask user if default parameters should be used for modeling. 
            is_default = console.is_default(dimension=dim)

            # get initial state of a car. 
            init_data = car.initialize(dimension=dim, 
                                        init_velocity=velocity, 
                                        mode=mode,
                                        is_accel=is_accel, 
                                        is_mock=is_default)
            
            # invoke Kalman filter for processing IMU data.  
            imu_kf = ImuKF()
            imu_kf.callkf(dimension=dim, init_data=init_data)
        
        except Exception as e:
                    print('Exception: '.upper(), e)
                    traceback.print_tb(e.__traceback__)
                    init_data = None


    def gps(mode):
        """
        Allows to invoke all required modules in order to execute GPS module. 

        Takes `mode` as an input parameter that indicates car's motion pattern
        (for example, constant position `p`, constant speed `v` or random 
        acceleration `a`). 
        """

        try:
            car = Car()
            dim = 2 
            
            # assign initial velocity. 
            velocity, is_accel = car.default_velocity(mode, dim=dim)
            
            # ask user if default parameters should be used for modeling. 
            is_default = console.is_default(dimension=dim)
            
            # get initial state of a car. 
            init_data = car.initialize(dimension=dim, 
                                        init_velocity=velocity, 
                                        mode=mode,
                                        is_accel=is_accel, 
                                        is_mock=is_default)
            
            # invoke Kalman filter for processing GPS data.  
            gps_kf = GpsKF()
            gps_kf.callkf(dimension=dim, init_data=init_data)
        
        except Exception as e:
                    print('Exception: '.upper(), e)
                    traceback.print_tb(e.__traceback__)
                    init_data = None


    def neural_network(mode, algorithm):
        try:
            """
            There is exception handling in if/else block too (programmer can set 
            mode or defualt variables in the wrong way, and I don't know how to 
            handle this exception not in if/else statement).
            
            So either watch carefully if the name of the file or the method 
            changes or think out how to use try/except in this situation.
            """
            pass 
            
            """
            if mode == 'mnist':
                mnist_custom = HandwrittenDigits()
                mnist_custom.run(algorithm)
            
            elif mode == 'signs':
                signs_default.run()
            
            else:
                print('Info for developer:'.upper())
                print('''Incorrect mode or algorithm values in: 
                neural_network(mode, algorithm) in invoke.py''')
            """
        
        except Exception as e:
            print('Exception: '.upper(), e)
            traceback.print_tb(e.__traceback__)


    def fuzzy():
        try:
            fc = FuzzyDriver()
            fc.call()
        
        except Exception as e:
            print('Exception: '.upper(), e)
            traceback.print_tb(e.__traceback__)


    def test():
        pass
