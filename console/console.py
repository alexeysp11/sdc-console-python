"""
Add position, computer vision, fuzzy controller and Car2D modules.

Google how to write comlex console app.
"""

import sys
sys.path.append('../RTLS')
from sensors.gps import GpsKF
from sensors.gyro import GyroKF
sys.path.append('../DATMO')
from lidar import Lidar


if __name__ == '__main__':
    print('Welcome to SDC console!')
    
    while True:
        # get user's purpose
        command = input('>> ')
        
        # add exception handling!
        if command == 'sdc gps':
            plot = True
            
            # enter custom position, speed and time!
            
            kf_1d = GpsKF()
            kf_1d.callkf(plot=plot, dimension=1)
            
            kf_2d = GpsKF()
            kf_2d.callkf(plot=plot, dimension=2)
        
        elif command == 'sdc position':
            velocity = 0 
            
            # then you need to pass velocity to 
            kf_1d = GpsKF()
            kf_1d.callkf(plot=plot, dimension='1D', velocity=0)
            
            kf_2d = GpsKF()
            kf_2d.callkf(plot=plot, dimension='2D', velocity=0)
        
        elif command == 'sdc gyro':
            gyro_1d = GyroKF()
            gyro_1d.callkf(dim=2)
        
        elif command == 'sdc lidar':
            lidar = Lidar()
            lidar.call_lidar()
        
        elif command == 'sdc -info':
            # use a table and wait for command again!
            print('''Information:
            rtls        | real time locating system
            gps         | display each algorithm just once (velocity)
            position    | simple 
            gyro        | gyroscope
            lidar       | lidar
            fuzzy       | fuzzy controller 
            cv          | computer vision 
            test        | unit tests for each module
            exit        | exit 
            ''')
            iterations = []
        
        elif command == 'sdc exit':
            break
        