import sys, traceback

sys.path.append('../console')
sys.path.append('../physical_models')
sys.path.append('../signal_processing')
sys.path.append('../control_algorithms')

from console.console import Console as console
from physical_models.car import Car
from signal_processing.spa import SignalProcessingAlgorithm as SPA
from control_algorithms.fuzzy_driver_miso import FuzzyDriverMiso
from control_algorithms.fuzzy_driver_siso import FuzzyDriverSiso


class Invoke: 
    """
    Calls Kalman Filter for GPS, IMU (that consists of GPS, gyro, 
    accelerometer) and Fuzzy controller.
    """

    def imu(mode):
        """
        Allows to invoke all required modules in order to execute IMT module 
        that consists of GPS, speedometer, accelerometer. 

        Takes `mode` as an input parameter that indicates car's motion pattern
        (for example, constant position `p`, constant speed `v` or random 
        acceleration `a`). 
        """

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
                                        is_default=is_default)
            
            # invoke Kalman filter for processing IMU data.  
            spa = SPA()
            spa.imu_kf(dimension=dim, init_data=init_data)
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
                                        is_default=is_default)
            
            # invoke Kalman filter for processing GPS data.  
            spa = SPA()
            spa.gps_kf(dimension=dim, init_data=init_data)
        except Exception as e:
            print('Exception: '.upper(), e)
            traceback.print_tb(e.__traceback__)
            init_data = None


    def fuzzy():
        try:
            is_miso = console.is_miso_fuzzy()
            if is_miso == True: 
                fc = FuzzyDriverMiso()
                fc.call() 
            else: 
                fc = FuzzyDriverSiso()
                fc.call()
        except Exception as e:
            print('Exception: '.upper(), e)
            traceback.print_tb(e.__traceback__)
